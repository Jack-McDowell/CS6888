import Scope, GlobalScope
import Type, ExprType
import ASTNode
import Operator
import Event, ReadEvent

import angr

proj = angr.Project("../test")
testscope = GlobalScope(proj)

# Creating the general condition
var_name = "is_allowed"
var_type = ExprType(Type.BV8, 0)
var_scope = testscope
var_node = ASTNode(Operator.VAR, [var_name, var_type, var_scope])
literal_node = ASTNode(Operator.LITERAL, [1, ExprType(Type.BV8, 0)])
cond = ASTNode(Operator.EQ, [var_node, literal_node])
print("General Constraint: " + cond.stringify())

# Creating the event
evt = ReadEvent("secret", testscope, cond, "READ(secret) -> is_allowed == 1")

# Prepare the project
inp = claripy.BVS("input", 128)
state = binary.factory.full_init_state(argc=2, args=["test", inp])
evt.subscribe(state)
simulation = project.factory.simgr(state)
simulation.explore()