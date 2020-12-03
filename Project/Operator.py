from enum import Enum
import angr, archinfo
from varparse import eval_variable

class Type(Enum):
    BOOL = 0
    BV8 = 1
    BV16 = 2
    BV32 = 3
    BV64 = 4

class ExprType:
    def __init__(self, t, pointers):
        self.t = t
        self.pointers = pointers

    def get_pointed_size(self):
        assert(not self.t == Type.BOOL)

        if self.pointers > 1:
            return 8
        else:
            return 2 ** (self.t.value - 1)

def bigger_int(type1, type2):
    assert(type1.pointers == 0 and not type1.t == Type.BOOL)
    assert(type2.pointers == 0 and not type2.t == Type.BOOL)

    return type1 if type1.t > type2 else type2

def deref_type(type1):
    assert(type1.pointers > 0)

    return ExprType(type1.t, type1.pointers - 1)

class Operator:
    def __init__(self, output, angrify, typer, operands):
        self.output = output
        self.angrify = angrify
        self.typer = typer
        self.operands = operands

    PLUS = None
    MINUS = None
    TIMES = None
    DIVIDE = None
    EXP = None
    BAND = None
    BOR = None
    BXOR = None
    EQ = None
    NEQ = None
    GT = None
    LT = None
    GE = None
    LE = None
    LOR = None
    LAND = None
    DEREF = None
    INDEX = None
    VAR = None
    NEXT = None
    LITERAL = None
    RETN = None

Operator.PLUS = Operator(
    lambda operands: "(" + operands[0] + " + " + operands[1] + ")",
    lambda operands, state, lval: operands[0].get_sym(state) + operands[1].get_sym(state),
    lambda operands, lval: bigger_int(operands[0], operands[1]),
    2)

Operator.MINUS = Operator(
    lambda operands: "(" + operands[0] + " - " + operands[1] + ")",
    lambda operands, state, lval: operands[0].get_sym(state) - operands[1].get_sym(state),
    lambda operands, lval: bigger_int(operands[0], operands[1]),
    2)

Operator.TIMES = Operator(
    lambda operands: "(" + operands[0] + " * " + operands[1] + ")",
    lambda operands, state, lval: operands[0].get_sym(state) * operands[1].get_sym(state),
    lambda operands, lval: bigger_int(operands[0], operands[1]),
    2)

Operator.DIVIDE = Operator(
    lambda operands: "(" + operands[0] + " / " + operands[1] + ")",
    lambda operands, state, lval: operands[0].get_sym(state) / operands[1].get_sym(state),
    lambda operands, lval: bigger_int(operands[0], operands[1]),
    2)

Operator.EXP = Operator(
    lambda operands: "(" + operands[0] + " ** " + operands[1] + ")",
    lambda operands, state, lval: operands[0].get_sym(state) ** operands[1].get_sym(state),
    lambda operands, lval: bigger_int(operands[0], operands[1]),
    2)

Operator.BAND = Operator(
    lambda operands: "(" + operands[0] + " & " + operands[1] + ")",
    lambda operands, state, lval: operands[0].get_sym(state) & operands[1].get_sym(state),
    lambda operands, lval: bigger_int(operands[0], operands[1]),
    2)

Operator.BOR = Operator(
    lambda operands: "(" + operands[0] + " | " + operands[1] + ")",
    lambda operands, state, lval: operands[0].get_sym(state) | operands[1].get_sym(state),
    lambda operands, lval: bigger_int(operands[0], operands[1]),
    2)

Operator.BXOR = Operator(
    lambda operands: "(" + operands[0] + " ^ " + operands[1] + ")",
    lambda operands, state, lval: operands[0].get_sym(state) | operands[1].get_sym(state),
    lambda operands, lval: bigger_int(operands[0], operands[1]),
    2)

Operator.EQ = Operator(
    lambda operands: "(" + operands[0] + " == " + operands[1] + ")",
    lambda operands, state, lval: operands[0].get_sym(state) == operands[1].get_sym(state),
    lambda operands, lval: Type.BOOL,
    2)

