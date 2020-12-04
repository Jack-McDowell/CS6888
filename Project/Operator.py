from enum import Enum
import angr, archinfo, claripy
from varparse import eval_variable

class Type(Enum):
    BOOL = 0
    BV8 = 1
    BV16 = 2
    BV32 = 3
    BV64 = 4

class ExprType:
    def __init__(self, t, pointers=0, signed=False):
        self.t = t
        self.pointers = pointers
        self.signed = signed

    def get_pointed_size(self):
        assert(not self.t == Type.BOOL)

        if self.pointers > 1:
            return 8
        else:
            return 2 ** (self.t.value - 1)

def combine_int(type1, type2):
    assert(type1.pointers == 0 and not type1.t == Type.BOOL)
    assert(type2.pointers == 0 and not type2.t == Type.BOOL)

    return ExprType(type1.t if type1.t.value > type2.t.value else type2.t, signed=type1.signed)

def deref_type(type1):
    assert(type1.pointers > 0)

    return ExprType(type1.t, type1.pointers - 1, type1.signed)

def perform_deref(state, ptr, lval):
    if lval:
        return ptr
    else:
        return state.memory.load(ptr, operands[0].get_type().get_pointed_size(),
                                 disable_actions=True, inspect=False, 
                                 endness=archinfo.Endness.LE),

def int_unif(op1, op2, state):
    v1 = op1.get_sym(state)
    v2 = op2.get_sym(state)

    t1 = op1.get_type()
    t2 = op2.get_type()

    if t1.t != t2.t:
        assert(t1.pointers == 0 and not t1.t == Type.BOOL)
        assert(t2.pointers == 0 and not t2.t == Type.BOOL)

        bc1 = 2 ** (t1.t.value + 2)
        bc2 = 2 ** (t2.t.value + 2)

        if bc1 > bc2 and not type(v2) is int:
            v2 = v2.sign_extend(bc1 - bc2) if t2.signed else v2.zero_extend(bc1 - bc2)
        elif bc2 > bc1 and not type(v1) is int: 
            v1 = v1.sign_extend(bc2 - bc1) if t1.signed else v1.zero_extend(bc2 = bc1)

    return (v1, v2, t1, t2)

def int_op(op1, op2, state, op):
    v1, v2, t1, t2 = int_unif(op1, op2, state)
    
    return op(v1, v2)

def signed_eq(op1, op2, state):
    v1, v2, t1, t2 = int_unif(op1, op2, state)

    if t1.signed == t2.signed:
        return v1 == v2

    return claripy.If(claripy.SLT(v1 if t1.signed else v2, 0), False, v1 == v2)

def signed_lt(op1, op2, state):
    v1, v2, t1, t2 = int_unif(op1, op2, state)

    if t1.signed == t2.signed:
        return claripy.SLT(v1, v2) if t1.signed else claripy.ULT(v1, v2)

    return claripy.If(claripy.SLT(v1 if t1.signed else v2, 0), t1.signed, v1 < v2)

def signed_gt(op1, op2, state):
    v1, v2, t1, t2 = int_unif(op1, op2, state)

    if t1.signed == t2.signed:
        return claripy.SGT(v1, v2) if t1.signed else claripy.UGT(v1, v2)

    return claripy.If(claripy.SLT(v1 if t1.signed else v2, 0), not t1.signed, v1 > v2)

def perform_access(state, struct, offset, lval):
    array_ptr = not operands[0].get_type().pointers == 0
    ptr = operands[0].get_sym(state, not array_ptr) + operands[0] + offset
    return perform_deref(state, ptr, lval)

def perform_index(state, arr_node, idx_node, lval):
    offset = operands[0].get_type().get_pointed_size() * operands[1].get_sym(state)
    return perform_access(state, arr_node, offset, lval)

class Operator:
    def __init__(self, output, angrify, typer, operands):
        self.output = output
        self.angrify = angrify
        self.typer = typer
        self.operands = operands

    PLUS = None
    MINUS = None
    MUL = None
    BAND = None
    BOR = None
    BXOR = None
    BNOT = None
    EQ = None
    NEQ = None
    GT = None
    LT = None
    GE = None
    LE = None
    LOR = None
    LAND = None
    LNOT = None
    DEREF = None
    INDEX = None
    ACCESS = None
    VAR = None
    NEXT = None
    LITERAL = None
    RETN = None

Operator.PLUS = Operator(
    lambda operands: "(" + operands[0] + " + " + operands[1] + ")",
    lambda operands, state, lval: 
        (int_op(operands[0], operands[1], state, lambda a, b: a + b), False),
    lambda operands, lval: combine_int(operands[0], operands[1]),
    2)

Operator.MINUS = Operator(
    lambda operands: "(" + operands[0] + " - " + operands[1] + ")",
    lambda operands, state, lval: 
        (int_op(operands[0], operands[1], state, lambda a, b: a - b), False),
    lambda operands, lval: combine_int(operands[0], operands[1]),
    2)

Operator.MUL = Operator(
    lambda operands: "(" + operands[0] + " * " + operands[1] + ")",
    lambda operands, state, lval: 
        (int_op(operands[0], operands[1], state, lambda a, b: a * b), False),
    lambda operands, lval: combine_int(operands[0], operands[1]),
    2)

