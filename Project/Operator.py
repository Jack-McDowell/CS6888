from enum import Enum
import angr
import eval_variable

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
        assert(self.pointers > 0)
        assert(not self.t == Type.BOOL)

        if self.pointers > 1:
            return 64
        elif self.pointers == 1:
            return 4 * (2 ** self.t)

def bigger_int(type1, type2):
    assert(type1.pointers == 0 and not type1.t == Type.BOOL)
    assert(type2.pointers == 0 and not type2.t == Type.BOOL)

    return type1 if type1.t > type2 else type2

def deref_type(type1):
    assert(type1.pointers > 0)

    return ExprType(type1.t, type1.pointers - 1)

def compute_next(state, ast):
    raise NotImplementedError()

class Operator:
    def __init__(self, output, angrify, typer, operands):
        self.output = output
        self.angrify = angrify
        self.typer = typer
        self.operands = operands

    PLUS = Operator(
        lambda operands: "(" + operands[0] + " + " + operands[1] + ")",
        lambda operands, state: operands[0].get_sym(state) + operands[1].get_sym(state),
        lambda operands: bigger_int(operands[0], operands[1]),
        2)

    MINUS = Operator(
        lambda operands: "(" + operands[0] + " - " + operands[1] + ")",
        lambda operands, state: operands[0].get_sym(state) - operands[1].get_sym(state),
        lambda operands: bigger_int(operands[0], operands[1]),
        2)

    TIMES = Operator(
        lambda operands: "(" + operands[0] + " * " + operands[1] + ")",
        lambda operands, state: operands[0].get_sym(state) * operands[1].get_sym(state),
        lambda operands: bigger_int(operands[0], operands[1]),
        2)

    DIVIDE = Operator(
        lambda operands: "(" + operands[0] + " / " + operands[1] + ")",
        lambda operands, state: operands[0].get_sym(state) / operands[1].get_sym(state),
        lambda operands: bigger_int(operands[0], operands[1]),
        2)

    EXP = Operator(
        lambda operands: "(" + operands[0] + " ** " + operands[1] + ")",
        lambda operands, state: operands[0].get_sym(state) ** operands[1].get_sym(state),
        lambda operands: bigger_int(operands[0], operands[1]),
        2)

    BAND = Operator(
        lambda operands: "(" + operands[0] + " & " + operands[1] + ")",
        lambda operands, state: operands[0].get_sym(state) & operands[1].get_sym(state),
        lambda operands: bigger_int(operands[0], operands[1]),
        2)

    BOR = Operator(
        lambda operands: "(" + operands[0] + " | " + operands[1] + ")",
        lambda operands, state: operands[0].get_sym(state) | operands[1].get_sym(state),
        lambda operands: bigger_int(operands[0], operands[1]),
        2)

    BXOR = Operator(
        lambda operands: "(" + operands[0] + " ^ " + operands[1] + ")",
        lambda operands, state: operands[0].get_sym(state) | operands[1].get_sym(state),
        lambda operands: bigger_int(operands[0], operands[1]),
        2)

    EQ = Operator(
        lambda operands: "(" + operands[0] + " == " + operands[1] + ")",
        lambda operands, state: operands[0].get_sym(state) == operands[1].get_sym(state),
        lambda operands: Type.BOOL,
        2)

    NEQ = Operator(
        lambda operands: "(" + operands[0] + " != " + operands[1] + ")",
        lambda operands, state: operands[0].get_sym(state) != operands[1].get_sym(state),
        lambda operands: Type.BOOL,
        2)

    GT = Operator(
        lambda operands: "(" + operands[0] + " > " + operands[1] + ")",
        lambda operands, state: operands[0].get_sym(state) > operands[1].get_sym(state),
        lambda operands: Type.BOOL,
        2)

    LT = Operator(
        lambda operands: "(" + operands[0] + " < " + operands[1] + ")",
        lambda operands, state: operands[0].get_sym(state) < operands[1].get_sym(state),
        lambda operands: Type.BOOL,
        2)

    GE = Operator(
        lambda operands: "(" + operands[0] + " >= " + operands[1] + ")",
        lambda operands, state: operands[0].get_sym(state) >= operands[1].get_sym(state),
        lambda operands: Type.BOOL,
        2)

    LE = Operator(
        lambda operands: "(" + operands[0] + " <= " + operands[1] + ")",
        lambda operands, state: operands[0].get_sym(state) <= operands[1].get_sym(state),
        lambda operands: Type.BOOL,
        2)

    LOR = Operator(
        lambda operands: "(" + operands[0] + " || " + operands[1] + ")",
        lambda operands, state: operands[0].get_sym(state) or operands[1].get_sym(state),
        lambda operands: Type.BOOL,
        2)

    LAND = Operator(
        lambda operands: "(" + operands[0] + " && " + operands[1] + ")",
        lambda operands, state: operands[0].get_sym(state) and operands[1].get_sym(state),
        lambda operands: Type.BOOL,
        2)

    DEREF = Operator(
        lambda operands: "*(" + operands[0] + ")",
        lambda operands, state: 
            state.memory.load(operands[0].get_sym(state), 
                              operands[0].get_type().get_pointed_size(),
                              disable_actions=True, inspect=False)
        lambda operands: deref_type(operands[0]),
        1)

    INDEX = Operator(
        lambda operands: "(" + operands[0] + ")[" + operands[1] + "]",
        lambda operands, state: 
            state.memory.load(operands[0].get_sym(state) + operands[0].get_type().get_pointed_size() * operands[1].get_sym(state), 
                              operands[0].get_type().get_pointed_size(),
                              disable_actions=True, inspect=False)
        lambda operands: deref_type(operands[0]),
        2)

    VAR = Operator(
        lambda operands: operands[0],
        eval_variable
        lambda operands: operands[1],
        3)
    
    NEXT = Operator(
        lambda operands: "NEXT(" + operands[0] + ")",
        lambda operands, state: compute_next(state, operands[0])
        lambda operands: operands[0],
        1)

    RETN = Operator(
        lambda operands: "RETURN_VAL()",
        lambda operands, state: state.regs.rax
        lambda operands: operands[0],
        1)