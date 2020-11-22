import angr
import claripy

def sym_i64():
    pass
def sym_i32():
    pass
def sym_i8():
    pass
def sym_str():
    pass

def get_function_state(binary, name, *args):
    sym = binary.loader.main_object.get_symbol(name)
    if sym == None:
        print("Unable to find symbol " + name)
        return None

    return binary.factory.call_state(sym.rebased_addr, args)

buf = claripy.BVS("query", 1024)
def on_break(state):
    global buf
    print("Oh no!")
    l = list(state.solver.get_variables())
    for v in l:
        val = state.solver.eval(v[1])
        print(str(v[0]) + ": " + str(val))
    print("Buffer: " + str(state.solver.eval(buf)))

def can_violate(state):
    print(list(state.solver.get_variables()))
    return True

binary = angr.Project("./test")
buf = claripy.BVS("query", 1024)
state = binary.factory.call_state(binary.loader.find_symbol("execute_query").rebased_addr, args=[buf])
state.inspect.b("mem_read", when=angr.BP_BEFORE, action=on_break, mem_read_address=binary.loader.find_symbol("password").rebased_addr)
sim = binary.factory.simgr(state)
states = sim.run().deadended
for s in states:
    print("Eval: " + str(s.solver.eval(buf)))
    can_violate(s)
