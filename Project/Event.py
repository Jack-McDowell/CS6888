from varparse import Scope
import angr

class Event:
    def __init__(self, scope, general_constraint, stmt):
        self.scope = scope
        self.general_constraint = general_constraint
        self.stmt = stmt
        self.engine = None
    
    def subscribe(self):
        pass

    def get_event_condition(self, state):
        pass

    def set_engine(self, engine):
        self.engine = engine

    @staticmethod
    def breakpoint(evt, state):
        for event in evt.__class__.events:
            event_cond = event.get_event_condition(state)
            
            if (type(event_cond) is bool and not event_cond) or state.solver.is_false(event_cond):
                continue

            gen_c = event.general_constraint.get_sym(state) == False
            if state.solver.satisfiable(extra_constraints=[event_cond, gen_c]):
                evt.engine.handle_violation(state, [event_cond, gen_c], event)

class ReadEvent(Event):
    subscribed = False
    events = []

    def __init__(self, ast, scope, general_constraint, stmt):
        super().__init__(scope, general_constraint, stmt)
        self.ast = ast

    def subscribe(self, state):
        ReadEvent.events.append(self)
        if not ReadEvent.subscribed:
            ReadEvent.subscribed = True
            state.inspect.b("mem_read", when=angr.BP_BEFORE, 
                            action=lambda state: Event.breakpoint(self, state))

    def get_event_condition(self, state):
        if self.scope.state_in_scope(state):
            return state.inspect.mem_read_address == self.ast.get_sym(state, True)
        else:
            return False

class WriteEvent(Event):
    subscribed = False
    events = []

    def __init__(self, ast, scope, general_constraint, stmt):
        super().__init__(scope, general_constraint, stmt)
        self.ast = ast

    def subscribe(self, state):
        WriteEvent.events.append(self)
        if not WriteEvent.subscribed:
            WriteEvent.subscribed = True
            state.inspect.b("mem_write", when=angr.BP_BEFORE, 
                            action=lambda state: Event.breakpoint(self, state))

    def get_event_condition(self, state):
        if self.scope.state_in_scope(state):
            return state.inspect.mem_write_address == self.ast.get_sym(state, True)
        else:
            return False

class CallEvent(Event):
    subscribed = False
    events = []

    def __init__(self, fn, scope, general_constraint, stmt):
        super().__init__(scope, general_constraint, stmt)
        self.fn = fn

    def subscribe(self, state):
        CallEvent.events.append(self)
        if not CallEvent.subscribed:
            CallEvent.subscribed = True
            state.inspect.b("call", when=angr.BP_BEFORE, 
                            action=lambda state: Event.breakpoint(self, state))

    def get_event_condition(self, state):
        if self.scope.state_in_scope(state):
            if self.fn == None:
                return True
            # print(str(state.inspect.function_address))
            return state.inspect.function_address == self.fn.rebased_addr
        else:
            return False

class ReturnEvent:
    subscribed = False
    events = []

    def subscribe(self, state):
        ReturnEvent.events.append(self)
        if not ReturnEvent.subscribed:
            ReturnEvent.subscribed = True
            state.inspect.b("return", when=angr.BP_BEFORE, 
                            action=lambda state: Event.breakpoint(self, state))

    def get_event_condition(self, state):
        return self.scope.state_in_scope(state)

class AlwaysEvent:
    subscribed = False
    events = []
    def subscribe(self, state):
        AlwaysEvent.events.append(self)
        if not AlwaysEvent.subscribed:
            AlwaysEvent.subscribed = True
            state.inspect.b("mem_write", when=angr.BP_AFTER, 
                            action=lambda state: Event.breakpoint(self, state))
            state.inspect.b("call", when=angr.BP_AFTER, 
                            action=lambda state: Event.breakpoint(self, state))
    
    def get_event_condition(self, state):
        return True
