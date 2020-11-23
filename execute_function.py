import angr
import claripy
import archinfo

binary = angr.Project("./test")

inp = claripy.BVS("input", 128)

def read_global(state, name, byte_cnt=8):
    global binary
    addr = binary.loader.find_symbol(name).rebased_addr
    memory = state.memory.load(addr, byte_cnt, disable_actions=True, inspect=False)
    return memory

no_reads = {
    "secret": lambda state: (0 == read_global(state, "allowed", 1))
}

def on_break(state):
    for no_read in no_reads:
        cond = no_reads[no_read](state)
        addr = binary.loader.find_symbol(no_read).rebased_addr
        cpy = state.copy()
        cpy.solver.add(state.inspect.mem_read_address == addr)
        cpy.solver.add(cond)
        if cpy.solver.satisfiable():
            print("Illegal memory address " + hex(addr) + " accessed")
            concrete_addr = cpy.solver.eval(state.inspect.mem_read_address)
            print("    Data contained: " + str(cpy.memory.load(concrete_addr, 8, disable_actions=True, inspect=False, endness=archinfo.Endness.LE)))
            print("    Accessing instruction address: " + str(cpy.regs.rip))
            concrete_input = cpy.solver.eval(inp)
            print("    Input responsible: " + str(concrete_input.to_bytes(int(concrete_input.bit_length() / 8 + 1), "big")))

state = binary.factory.full_init_state(argc=2, args=["test", inp])
state.inspect.b("mem_read", when=angr.BP_AFTER, action=lambda state: on_break(state))
sim = binary.factory.simgr(state)
states = sim.explore().deadended
for s in states:
    print(hex(s.solver.eval(inp)))
