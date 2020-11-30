import angr

class Scope:
    def __init__(self, project):
        self.project = project
        pass

    def eval_variable_address(self, state, name):
        pass

    def state_in_scope(self, state):
        pass

class GlobalScope(Scope):
    def eval_variable_address(self, state, name):
        addr = self.project.loader.find_symbol(name).rebased_addr
        return addr

    def state_in_scope(self, state):
        return True

class FunctionScope(Scope):
    def eval_variable_address(self, state, name):
        pass

def eval_variable(operands, state):
    var_name = operands[0]
    var_type = operands[1]
    var_scope = operands[2]

    addr = var_scope.eval_variable_address(state, var_name)
    size = 8 if var_type.pointers > 0 else 2 ** (var_type.t.value - 1)

    return state.memory.load(addr, size, disable_actions=True, inspect=False)
