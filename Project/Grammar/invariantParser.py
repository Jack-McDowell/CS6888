# Generated from invariant.g4 by ANTLR 4.7.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys

def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\36")
        buf.write("T\4\2\t\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2")
        buf.write("\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\5\2\32\n\2\3")
        buf.write("\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2")
        buf.write("\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3")
        buf.write("\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\7\2?\n\2\f\2\16\2B\13\2")
        buf.write("\5\2D\n\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\7\2O\n\2")
        buf.write("\f\2\16\2R\13\2\3\2\2\3\2\3\2\2\6\3\2\n\13\3\2\f\r\3\2")
        buf.write("\16\21\3\2\22\23\2i\2\31\3\2\2\2\4\5\b\2\1\2\5\6\7\n\2")
        buf.write("\2\6\32\5\2\2\26\7\b\7\r\2\2\b\32\7\34\2\2\t\n\7\27\2")
        buf.write("\2\n\32\5\2\2\24\13\f\7\t\2\2\f\r\5\2\2\2\r\16\7\5\2\2")
        buf.write("\16\32\3\2\2\2\17\20\7\33\2\2\20\32\5\2\2\t\21\22\7\32")
        buf.write("\2\2\22\32\5\2\2\6\23\32\7\35\2\2\24\32\7\34\2\2\25\26")
        buf.write("\7\3\2\2\26\27\5\2\2\2\27\30\7\5\2\2\30\32\3\2\2\2\31")
        buf.write("\4\3\2\2\2\31\7\3\2\2\2\31\t\3\2\2\2\31\13\3\2\2\2\31")
        buf.write("\17\3\2\2\2\31\21\3\2\2\2\31\23\3\2\2\2\31\24\3\2\2\2")
        buf.write("\31\25\3\2\2\2\32P\3\2\2\2\33\34\f\23\2\2\34\35\7\24\2")
        buf.write("\2\35O\5\2\2\24\36\37\f\22\2\2\37 \t\2\2\2 O\5\2\2\23")
        buf.write("!\"\f\21\2\2\"#\t\3\2\2#O\5\2\2\22$%\f\16\2\2%&\t\4\2")
        buf.write("\2&O\5\2\2\17\'(\f\r\2\2()\t\5\2\2)O\5\2\2\16*+\f\f\2")
        buf.write("\2+,\7\27\2\2,O\5\2\2\r-.\f\13\2\2./\7\31\2\2/O\5\2\2")
        buf.write("\f\60\61\f\n\2\2\61\62\7\30\2\2\62O\5\2\2\13\63\64\f\b")
        buf.write("\2\2\64\65\7\25\2\2\65O\5\2\2\t\66\67\f\7\2\2\678\7\26")
        buf.write("\2\28O\5\2\2\b9:\f\30\2\2:C\7\3\2\2;@\5\2\2\2<=\7\4\2")
        buf.write("\2=?\5\2\2\2><\3\2\2\2?B\3\2\2\2@>\3\2\2\2@A\3\2\2\2A")
        buf.write("D\3\2\2\2B@\3\2\2\2C;\3\2\2\2CD\3\2\2\2DE\3\2\2\2EO\7")
        buf.write("\5\2\2FG\f\27\2\2GH\7\6\2\2HO\7\35\2\2IJ\f\20\2\2JK\7")
        buf.write("\7\2\2KL\5\2\2\2LM\7\b\2\2MO\3\2\2\2N\33\3\2\2\2N\36\3")
        buf.write("\2\2\2N!\3\2\2\2N$\3\2\2\2N\'\3\2\2\2N*\3\2\2\2N-\3\2")
        buf.write("\2\2N\60\3\2\2\2N\63\3\2\2\2N\66\3\2\2\2N9\3\2\2\2NF\3")
        buf.write("\2\2\2NI\3\2\2\2OR\3\2\2\2PN\3\2\2\2PQ\3\2\2\2Q\3\3\2")
        buf.write("\2\2RP\3\2\2\2\7\31@CNP")
        return buf.getvalue()


