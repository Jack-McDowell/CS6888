import angr, archinfo

from elfparse import get_function_bounds, get_var_stack_offset

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
    def __init__(self, project, function_name):
        super().__init__(self, project)
        self.base, self.end = get_function_bounds(function_name)
        self.func = function_name

    def eval_variable_address(self, state, name):
        frame = get_stack_frame(self, state)
        return frame.stack_pointer + get_var_stack_offset(self.project, self.func, name)

    def state_in_scope(self, state):
        return not self.get_stack_frame(state) == None

    def get_stack_frame(self, state):
        for callsite in state.callstack:
            if callsite == self.base: # TODO: Treat as symbolic?
                return callsite
        return None

def eval_variable(operands, state, lval=False):
    var_name = operands[0]
    var_type = operands[1]
    var_scope = operands[2]

    addr = var_scope.eval_variable_address(state, var_name)
    size = 8 if var_type.pointers > 0 else 2 ** (var_type.t.value - 1)

    return addr if lval else state.memory.load(addr, size, disable_actions=True, inspect=False, endness=archinfo.Endness.LE)
