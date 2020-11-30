import Scope
import angr

def handle_violation(state, event):
    print(event.stmt + " was violated!")

class Event:
    def __init__(self, scope, general_constraint, stmt):
        self.scope = scope
        self.general_constraint = general_constraint
        self.stmt = stmt
    
    def subscribe(self):
        pass

    def get_event_condition(self, state):
        pass

    @staticmethod
    def breakpoint(events, state):
        for event in events:
            event_cond = get_event_condition(tmp_state)
            if type(event_cond) is bool:
                if not event_cond:
                    continue
            
            tmp_state = state.copy()
            tmp_state.solver.add(get_event_condition(tmp_state))
            tmp_state.solver.add(not general_constraint.get_sym(tmp_state))
            if tmp_state.solver.satisfiable():
                handle_violation(tmp_state, event)

class ReadEvent(Event):
    subscribed = False
    read_events = []

    def __init__(self, name, general_constraint, stmt):
        super().__init__(scope, general_constraint, stmt)
        self.name = name

    def subscribe(self, state):
        read_events.append(self)
        if not subscribed:
            subscribed = True
            state.inspect.b("mem_read", when=angr.BP_BEFORE, 
                            action=lambda state: Event.breakpoint(read_events, state))

    def get_event_condition(self, state):
        if self.scope.state_in_scope(state):
            return state.inspect.mem_read_address == self.scope.eval_variable_address(state, self.name)
        else:
            return False

class WriteEvent(Event):
    subscribed = False
    write_events = []

    def __init__(self, name, scope, general_constraint, stmt):
        super().__init__(scope, general_constraint, stmt)
        self.name = name

    def subscribe(self, state):
        write_events.append(self)
        if not subscribed:
            subscribed = True
            state.inspect.b("mem_write", when=angr.BP_BEFORE, 
                            action=lambda state: Event.breakpoint(write_events, state))

    def get_event_condition(self, state):
        if self.scope.state_in_scope(state):
            return state.inspect.mem_read_address == self.scope.eval_variable_address(state, self.name)
        else:
            return False

class CallEvent(Event):
    subscribed = False
    call_events = []

    def __init__(self, name, scope, general_constraint, stmt):
        super().__init__(scope, general_constraint, stmt)
        self.name = name

    def subscribe(self, state):
        call_events.append(self)
        if not subscribed:
            subscribed = True
            state.inspect.b("call", when=angr.BP_BEFORE, 
                            action=lambda state: Event.breakpoint(call_events, state))

    def get_event_condition(self, state):
        if self.scope.state_in_scope(state):
            if self.name == None:
                return True
            return state.inspect.function_address == self.name # TODO: Verify function_address
        else:
            return False

class ReturnEvent:
    subscribed = False
    ret_events = []

    def subscribe(self, state):
        ret_events.append(self)
        if not subscribed:
            subscribed = True
            state.inspect.b("return", when=angr.BP_BEFORE, 
                            action=lambda state: Event.breakpoint(return_events, state))

    def get_event_condition(self, state):
        return True

class AlwaysEvent(WriteEvent):
    def get_event_condition(self, state):
        return True