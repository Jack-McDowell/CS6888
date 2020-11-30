from varparse import Scope
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
            event_cond = event.get_event_condition(state)
            if type(event_cond) is bool:
                if not event_cond:
                    continue
            
            tmp_state = state.copy()
            tmp_state.solver.add(event_cond)
            tmp_state.solver.add(not general_constraint.get_sym(state))
            if tmp_state.solver.satisfiable():
                handle_violation(tmp_state, event)

class ReadEvent(Event):
    subscribed = False
    read_events = []

    def __init__(self, name, scope, general_constraint, stmt):
        super().__init__(scope, general_constraint, stmt)
        self.name = name

    def subscribe(self, state):
        read_events.append(self)
        if not ReadEvent.subscribed:
            ReadEvent.subscribed = True
            state.inspect.b("mem_read", when=angr.BP_BEFORE, 
                            action=lambda state: Event.breakpoint(ReadEvent.read_events, state))

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
        if not WriteEvent.subscribed:
            WriteEvent.subscribed = True
            state.inspect.b("mem_write", when=angr.BP_BEFORE, 
                            action=lambda state: Event.breakpoint(WriteEvent.write_events, state))

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
        if not CallEvent.subscribed:
            CallEvent.subscribed = True
            state.inspect.b("call", when=angr.BP_BEFORE, 
                            action=lambda state: Event.breakpoint(CallEvent.call_events, state))

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
        if not ReturnEvent.subscribed:
            ReturnEvent.subscribed = True
            state.inspect.b("return", when=angr.BP_BEFORE, 
                            action=lambda state: Event.breakpoint(ReturnEvent.return_events, state))

    def get_event_condition(self, state):
        return True

class AlwaysEvent:
    subscribed = False
    always_events = []
    def subscribe(self, state):
        always_events.append(self)
        if not AlwaysEvent.subscribed:
            AlwaysEvent.subscribed = True
            state.inspect.b("mem_write", when=angr.BP_AFTER, 
                            action=lambda state: Event.breakpoint(AlwaysEvent.always_events, state))
            state.inspect.b("call", when=angr.BP_AFTER, 
                            action=lambda state: Event.breakpoint(AlwaysEvent.always_events, state))
    
    def get_event_condition(self, state):
        return True