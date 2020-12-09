"""
This file parses invariants from source code. Invariants will occur in the code with the following style of comments
// INVARIANT(var1, var2...) ACTION(var) -> expr
Global invariants can be assigned as long as there is a line in between all the invariants and any function
"""
from Grammar.invariantParser import invariantParser as InvariantParser
from Grammar.invariantLexer import invariantLexer as InvariantLexer
from antlr4 import InputStream, CommonTokenStream, ParseTreeWalker, ParseTreeListener, ParserRuleContext
from AST import ASTNode
from Operator import Operator, Type, ExprType
from varparse import GlobalScope, FunctionScope
import Event as Event
import re


class Invariant:
    """
    Invariants have an associated scope, event, variables, and expression
    Scope is stored as an object of the varparse.Scope class
    We also store the string representation of the invariant
    Variables are stored in the following map structure
        { variable_name: (variable_type, variable_scope) }
    """

    def __init__(self, scope, variables, str_expr, project):
        self.scope = scope
        self.vars = variables
        self.str_expr = str_expr
        self.ast = None
        self.event = None
        self.project = project

    def parse_expr(self):
        """
        This function parses the invariant and sets the event and AST
        :return: NONE
        """
        assert ("->" in self.str_expr)
        parts = self.str_expr.split('->')
        # Create the parse tree
        stream = InputStream(parts[1])
        lex_stream = InvariantLexer(stream)
        parser = InvariantParser(CommonTokenStream(lex_stream))
        tree = parser.expr(0)
        # Parse the tree to create AST
        self.ast = parse_tree(tree, self.vars)
        con_reg = '(READ|WRITE|CALL|RETURN|ALWAYS)\((.*)\)'
        con_match = re.match(con_reg, parts[0].strip())
        assert(con_match is not None)
        con_expr = con_match.group(2)
        event = con_match.group(1)
        if event == 'READ' or event == 'WRITE':
            con_stream = InputStream(con_expr)
            con_lex_stream = InvariantLexer(con_stream)
            con_parser = InvariantParser(CommonTokenStream(con_lex_stream))
            con_tree = con_parser.expr(0)
            # Parse the tree to create AST
            con_ast = parse_tree(con_tree, self.vars)
            if event == 'READ':
                self.event = Event.ReadEvent(con_ast, self.scope, self.ast, self.str_expr)
            else:
                self.event = Event.WriteEvent(con_ast, self.scope, self.ast, self.str_expr)
        elif event == "CALL":
            self.event = Event.CallEvent(self.project.loader.find_symbol(con_expr).rebased_addr, self.scope, self.ast, self.str_expr)
        elif event == "RETURN":
            self.event = Event.ReturnEvent(self.project.loader.find_symbol(con_expr).rebased_addr, self.scope, self.ast, self.str_expr)
        elif event == "ALWAYS":
            self.event = Event.AlwaysEvent(self.scope, self.ast, self.str_expr)


def get_type_from_str(type):
    expr_type = None
    bool_reg = "bool(\**)"
    bool_match = re.match(bool_reg, type)
    num_reg = "(u?)num(8|16|32|64)(\**)"
    num_match = re.match(num_reg, type)
    if bool_match is not None:
        expr_type = ExprType(Type.BOOL, pointers=len(bool_match.group(1)))
    elif num_match is not None:
        signed = len(num_match.group(1)) == 0
        size = int(num_match.group(2))
        pointers = len(num_match.group(3))
        if size == 8:
            expr_type = ExprType(Type.BV8, pointers=pointers, signed=signed)
        elif size == 16:
            expr_type = ExprType(Type.BV16, pointers=pointers, signed=signed)
        elif size == 32:
            expr_type = ExprType(Type.BV32, pointers=pointers, signed=signed)
        else:
            expr_type = ExprType(Type.BV64, pointers=pointers, signed=signed)
    else:
        # TODO: Handle errors better
        assert False
    return expr_type


