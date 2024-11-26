# Generated from Morse.g4 by ANTLR 4.13.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,37,19,2,0,7,0,2,1,7,1,2,2,7,2,1,0,1,0,1,0,5,0,10,8,0,10,0,12,
        0,13,9,0,1,1,1,1,1,2,1,2,1,2,0,0,3,0,2,4,0,2,1,0,1,26,1,0,27,36,
        18,0,11,1,0,0,0,2,14,1,0,0,0,4,16,1,0,0,0,6,10,3,2,1,0,7,10,3,4,
        2,0,8,10,5,37,0,0,9,6,1,0,0,0,9,7,1,0,0,0,9,8,1,0,0,0,10,13,1,0,
        0,0,11,9,1,0,0,0,11,12,1,0,0,0,12,1,1,0,0,0,13,11,1,0,0,0,14,15,
        7,0,0,0,15,3,1,0,0,0,16,17,7,1,0,0,17,5,1,0,0,0,2,9,11
    ]

class MorseParser ( Parser ):

    grammarFileName = "Morse.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'.-'", "'-...'", "'-.-.'", "'-..'", "'.'", 
                     "'..-.'", "'--.'", "'....'", "'..'", "'.---'", "'-.-'", 
                     "'.-..'", "'--'", "'-.'", "'---'", "'.--.'", "'--.-'", 
                     "'.-.'", "'...'", "'-'", "'..-'", "'...-'", "'.--'", 
                     "'-..-'", "'-.--'", "'--..'", "'-----'", "'.----'", 
                     "'..---'", "'...--'", "'....-'", "'.....'", "'-....'", 
                     "'--...'", "'---..'", "'----.'" ]

    symbolicNames = [ "<INVALID>", "A", "B", "C", "D", "E", "F", "G", "H", 
                      "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", 
                      "S", "T", "U", "V", "W", "X", "Y", "Z", "ZERO", "ONE", 
                      "TWO", "THREE", "FOUR", "FIVE", "SIX", "SEVEN", "EIGHT", 
                      "NINE", "WS" ]

    RULE_morse_code = 0
    RULE_letter = 1
    RULE_digit = 2

    ruleNames =  [ "morse_code", "letter", "digit" ]

    EOF = Token.EOF
    A=1
    B=2
    C=3
    D=4
    E=5
    F=6
    G=7
    H=8
    I=9
    J=10
    K=11
    L=12
    M=13
    N=14
    O=15
    P=16
    Q=17
    R=18
    S=19
    T=20
    U=21
    V=22
    W=23
    X=24
    Y=25
    Z=26
    ZERO=27
    ONE=28
    TWO=29
    THREE=30
    FOUR=31
    FIVE=32
    SIX=33
    SEVEN=34
    EIGHT=35
    NINE=36
    WS=37

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class Morse_codeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def letter(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MorseParser.LetterContext)
            else:
                return self.getTypedRuleContext(MorseParser.LetterContext,i)


        def digit(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MorseParser.DigitContext)
            else:
                return self.getTypedRuleContext(MorseParser.DigitContext,i)


        def WS(self, i:int=None):
            if i is None:
                return self.getTokens(MorseParser.WS)
            else:
                return self.getToken(MorseParser.WS, i)

        def getRuleIndex(self):
            return MorseParser.RULE_morse_code

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMorse_code" ):
                listener.enterMorse_code(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMorse_code" ):
                listener.exitMorse_code(self)




    def morse_code(self):

        localctx = MorseParser.Morse_codeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_morse_code)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 11
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 274877906942) != 0):
                self.state = 9
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26]:
                    self.state = 6
                    self.letter()
                    pass
                elif token in [27, 28, 29, 30, 31, 32, 33, 34, 35, 36]:
                    self.state = 7
                    self.digit()
                    pass
                elif token in [37]:
                    self.state = 8
                    self.match(MorseParser.WS)
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 13
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LetterContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def A(self):
            return self.getToken(MorseParser.A, 0)

        def B(self):
            return self.getToken(MorseParser.B, 0)

        def C(self):
            return self.getToken(MorseParser.C, 0)

        def D(self):
            return self.getToken(MorseParser.D, 0)

        def E(self):
            return self.getToken(MorseParser.E, 0)

        def F(self):
            return self.getToken(MorseParser.F, 0)

        def G(self):
            return self.getToken(MorseParser.G, 0)

        def H(self):
            return self.getToken(MorseParser.H, 0)

        def I(self):
            return self.getToken(MorseParser.I, 0)

        def J(self):
            return self.getToken(MorseParser.J, 0)

        def K(self):
            return self.getToken(MorseParser.K, 0)

        def L(self):
            return self.getToken(MorseParser.L, 0)

        def M(self):
            return self.getToken(MorseParser.M, 0)

        def N(self):
            return self.getToken(MorseParser.N, 0)

        def O(self):
            return self.getToken(MorseParser.O, 0)

        def P(self):
            return self.getToken(MorseParser.P, 0)

        def Q(self):
            return self.getToken(MorseParser.Q, 0)

        def R(self):
            return self.getToken(MorseParser.R, 0)

        def S(self):
            return self.getToken(MorseParser.S, 0)

        def T(self):
            return self.getToken(MorseParser.T, 0)

        def U(self):
            return self.getToken(MorseParser.U, 0)

        def V(self):
            return self.getToken(MorseParser.V, 0)

        def W(self):
            return self.getToken(MorseParser.W, 0)

        def X(self):
            return self.getToken(MorseParser.X, 0)

        def Y(self):
            return self.getToken(MorseParser.Y, 0)

        def Z(self):
            return self.getToken(MorseParser.Z, 0)

        def getRuleIndex(self):
            return MorseParser.RULE_letter

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLetter" ):
                listener.enterLetter(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLetter" ):
                listener.exitLetter(self)




    def letter(self):

        localctx = MorseParser.LetterContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_letter)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 14
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 134217726) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DigitContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ZERO(self):
            return self.getToken(MorseParser.ZERO, 0)

        def ONE(self):
            return self.getToken(MorseParser.ONE, 0)

        def TWO(self):
            return self.getToken(MorseParser.TWO, 0)

        def THREE(self):
            return self.getToken(MorseParser.THREE, 0)

        def FOUR(self):
            return self.getToken(MorseParser.FOUR, 0)

        def FIVE(self):
            return self.getToken(MorseParser.FIVE, 0)

        def SIX(self):
            return self.getToken(MorseParser.SIX, 0)

        def SEVEN(self):
            return self.getToken(MorseParser.SEVEN, 0)

        def EIGHT(self):
            return self.getToken(MorseParser.EIGHT, 0)

        def NINE(self):
            return self.getToken(MorseParser.NINE, 0)

        def getRuleIndex(self):
            return MorseParser.RULE_digit

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDigit" ):
                listener.enterDigit(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDigit" ):
                listener.exitDigit(self)




    def digit(self):

        localctx = MorseParser.DigitContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_digit)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 16
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 137304735744) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





