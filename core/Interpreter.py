# =================================
#  DragonTree Programming Language
#  File: Interpreter.py
# =================================

from core.Lexer import Lexer
from core.Parser import Parser


class Interpreter:
    def __init__(self, debug=False):
        self.env: dict = {}
        self.debug: bool = debug

        self.line = 1
        self.string = None

    def interpret(self, string):
        self.string = string

        tokens = Lexer(string).lex()
        parser = Parser(self.env, tokens).parse()

        if self.debug:
            print("Tokens:")
            for token in tokens:
                print(f"  - {token}")

            if parser:
                parser.evaluate()

            self.line += 1

            print()

        else:
            if parser:
                parser.evaluate()

            self.line += 1
