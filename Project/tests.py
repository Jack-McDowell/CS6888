from varparse import Scope, GlobalScope
from Operator import Type, ExprType
from AST import ASTNode
from Operator import Operator
from Event import Event, ReadEvent
from engine import Engine

import angr, claripy

proj = angr.Project("../test")
testscope = GlobalScope(proj)

# Creating the general condition
var_name = "allowed"
var_type = ExprType(Type.BV8, 0)
var_scope = testscope
var_node = ASTNode(Operator.VAR, [var_name, var_type, var_scope])
literal_node = ASTNode(Operator.LITERAL, [1, ExprType(Type.BV8, 0)])
cond = ASTNode(Operator.EQ, [var_node, literal_node])
print("General Constraint: " + cond.stringify())

# Creating the event
evt = ReadEvent("secret", testscope, cond, "READ(secret) -> is_allowed == 1")

# Prepare the project
engine = Engine(proj, [evt])
engine.run()