def parse_tree(tree, variables):
    if isinstance(tree, InvariantParser.FunAppExprContext):
        func_name = tree.getChild(0).getChild(0).symbol.text
        assert(func_name == "NEXT" or func_name == "RETURN_VAL")
        if func_name == "NEXT":
            operand_one = parse_tree(tree.getChild(2), variables)
            return ASTNode(Operator.NEXT, [operand_one])
        else:
            operand_one = get_type_from_str(tree.getChild(2).getChild(0).symbol.text)
            return ASTNode(Operator.RETN, [operand_one])
    elif isinstance(tree, InvariantParser.IndexExprContext):
        operand_one = parse_tree(tree.getChild(0), variables)
        operand_two = parse_tree(tree.getChild(2), variables)
        return ASTNode(Operator.INDEX, [operand_one, operand_two])
    op = int((tree.getChildCount() - 1) / 2)
    token = tree.getChild(op)
    if token is None:
        if re.fullmatch('[0-9]+', tree.symbol.text):
            return ASTNode(Operator.LITERAL, [tree.symbol.text, ExprType(Type.BV64, pointers=0, signed=int(tree.symbol.text) <= 2 ** 63 - 1)])
        else:
            if tree.symbol.text == "true" or tree.symbol.text == "false":
                return ASTNode(Operator.LITERAL, [token.symbol.text == "true", ExprType(Type.BOOL, 0)])
            assert(tree.symbol.text in variables)
            return ASTNode(Operator.VAR,
                           [tree.symbol.text, variables[tree.symbol.text][0], variables[tree.symbol.text][1]])
    if token.symbol.text == "+":
        operand_one = parse_tree(tree.getChild(0), variables)
        operand_two = parse_tree(tree.getChild(2), variables)
        operator = Operator.PLUS
        return ASTNode(operator, [operand_one, operand_two])
    elif token.symbol.text == "-":
        if tree.getChildCount == 3:
            operand_one = parse_tree(tree.getChild(0), variables)
            operand_two = parse_tree(tree.getChild(2), variables)
            operator = Operator.MINUS
            return ASTNode(operator, [operand_one, operand_two])
        else:
            operand_one = ASTNode(Operator.LITERAL, ['0', ExprType(Type.BV64, 0)])
            operand_two = parse_tree(tree.getChild(1), variables)
            operator = Operator.MINUS
            return ASTNode(operator, [operand_one, operand_two])
    elif token.symbol.text == '*':
        if tree.getChildCount() == 3:
            operand_one = parse_tree(tree.getChild(0), variables)
            operand_two = parse_tree(tree.getChild(2), variables)
            operator = Operator.TIMES
            return ASTNode(operator, [operand_one, operand_two])
        else:
            operand_one = parse_tree(tree.getChild(1), variables)
            operator = Operator.DEREF
            return ASTNode(operator, [operand_one])
    elif token.symbol.text == '/':
        operand_one = parse_tree(tree.getChild(0), variables)
        operand_two = parse_tree(tree.getChild(2), variables)
        operator = Operator.DIVIDE
        return ASTNode(operator, [operand_one, operand_two])
    elif token.symbol.text == '&':
        operand_one = parse_tree(tree.getChild(0), variables)
        operand_two = parse_tree(tree.getChild(2), variables)
        operator = Operator.BAND
        return ASTNode(operator, [operand_one, operand_two])
    elif token.symbol.text == '|':
        operand_one = parse_tree(tree.getChild(0), variables)
        operand_two = parse_tree(tree.getChild(2), variables)
        operator = Operator.BOR
        return ASTNode(operator, [operand_one, operand_two])
    elif token.symbol.text == '^':
        operand_one = parse_tree(tree.getChild(0), variables)
        operand_two = parse_tree(tree.getChild(2), variables)
        operator = Operator.BXOR
        return ASTNode(operator, [operand_one, operand_two])
    elif token.symbol.text == '==':
        operand_one = parse_tree(tree.getChild(0), variables)
        operand_two = parse_tree(tree.getChild(2), variables)
        operator = Operator.EQ
        return ASTNode(operator, [operand_one, operand_two])
    elif token.symbol.text == '!=':
        operand_one = parse_tree(tree.getChild(0), variables)
        operand_two = parse_tree(tree.getChild(2), variables)
        operator = Operator.NEQ
        return ASTNode(operator, [operand_one, operand_two])
    elif token.symbol.text == '>':
        operand_one = parse_tree(tree.getChild(0), variables)
        operand_two = parse_tree(tree.getChild(2), variables)
        operator = Operator.GT
        return ASTNode(operator, [operand_one, operand_two])
    elif token.symbol.text == '<':
        operand_one = parse_tree(tree.getChild(0), variables)
        operand_two = parse_tree(tree.getChild(2), variables)
        operator = Operator.LT
        return ASTNode(operator, [operand_one, operand_two])
    elif token.symbol.text == '>=':
        operand_one = parse_tree(tree.getChild(0), variables)
        operand_two = parse_tree(tree.getChild(2), variables)
        operator = Operator.GE
        return ASTNode(operator, [operand_one, operand_two])
    elif token.symbol.text == '<=':
        operand_one = parse_tree(tree.getChild(0), variables)
        operand_two = parse_tree(tree.getChild(2), variables)
        operator = Operator.LE
        return ASTNode(operator, [operand_one, operand_two])
    elif token.symbol.text == '&&':
        operand_one = parse_tree(tree.getChild(0), variables)
        operand_two = parse_tree(tree.getChild(2), variables)
        operator = Operator.LAND
        return ASTNode(operator, [operand_one, operand_two])
    elif token.symbol.text == '||':
        operand_one = parse_tree(tree.getChild(0), variables)
        operand_two = parse_tree(tree.getChild(2), variables)
        operator = Operator.LOR
        return ASTNode(operator, [operand_one, operand_two])
    elif token.symbol.text == '!':
        operand_one = parse_tree(tree.getChild(1), variables)
        operator = Operator.LNOT
        return ASTNode(operator, [operand_one])
    elif token.symbol.text == '~':
        operand_one = parse_tree(tree.getChild(1), variables)
        operator = Operator.BNOT
        return ASTNode(operator, [operand_one])
    elif re.fullmatch('[0-9]+', token.symbol.text):
        return ASTNode(Operator.LITERAL,
                       [token.symbol.text, ExprType(Type.BV64, pointers=0, signed=int(token.symbol.text) <= 2 ** 63 - 1)])
    else:
        if token.symbol.text == "true" or token.symbol.text == "false":
            return ASTNode(Operator.LITERAL, [token.symbol.text == "true", ExprType(Type.BOOL, 0)])
        assert (token.symbol.text in variables)
        return ASTNode(Operator.VAR,
                       [token.symbol.text, variables[token.symbol.text][0], variables[token.symbol.text][1]])