class invariantParser ( Parser ):

    grammarFileName = "invariant.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'('", "','", "')'", "'.'", "'['", "']'", 
                     "'NEXT('", "'*'", "'/'", "'+'", "'-'", "'>'", "'<'", 
                     "'<='", "'>='", "'=='", "'!='", "'**'", "'&&'", "'||'", 
                     "'&'", "'|'", "'^'", "'!'", "'~'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "MUL", "DIV", "ADD", "SUB", "GT", "LT", "GTE", "LTE", 
                      "EQ", "NE", "EXP", "LAND", "LOR", "BAND", "BOR", "BXOR", 
                      "LNOT", "BNOT", "NUMBER", "IDENTIFIER", "WS" ]

    RULE_expr = 0

    ruleNames =  [ "expr" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    T__6=7
    MUL=8
    DIV=9
    ADD=10
    SUB=11
    GT=12
    LT=13
    GTE=14
    LTE=15
    EQ=16
    NE=17
    EXP=18
    LAND=19
    LOR=20
    BAND=21
    BOR=22
    BXOR=23
    LNOT=24
    BNOT=25
    NUMBER=26
    IDENTIFIER=27
    WS=28

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.7.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None



    class ExprContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return invariantParser.RULE_expr

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)


    class ExponentiationExprContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a invariantParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(invariantParser.ExprContext)
            else:
                return self.getTypedRuleContext(invariantParser.ExprContext,i)

        def EXP(self):
            return self.getToken(invariantParser.EXP, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExponentiationExpr" ):
                listener.enterExponentiationExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExponentiationExpr" ):
                listener.exitExponentiationExpr(self)


    class NegNumberContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a invariantParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def SUB(self):
            return self.getToken(invariantParser.SUB, 0)
        def NUMBER(self):
            return self.getToken(invariantParser.NUMBER, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNegNumber" ):
                listener.enterNegNumber(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNegNumber" ):
                listener.exitNegNumber(self)


    class NextExprContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a invariantParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self):
            return self.getTypedRuleContext(invariantParser.ExprContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNextExpr" ):
                listener.enterNextExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNextExpr" ):
                listener.exitNextExpr(self)


    class BnotExprContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a invariantParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def BNOT(self):
            return self.getToken(invariantParser.BNOT, 0)
        def expr(self):
            return self.getTypedRuleContext(invariantParser.ExprContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBnotExpr" ):
                listener.enterBnotExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBnotExpr" ):
                listener.exitBnotExpr(self)


    class AdditiveExprContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a invariantParser.ExprContext
            super().__init__(parser)
            self.op = None # Token
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(invariantParser.ExprContext)
            else:
                return self.getTypedRuleContext(invariantParser.ExprContext,i)

        def ADD(self):
            return self.getToken(invariantParser.ADD, 0)
        def SUB(self):
            return self.getToken(invariantParser.SUB, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAdditiveExpr" ):
                listener.enterAdditiveExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAdditiveExpr" ):
                listener.exitAdditiveExpr(self)


    class RelationalExprContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a invariantParser.ExprContext
            super().__init__(parser)
            self.op = None # Token
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(invariantParser.ExprContext)
            else:
                return self.getTypedRuleContext(invariantParser.ExprContext,i)

        def GT(self):
            return self.getToken(invariantParser.GT, 0)
        def GTE(self):
            return self.getToken(invariantParser.GTE, 0)
        def LT(self):
            return self.getToken(invariantParser.LT, 0)
        def LTE(self):
            return self.getToken(invariantParser.LTE, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRelationalExpr" ):
                listener.enterRelationalExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRelationalExpr" ):
                listener.exitRelationalExpr(self)


    class BandExprContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a invariantParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(invariantParser.ExprContext)
            else:
                return self.getTypedRuleContext(invariantParser.ExprContext,i)

        def BAND(self):
            return self.getToken(invariantParser.BAND, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBandExpr" ):
                listener.enterBandExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBandExpr" ):
                listener.exitBandExpr(self)


    class DeRefExprContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a invariantParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def MUL(self):
            return self.getToken(invariantParser.MUL, 0)
        def expr(self):
            return self.getTypedRuleContext(invariantParser.ExprContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDeRefExpr" ):
                listener.enterDeRefExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDeRefExpr" ):
                listener.exitDeRefExpr(self)


    class NumExprContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a invariantParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def NUMBER(self):
            return self.getToken(invariantParser.NUMBER, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNumExpr" ):
                listener.enterNumExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNumExpr" ):
                listener.exitNumExpr(self)


    class ParenExprContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a invariantParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self):
            return self.getTypedRuleContext(invariantParser.ExprContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterParenExpr" ):
                listener.enterParenExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitParenExpr" ):
                listener.exitParenExpr(self)


    class BorExprContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a invariantParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(invariantParser.ExprContext)
            else:
                return self.getTypedRuleContext(invariantParser.ExprContext,i)

        def BOR(self):
            return self.getToken(invariantParser.BOR, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBorExpr" ):
                listener.enterBorExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBorExpr" ):
                listener.exitBorExpr(self)


    class IndexExprContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a invariantParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(invariantParser.ExprContext)
            else:
                return self.getTypedRuleContext(invariantParser.ExprContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIndexExpr" ):
                listener.enterIndexExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIndexExpr" ):
                listener.exitIndexExpr(self)


    class VarExprContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a invariantParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def IDENTIFIER(self):
            return self.getToken(invariantParser.IDENTIFIER, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterVarExpr" ):
                listener.enterVarExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitVarExpr" ):
                listener.exitVarExpr(self)


    class LandExprContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a invariantParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(invariantParser.ExprContext)
            else:
                return self.getTypedRuleContext(invariantParser.ExprContext,i)

        def LAND(self):
            return self.getToken(invariantParser.LAND, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLandExpr" ):
                listener.enterLandExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLandExpr" ):
                listener.exitLandExpr(self)


    class NotExprContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a invariantParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def LNOT(self):
            return self.getToken(invariantParser.LNOT, 0)
        def expr(self):
            return self.getTypedRuleContext(invariantParser.ExprContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNotExpr" ):
                listener.enterNotExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNotExpr" ):
                listener.exitNotExpr(self)


    class RefExprContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a invariantParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def BAND(self):
            return self.getToken(invariantParser.BAND, 0)
        def expr(self):
            return self.getTypedRuleContext(invariantParser.ExprContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRefExpr" ):
                listener.enterRefExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRefExpr" ):
                listener.exitRefExpr(self)


    class LorExprContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a invariantParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(invariantParser.ExprContext)
            else:
                return self.getTypedRuleContext(invariantParser.ExprContext,i)

        def LOR(self):
            return self.getToken(invariantParser.LOR, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLorExpr" ):
                listener.enterLorExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLorExpr" ):
                listener.exitLorExpr(self)


    class MultiplicativeExprContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a invariantParser.ExprContext
            super().__init__(parser)
            self.op = None # Token
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(invariantParser.ExprContext)
            else:
                return self.getTypedRuleContext(invariantParser.ExprContext,i)

        def MUL(self):
            return self.getToken(invariantParser.MUL, 0)
        def DIV(self):
            return self.getToken(invariantParser.DIV, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMultiplicativeExpr" ):
                listener.enterMultiplicativeExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMultiplicativeExpr" ):
                listener.exitMultiplicativeExpr(self)


    class FunAppExprContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a invariantParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(invariantParser.ExprContext)
            else:
                return self.getTypedRuleContext(invariantParser.ExprContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFunAppExpr" ):
                listener.enterFunAppExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFunAppExpr" ):
                listener.exitFunAppExpr(self)


    class EqualityExprContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a invariantParser.ExprContext
            super().__init__(parser)
            self.op = None # Token
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(invariantParser.ExprContext)
            else:
                return self.getTypedRuleContext(invariantParser.ExprContext,i)

        def EQ(self):
            return self.getToken(invariantParser.EQ, 0)
        def NE(self):
            return self.getToken(invariantParser.NE, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterEqualityExpr" ):
                listener.enterEqualityExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitEqualityExpr" ):
                listener.exitEqualityExpr(self)


    class BxorExprContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a invariantParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(invariantParser.ExprContext)
            else:
                return self.getTypedRuleContext(invariantParser.ExprContext,i)

        def BXOR(self):
            return self.getToken(invariantParser.BXOR, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBxorExpr" ):
                listener.enterBxorExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBxorExpr" ):
                listener.exitBxorExpr(self)


    class AccessExprContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a invariantParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self):
            return self.getTypedRuleContext(invariantParser.ExprContext,0)

        def IDENTIFIER(self):
            return self.getToken(invariantParser.IDENTIFIER, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAccessExpr" ):
                listener.enterAccessExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAccessExpr" ):
                listener.exitAccessExpr(self)



    def expr(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = invariantParser.ExprContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 0
        self.enterRecursionRule(localctx, 0, self.RULE_expr, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 23
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [invariantParser.MUL]:
                localctx = invariantParser.DeRefExprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx

                self.state = 3
                self.match(invariantParser.MUL)
                self.state = 4
                self.expr(20)
                pass
            elif token in [invariantParser.SUB]:
                localctx = invariantParser.NegNumberContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 5
                self.match(invariantParser.SUB)
                self.state = 6
                self.match(invariantParser.NUMBER)
                pass
            elif token in [invariantParser.BAND]:
                localctx = invariantParser.RefExprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 7
                self.match(invariantParser.BAND)
                self.state = 8
                self.expr(18)
                pass
            elif token in [invariantParser.T__6]:
                localctx = invariantParser.NextExprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 9
                self.match(invariantParser.T__6)
                self.state = 10
                self.expr(0)
                self.state = 11
                self.match(invariantParser.T__2)
                pass
            elif token in [invariantParser.BNOT]:
                localctx = invariantParser.BnotExprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 13
                self.match(invariantParser.BNOT)
                self.state = 14
                self.expr(7)
                pass
            elif token in [invariantParser.LNOT]:
                localctx = invariantParser.NotExprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 15
                self.match(invariantParser.LNOT)
                self.state = 16
                self.expr(4)
                pass
            elif token in [invariantParser.IDENTIFIER]:
                localctx = invariantParser.VarExprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 17
                self.match(invariantParser.IDENTIFIER)
                pass
            elif token in [invariantParser.NUMBER]:
                localctx = invariantParser.NumExprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 18
                self.match(invariantParser.NUMBER)
                pass
            elif token in [invariantParser.T__0]:
                localctx = invariantParser.ParenExprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 19
                self.match(invariantParser.T__0)
                self.state = 20
                self.expr(0)
                self.state = 21
                self.match(invariantParser.T__2)
                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 78
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,4,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 76
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
                    if la_ == 1:
                        localctx = invariantParser.ExponentiationExprContext(self, invariantParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 25
                        if not self.precpred(self._ctx, 17):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 17)")
                        self.state = 26
                        self.match(invariantParser.EXP)
                        self.state = 27
                        self.expr(18)
                        pass

                    elif la_ == 2:
                        localctx = invariantParser.MultiplicativeExprContext(self, invariantParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 28
                        if not self.precpred(self._ctx, 16):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 16)")
                        self.state = 29
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not(_la==invariantParser.MUL or _la==invariantParser.DIV):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 30
                        self.expr(17)
                        pass

                    elif la_ == 3:
                        localctx = invariantParser.AdditiveExprContext(self, invariantParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 31
                        if not self.precpred(self._ctx, 15):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 15)")
                        self.state = 32
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not(_la==invariantParser.ADD or _la==invariantParser.SUB):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 33
                        self.expr(16)
                        pass

                    elif la_ == 4:
                        localctx = invariantParser.RelationalExprContext(self, invariantParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 34
                        if not self.precpred(self._ctx, 12):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 12)")
                        self.state = 35
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << invariantParser.GT) | (1 << invariantParser.LT) | (1 << invariantParser.GTE) | (1 << invariantParser.LTE))) != 0)):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 36
                        self.expr(13)
                        pass

                    elif la_ == 5:
                        localctx = invariantParser.EqualityExprContext(self, invariantParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 37
                        if not self.precpred(self._ctx, 11):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 11)")
                        self.state = 38
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not(_la==invariantParser.EQ or _la==invariantParser.NE):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 39
                        self.expr(12)
                        pass

                    elif la_ == 6:
                        localctx = invariantParser.BandExprContext(self, invariantParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 40
                        if not self.precpred(self._ctx, 10):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 10)")
                        self.state = 41
                        self.match(invariantParser.BAND)
                        self.state = 42
                        self.expr(11)
                        pass

                    elif la_ == 7:
                        localctx = invariantParser.BxorExprContext(self, invariantParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 43
                        if not self.precpred(self._ctx, 9):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 9)")
                        self.state = 44
                        self.match(invariantParser.BXOR)
                        self.state = 45
                        self.expr(10)
                        pass

                    elif la_ == 8:
                        localctx = invariantParser.BorExprContext(self, invariantParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 46
                        if not self.precpred(self._ctx, 8):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 8)")
                        self.state = 47
                        self.match(invariantParser.BOR)
                        self.state = 48
                        self.expr(9)
                        pass

                    elif la_ == 9:
                        localctx = invariantParser.LandExprContext(self, invariantParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 49
                        if not self.precpred(self._ctx, 6):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 6)")
                        self.state = 50
                        self.match(invariantParser.LAND)
                        self.state = 51
                        self.expr(7)
                        pass

                    elif la_ == 10:
                        localctx = invariantParser.LorExprContext(self, invariantParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 52
                        if not self.precpred(self._ctx, 5):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 5)")
                        self.state = 53
                        self.match(invariantParser.LOR)
                        self.state = 54
                        self.expr(6)
                        pass

                    elif la_ == 11:
                        localctx = invariantParser.FunAppExprContext(self, invariantParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 55
                        if not self.precpred(self._ctx, 22):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 22)")
                        self.state = 56
                        self.match(invariantParser.T__0)
                        self.state = 65
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)
                        if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << invariantParser.T__0) | (1 << invariantParser.T__6) | (1 << invariantParser.MUL) | (1 << invariantParser.SUB) | (1 << invariantParser.BAND) | (1 << invariantParser.LNOT) | (1 << invariantParser.BNOT) | (1 << invariantParser.NUMBER) | (1 << invariantParser.IDENTIFIER))) != 0):
                            self.state = 57
                            self.expr(0)
                            self.state = 62
                            self._errHandler.sync(self)
                            _la = self._input.LA(1)
                            while _la==invariantParser.T__1:
                                self.state = 58
                                self.match(invariantParser.T__1)
                                self.state = 59
                                self.expr(0)
                                self.state = 64
                                self._errHandler.sync(self)
                                _la = self._input.LA(1)



                        self.state = 67
                        self.match(invariantParser.T__2)
                        pass

                    elif la_ == 12:
                        localctx = invariantParser.AccessExprContext(self, invariantParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 68
                        if not self.precpred(self._ctx, 21):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 21)")
                        self.state = 69
                        self.match(invariantParser.T__3)
                        self.state = 70
                        self.match(invariantParser.IDENTIFIER)
                        pass

                    elif la_ == 13:
                        localctx = invariantParser.IndexExprContext(self, invariantParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 71
                        if not self.precpred(self._ctx, 14):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 14)")
                        self.state = 72
                        self.match(invariantParser.T__4)
                        self.state = 73
                        self.expr(0)
                        self.state = 74
                        self.match(invariantParser.T__5)
                        pass

             
                self.state = 80
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,4,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[0] = self.expr_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expr_sempred(self, localctx:ExprContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 17)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 16)
         

            if predIndex == 2:
                return self.precpred(self._ctx, 15)
         

            if predIndex == 3:
                return self.precpred(self._ctx, 12)
         

            if predIndex == 4:
                return self.precpred(self._ctx, 11)
         

            if predIndex == 5:
                return self.precpred(self._ctx, 10)
         

            if predIndex == 6:
                return self.precpred(self._ctx, 9)
         

            if predIndex == 7:
                return self.precpred(self._ctx, 8)
         

            if predIndex == 8:
                return self.precpred(self._ctx, 6)
         

            if predIndex == 9:
                return self.precpred(self._ctx, 5)
         

            if predIndex == 10:
                return self.precpred(self._ctx, 22)
         

            if predIndex == 11:
                return self.precpred(self._ctx, 21)
         

            if predIndex == 12:
                return self.precpred(self._ctx, 14)
         