Operator.BAND = Operator(
    lambda operands: "(" + operands[0] + " & " + operands[1] + ")",
    lambda operands, state, lval: 
        (int_op(operands[0], operands[1], state, lambda a, b: a & b), False),
    lambda operands, lval: combine_int(operands[0], operands[1]),
    2)

Operator.BOR = Operator(
    lambda operands: "(" + operands[0] + " | " + operands[1] + ")",
    lambda operands, state, lval: 
        (int_op(operands[0], operands[1], state, lambda a, b: a | b), False),
    lambda operands, lval: combine_int(operands[0], operands[1]),
    2)

Operator.BXOR = Operator(
    lambda operands: "(" + operands[0] + " ^ " + operands[1] + ")",
    lambda operands, state, lval: 
        (int_op(operands[0], operands[1], state, lambda a, b: a ^ b), False),
    lambda operands, lval: combine_int(operands[0], operands[1]),
    2)

Operator.BNOT = Operator(
    lambda operands: "~" + operands[0],
    lambda operands, state, lval: 
        (~(operands[0].get_sym(state)), False),
    lambda operands, lval: operands[0],
    2)

Operator.EQ = Operator(
    lambda operands: "(" + operands[0] + " == " + operands[1] + ")",
    lambda operands, state, lval: (signed_eq(operands[0], operands[1], state), False),
    lambda operands, lval: Type.BOOL,
    2)

Operator.NEQ = Operator(
    lambda operands: "(" + operands[0] + " != " + operands[1] + ")",
    lambda operands, state, lval: (claripy.Not(signed_eq(operands[0], operands[1], state)), False),
    lambda operands, lval: Type.BOOL,
    2)

Operator.GT = Operator(
    lambda operands: "(" + operands[0] + " > " + operands[1] + ")",
    lambda operands, state, lval: (signed_gt(operands[0], operands[1], state), False),
    lambda operands, lval: Type.BOOL,
    2)

Operator.LT = Operator(
    lambda operands: "(" + operands[0] + " < " + operands[1] + ")",
    lambda operands, state, lval: (signed_lt(operands[0], operands[1], state), False),
    lambda operands, lval: Type.BOOL,
    2)

Operator.GE = Operator(
    lambda operands: "(" + operands[0] + " >= " + operands[1] + ")",
    lambda operands, state, lval: (claripy.Not(signed_lt(operands[0], operands[1]), state), False),
    lambda operands, lval: Type.BOOL,
    2)

Operator.LE = Operator(
    lambda operands: "(" + operands[0] + " <= " + operands[1] + ")",
    lambda operands, state, lval: (claripy.Not(signed_gt(operands[0], operands[1]), state), False),
    lambda operands, lval: Type.BOOL,
    2)

Operator.LOR = Operator(
    lambda operands: "(" + operands[0] + " || " + operands[1] + ")",
    lambda operands, state, lval: 
        (claripy.Or(operands[0].get_sym(state), operands[1].get_sym(state)), False),
    lambda operands, lval: Type.BOOL,
    2)

Operator.LAND = Operator(
    lambda operands: "(" + operands[0] + " && " + operands[1] + ")",
    lambda operands, state, lval: 
        (claripy.And(operands[0].get_sym(state), operands[1].get_sym(state)), False),
    lambda operands, lval: Type.BOOL,
    2)

Operator.LNOT = Operator(
    lambda operands: "!" + operands[0],
    lambda operands, state, lval: (claripy.Not(operands[0].get_sym(state)), False),
    lambda operands, lval: Type.BOOL,
    2)

Operator.DEREF = Operator(
    lambda operands: "*" + operands[0],
    lambda operands, state, lval: 
        (perform_deref(state, operands[0].get_sym(state), lval), True),
    lambda operands, lval: operands[0] if lval else deref_type(operands[0]),
    1)

Operator.INDEX = Operator(
    lambda operands: operands[0] + "[" + operands[1] + "]",
    lambda operands, state, lval: (perform_index(state, operands[0], operands[1], lval), True),
    lambda operands, lval: operands[0] if lval else deref_type(operands[0]),
    2)

Operator.ACCESS = Operator(
    lambda operands: "*(???*)((char*) " + operands[0] + " + " operands[1] + ")",
    lambda operands, state, lval: (perform_access(state, operands[0], operands[1], lval), True),
    lambda operands, lval: operands[2] if lval else deref_type(operands[2]),
    3)

Operator.VAR = Operator(
    lambda operands: operands[0],
    lambda operands, state, lval: (eval_variable(operands, state, lval), True),
    lambda operands, lval: 
        operands[1] if not lval else ExprType(operands[1].t, operands[1].pointers + 1, operands[1].signed),
    3)

Operator.LITERAL = Operator(
    lambda operands: operands[0],
    lambda operands, state, lval: (operands[0], False),
    lambda operands, lval: operands[1],
    2)

Operator.NEXT = Operator(
    lambda operands: "NEXT(" + operands[0] + ")",
    lambda operands, state, lval: (state.inspect.mem_write_expr, True),
    lambda operands, lval: operands[0],
    1)

Operator.RETN = Operator(
    lambda operands: "RETURN_VAL()",
    lambda operands, state, lval: (state.regs.rax, True),
    lambda operands, lval: operands[0],
    1)
