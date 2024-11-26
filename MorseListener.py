# Generated from Morse.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .MorseParser import MorseParser
else:
    from MorseParser import MorseParser

# This class defines a complete listener for a parse tree produced by MorseParser.
class MorseListener(ParseTreeListener):

    # Enter a parse tree produced by MorseParser#morse_code.
    def enterMorse_code(self, ctx:MorseParser.Morse_codeContext):
        pass

    # Exit a parse tree produced by MorseParser#morse_code.
    def exitMorse_code(self, ctx:MorseParser.Morse_codeContext):
        pass


    # Enter a parse tree produced by MorseParser#letter.
    def enterLetter(self, ctx:MorseParser.LetterContext):
        pass

    # Exit a parse tree produced by MorseParser#letter.
    def exitLetter(self, ctx:MorseParser.LetterContext):
        pass


    # Enter a parse tree produced by MorseParser#digit.
    def enterDigit(self, ctx:MorseParser.DigitContext):
        pass

    # Exit a parse tree produced by MorseParser#digit.
    def exitDigit(self, ctx:MorseParser.DigitContext):
        pass



del MorseParser