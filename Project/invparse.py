from varparse import Scope
"""
This file parses invariants from source code. Invariants will occur in the code with the following style of comments
// INVARIANT(var1, var2...) ACTION(var) -> expr
Global invariants can be assigned in a section bracketed by
// GLOBAL INVARIANTS
global invariants go here
// END GLOBAL INVARIANTS
"""
class Invariant:
    """
    Invariants have an associated scope, event, variables, and expression
    Scope is stored as an object of the varparse.Scope class
    We also store the string representation of the invariant
    """
    def __init__(self, scope: Scope, vars, str_expr):
        self.scope = scope
        self.vars = vars
        self.str_expr = str_expr