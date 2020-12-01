import angr

class Engine:
    def __init__(self, project, invariants):
        self.file_path = project.filename
        self.proj = project
        self.inp = claripy.BVS("input", 4096)
        self.state = self.proj.factory.full_init_state(argc=2, args=[self.file_path, inp])
        self.simgr = None

        for evt in invariants:
            evt.set_engine(self)
            evt.subscribe(state)
    
    def handle_violation(self, state, evt):
        print(evt.stmt + " was violated by input " + hex(state.solver.eval(self.inp)))

    def run():
        self.simgr = self.proj.factory.simgr(self.state)
        self.simgr.explore()