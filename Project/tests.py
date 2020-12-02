from varparse import Scope, GlobalScope
from Operator import Type, ExprType
from AST import ASTNode
from Operator import Operator
from Event import *
from engine import Engine

import angr, claripy

import os

def write_test():
    os.system("gcc ../tests/simple_cond_write_cond.c -o ../test -O0 -g")

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
    evt = WriteEvent("secret", testscope, cond, "WRITE(secret) -> is_allowed == 1")
    
    return Engine(proj, [evt])

def write_next_test():
    os.system("gcc ../tests/next_definition.c -o ../test -O0 -g")

    proj = angr.Project("../test")
    testscope = GlobalScope(proj)

    # General condition
    var_name = "pUID"
    var_type = ExprType(Type.BV32, 1)
    var_scope = testscope
    var_node = ASTNode(Operator.VAR, [var_name, var_type, var_scope])
    deref_node = ASTNode(Operator.DEREF, [var_node])
    next_node = ASTNode(Operator.NEXT, [deref_node])
    cond = ASTNode(Operator.GE, [next_node, deref_node])
    print("General Contraint: " + cond.stringify())

    # Create the event
    evt = WriteEvent(deref_node, testscope, cond, "WRITE(*pUID) -> NEXT(*pUID) >= *pUID")

    return Engine(proj, [evt])

def arrays_test():
    os.system("gcc ../tests/arrays.c -o ../test -O0 -g")

    proj = angr.Project("../test")
    testscope = GlobalScope(proj)

    # General Condition
    arr_node = ASTNode(Operator.VAR, ["arr", ExprType(Type.BV32, 1), testscope])
    idx_node = ASTNode(Operator.VAR, ["idx", ExprType(Type.BV32, 0), testscope])
    two_node = ASTNode(Operator.LITERAL, [2, ExprType(Type.BV32, 0)])

    arr_index_two_node = ASTNode(Operator.INDEX, [arr_node, two_node])
    arr_index_idx_node = ASTNode(Operator.INDEX, [arr_node, idx_node])

    cond = ASTNode(Operator.LE, [arr_index_idx_node, arr_index_two_node])
    print("General Constraint: " + cond.stringify())

    evt = WriteEvent(arr_index_two_node, testscope, cond, "WRITE(arr[2]) -> arr[idx] < arr[2]")

    return Engine(proj, [evt])

# Prepare the project
arrays_test().run()
