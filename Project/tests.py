from varparse import Scope, GlobalScope, FunctionScope
from Operator import Type, ExprType
from AST import ASTNode
from Operator import Operator
from Event import *
from engine import Engine
from invparse import parse_invariants
from elfparse import *

import angr, claripy

import os

def write_test():
    os.system("gcc ../tests/simple_cond_write_cond.c -o ../test -O0 -g")

    proj = angr.Project("../test")
    testscope = GlobalScope(proj)

    # # Creating the general condition
    # var_name = "allowed"
    # var_type = ExprType(Type.BV8, 0)
    # var_scope = testscope
    # var_node = ASTNode(Operator.VAR, [var_name, var_type, var_scope])
    # literal_node = ASTNode(Operator.LITERAL, [1, ExprType(Type.BV8, 0)])
    # cond = ASTNode(Operator.EQ, [var_node, literal_node])
    # print("General Constraint: " + cond.stringify())
    #
    # # Creating the event
    # evt = WriteEvent("secret", testscope, cond, "WRITE(secret) -> is_allowed == 1")
    evts = parse_invariants("../tests/arrays.c", proj)

    return Engine(proj, evts)

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

    # # General Condition
    arr_node = ASTNode(Operator.VAR, ["arr", ExprType(Type.BV32, 0), testscope])
    idx_node = ASTNode(Operator.VAR, ["idx", ExprType(Type.BV32, 0), testscope])
    two_node = ASTNode(Operator.LITERAL, [2, ExprType(Type.BV32, 0)])

    arr_index_two_node = ASTNode(Operator.INDEX, [arr_node, two_node])
    arr_index_idx_node = ASTNode(Operator.INDEX, [arr_node, idx_node])
    next_node = ASTNode(Operator.NEXT, [arr_index_two_node])

    cond = ASTNode(Operator.LE, [arr_index_idx_node, next_node])
    print("General Constraint: " + cond.stringify())

    evt = WriteEvent(arr_index_two_node, testscope, cond, "WRITE(arr[2]) -> arr[idx] <= NEXT(arr[2])")

    return Engine(proj, [evt])

def calls_test():
    os.system("gcc ../tests/simple_cond_call_cond.c -o ../test -O0 -g")

    proj = angr.Project("../test")
    testscope = GlobalScope(proj)

    # General condition
    allowed = ASTNode(Operator.VAR, ["allowed", ExprType(Type.BV8, 0), testscope])
    one_node = ASTNode(Operator.LITERAL, [1, ExprType(Type.BV8, 0)])

    cond = ASTNode(Operator.EQ, [allowed, one_node])

    evt = CallEvent(proj.loader.find_symbol("special"), testscope, cond, "CALL(special) -> allowed == 1")

    return Engine(proj, [evt])

def return_test():
    os.system("gcc ../tests/return.c -o ../test -O0 -g")

    proj = angr.Project("../test")
    testscope = GlobalScope(proj)

    # General Condition
    retn_node = ASTNode(Operator.RETN, [ExprType(Type.BV32, 0)])
    val_node = ASTNode(Operator.VAR, ["val", ExprType(Type.BV32, 0), testscope])

    cond = ASTNode(Operator.GT, [retn_node, val_node])

    evt = ReturnEvent(proj.loader.find_symbol("main").rebased_addr, testscope, cond, "RETURN() -> RETURN_VAL() > val")

    return Engine(proj, [evt])


def locals_test():
    os.system("gcc ../tests/locals.c -o ../test -O0 -g")

    proj = angr.Project("../test")
    testscope = GlobalScope(proj)
    funcscope = FunctionScope(proj, "func")

    # General Condition
    local_node = ASTNode(Operator.VAR, ["local", ExprType(Type.BV32, signed=True), funcscope])
    arg_node = ASTNode(Operator.VAR, ["arg", ExprType(Type.BV32, signed=True), funcscope])
    next_node = ASTNode(Operator.NEXT, [local_node])

    cond = ASTNode(Operator.GT, [local_node, arg_node])

    evt = ReturnEvent(proj.loader.find_symbol("func").rebased_addr, funcscope, cond, "WRITE(local) -> NEXT(local) > arg")

    return Engine(proj, [evt])

def check(solver, stmt):
    if not solver.satisfiable(extra_constraints=[stmt]):
        print(stmt)

def operators_test():
    solver = claripy.Solver()

    sym_one      = claripy.BVS("one",      32); 
    sym_uone     = claripy.BVS("uone",     8 ); 
    sym_zero     = claripy.BVS("zero",     32); 
    sym_neg_one  = claripy.BVS("neg_one",  32); 
    sym_uint_max = claripy.BVS("uint_max", 32); 

    solver.add(sym_one      == 1            )
    solver.add(sym_uone     == 1            )
    solver.add(sym_zero     == 0            )
    solver.add(sym_neg_one  == -1           )
    solver.add(sym_uint_max == (2 ** 32) - 1)

    one_node      = ASTNode(Operator.LITERAL, [sym_one     , ExprType(Type.BV32, signed=True )])
    uone_node     = ASTNode(Operator.LITERAL, [sym_uone    , ExprType(Type.BV8,  signed=False)])
    zero_node     = ASTNode(Operator.LITERAL, [sym_zero    , ExprType(Type.BV32, signed=True )])
    neg_one_node  = ASTNode(Operator.LITERAL, [sym_neg_one , ExprType(Type.BV32, signed=True )])
    uint_max_node = ASTNode(Operator.LITERAL, [sym_uint_max, ExprType(Type.BV32, signed=False)])

    one_eq_zero_node = ASTNode(Operator.NEQ, [one_node, zero_node])
    check(solver, one_eq_zero_node.get_sym(None))

    neg_one_eq_uint_max_node = ASTNode(Operator.NEQ, [neg_one_node, uint_max_node])
    check(solver, neg_one_eq_uint_max_node.get_sym(None))

    uone_eq_one_node = ASTNode(Operator.EQ, [one_node, uone_node])
    check(solver, uone_eq_one_node.get_sym(None))

    sum_node = ASTNode(Operator.PLUS, [one_node, neg_one_node])
    sum_zero_node = ASTNode(Operator.EQ, [sum_node, zero_node])
    check(solver, sum_zero_node.get_sym(None))

    sub_node = ASTNode(Operator.MINUS, [zero_node, neg_one_node])
    sub_one_node = ASTNode(Operator.EQ, [sub_node, one_node])
    check(solver, sub_one_node.get_sym(None))

    mul_node = ASTNode(Operator.MUL, [neg_one_node, neg_one_node])
    mul_one_node = ASTNode(Operator.EQ, [mul_node, one_node])
    check(solver, mul_one_node.get_sym(None))

    xor_node = ASTNode(Operator.BXOR, [uint_max_node, neg_one_node])
    xor_zero_node = ASTNode(Operator.EQ, [xor_node, zero_node])
    check(solver, xor_zero_node.get_sym(None))


def test_all():
    files = [
        #"simple_read",
        #"simple_cond_read",
        #"simple_read_cond",
        #"simple_cond_read_cond",
        #"simple_cond_write_cond",
        #"simple_array_read",
        #"next_definition",
        #"locals",
        #"arrays",
        #"simple_cond_call_cond",
        "return"
    ]

    for f in files:
        os.system("gcc ../tests/" + f + ".c -o ../test -g -O0")
        print("Preparing test " + f)
        proj = angr.Project("../test")
        invs = parse_invariants("../tests/" + f + ".c", proj)
        for inv in invs:
            print("Invariant: " + inv.general_constraint.stringify())
        Engine(proj, invs).run()

    

# Prepare the project
test_all()
