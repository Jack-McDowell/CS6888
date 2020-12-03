"""
This file parses invariants from source code. Invariants will occur in the code with the following style of comments
// INVARIANT(var1, var2...) ACTION(var) -> expr
Global invariants can be assigned in a section bracketed by
// GLOBAL INVARIANTS
global invariants go here
// END GLOBAL INVARIANTS
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

    def __init__(self, scope, variables, str_expr):
        self.scope = scope
        self.vars = variables
        self.str_expr = str_expr
        self.ast = None
        self.event = None

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
            self.event = Event.CallEvent(con_expr, self.scope, self.ast, self.str_expr)
        #TODO: Handle return and always



def parse_tree(tree, variables):
    # TODO: Handle NEXT, RETURN, and INDEX
    op = int((tree.getChildCount() - 1) / 2)
    token = tree.getChild(op)
    if token is None:
        if re.fullmatch('[0-9]+', tree.symbol.text):
            return ASTNode(Operator.LITERAL, [tree.symbol.text, ExprType(Type.BV64, 0)])
        else:
            return ASTNode(Operator.VAR, [tree.symbol.text, None, None])
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
    elif token.symbol.text == '**':
        operand_one = parse_tree(tree.getChild(0), variables)
        operand_two = parse_tree(tree.getChild(2), variables)
        operator = Operator.EXP
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
    elif re.fullmatch('[0-9]+', token.symbol.text):
        return ASTNode(Operator.LITERAL, [token.symbol.text, ExprType(Type.BV64, 0)])
    else:
        if token.symbol.text == "true" or token.symbol.text == "false":
            return ASTNode(Operator.LITERAL, [token.symbol.text == "true", ExprType(Type.BOOL, 0)])
        assert (token.symbol.text in variables)
        return ASTNode(Operator.VAR,
                       [token.symbol.text, variables[token.symbol.text][0], variables[token.symbol.text][1]])


def parse_invariants(file_name, project):
    with open(file_name, 'r') as f:
        lines = f.readlines()
        invariants = []
        inv_reg = '^// ?INVARIANT\\(((([^)]*),)*([^)]*)?)\\):(.*)'
        for line in lines:
            line = line.strip()
            match = re.match(inv_reg, line)
            variables = {}
            if match is not None:
                args = match.group(1).split(',')
                #Create variables
                for var in args:
                    var = var.strip()
                    #TODO: ID Scope
                    scope = GlobalScope(project)
                    variables[var] = (ExprType(Type.BV64, 0), scope)
                expression = match.group(5)
                #TODO: ID Scope
                inv_scope = GlobalScope(project)
                invariant = Invariant(inv_scope, variables, expression)
                invariant.parse_expr()
                invariants.append(invariant.event)
    return invariants
