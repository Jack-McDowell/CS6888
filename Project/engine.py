import angr, claripy

class Engine:
    def __init__(self, project, invariants):
        self.file_path = project.filename
        self.proj = project
        self.inp = claripy.BVS("input", 4096)
        self.state = self.proj.factory.full_init_state(argc=2, args=[self.file_path, self.inp])
        self.simgr = None

        for evt in invariants:
            evt.set_engine(self)
            evt.subscribe(self.state)
    
    def handle_violation(self, state, conds, evt):
        print(evt.stmt + " was violated by input " + str(state.solver.eval(self.inp, extra_constraints=conds, cast_to=bytes)))

    def run(self):
        self.simgr = self.proj.factory.simgr(self.state, resilience=None)
        self.simgr.explore()