Operator.NEQ = Operator(
    lambda operands: "(" + operands[0] + " != " + operands[1] + ")",
    lambda operands, state, lval: operands[0].get_sym(state) != operands[1].get_sym(state),
    lambda operands, lval: Type.BOOL,
    2)

Operator.GT = Operator(
    lambda operands: "(" + operands[0] + " > " + operands[1] + ")",
    lambda operands, state, lval: operands[0].get_sym(state) > operands[1].get_sym(state),
    lambda operands, lval: Type.BOOL,
    2)

Operator.LT = Operator(
    lambda operands: "(" + operands[0] + " < " + operands[1] + ")",
    lambda operands, state, lval: operands[0].get_sym(state) < operands[1].get_sym(state),
    lambda operands, lval: Type.BOOL,
    2)

Operator.GE = Operator(
    lambda operands: "(" + operands[0] + " >= " + operands[1] + ")",
    lambda operands, state, lval: operands[0].get_sym(state) >= operands[1].get_sym(state),
    lambda operands, lval: Type.BOOL,
    2)

Operator.LE = Operator(
    lambda operands: "(" + operands[0] + " <= " + operands[1] + ")",
    lambda operands, state, lval: operands[0].get_sym(state) <= operands[1].get_sym(state),
    lambda operands, lval: Type.BOOL,
    2)

Operator.LOR = Operator(
    lambda operands: "(" + operands[0] + " || " + operands[1] + ")",
    lambda operands, state, lval: operands[0].get_sym(state) or operands[1].get_sym(state),
    lambda operands, lval: Type.BOOL,
    2)

Operator.LAND = Operator(
    lambda operands: "(" + operands[0] + " && " + operands[1] + ")",
    lambda operands, state, lval: operands[0].get_sym(state) and operands[1].get_sym(state),
    lambda operands, lval: Type.BOOL,
    2)

Operator.DEREF = Operator(
    lambda operands: "*" + operands[0],
    lambda operands, state, lval: operands[0].get_sym(state) if lval else
        state.memory.load(operands[0].get_sym(state), 
                          operands[0].get_type().get_pointed_size(),
                          disable_actions=True, inspect=False, endness=archinfo.Endness.LE),
    lambda operands, lval: operands[0] if lval else deref_type(operands[0]),
    1)

Operator.INDEX = Operator(
    lambda operands: operands[0] + "[" + operands[1] + "]",
    lambda operands, state, lval: 
        operands[0].get_sym(state, operands[0].get_type().pointers == 0) + operands[0].get_type().get_pointed_size() * operands[1].get_sym(state) if lval else
        state.memory.load(operands[0].get_sym(state, operands[0].get_type().pointers == 0) + operands[0].get_type().get_pointed_size() * operands[1].get_sym(state), 
                            operands[0].get_type().get_pointed_size(),
                            disable_actions=True, inspect=False, endness=archinfo.Endness.LE),
    lambda operands, lval: operands[0] if lval else deref_type(operands[0]),
    2)

Operator.VAR = Operator(
    lambda operands: operands[0],
    lambda operands, state, lval: eval_variable(operands, state, lval),
    lambda operands, lval: operands[1] if not lval else ExprType(operands[1].t, operands[1].pointers + 1),
    3)

Operator.LITERAL = Operator(
    lambda operands: operands[0],
    lambda operands, state, lval: operands[0],
    lambda operands, lval: operands[1],
    2)

Operator.NEXT = Operator(
    lambda operands: "NEXT(" + operands[0] + ")",
    lambda operands, state, lval: state.inspect.mem_write_expr,
    lambda operands, lval: operands[0],
    1)

Operator.RETN = Operator(
    lambda operands: "RETURN_VAL()",
    lambda operands, state, lval: state.regs.rax,
    lambda operands, lval: operands[0],
    1)
