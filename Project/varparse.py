import angr

import ExprType

class Scope:
    def __init__(self, project):
        self.project = project
        pass

    def eval_variable_address(self, name):
        pass

class GlobalScope(Scope):
    def eval_variable_address(self, name, state):
        addr = self.project.loader.find_symbol(name).rebased_addr
        return addr

class FunctionScope(Scope):
    def eval_variable_address(self, name, state):
        pass

def eval_variable(operands, state):
    var_name = operands[0]
    var_type = operands[1]
    var_scope = operands[2]

    addr = var_scope.eval_variable_address(var_name, state)
    size = var_type.get_pointed_size()

    return state.memory.load(addr, size, disable_actions=True, inspect=False)