def parse_invariants(file_name, project):
    with open(file_name, 'r') as f:
        x = 0
        lines = f.readlines()
        invariants = []
        inv_reg = '^// ?INVARIANT\\(((([^)]*),)*([^)]*)?)\\):(.*)'
        func_reg = '[A-z]+ +([A-z_]+)(\(| )'
        for line in lines:
            line = line.strip()
            match = re.match(inv_reg, line)
            variables = {}
            if match is not None:
                args = match.group(1).split(',')
                inv_scope = GlobalScope(project)
                for y in range (x, len(lines)):
                    l = lines[y].strip()
                    if re.match(inv_reg, l):
                        continue
                    func_match = re.match(func_reg, l)
                    if func_match is not None:
                        inv_scope = FunctionScope(project, func_match.group(1))
                        break
                    else:
                        break

                # Create variables
                for var in args:
                    var = var.strip()
                    s = var.split(' ')[0]
                    type = var.split(' ')[1]
                    var = var.split(' ')[2]
                    scope = GlobalScope(project)
                    if s == 'local':
                        scope = inv_scope
                    expr_type = get_type_from_str(type)
                    variables[var] = (expr_type, scope)
                expression = match.group(5)
                invariant = Invariant(inv_scope, variables, expression, project)
                invariant.parse_expr()
                invariants.append(invariant.event)
            x += 1
    return invariants


if __name__ == "__main__":
    parse_invariants("../tests/query_direct.c", None)