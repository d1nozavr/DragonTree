# =================================
#  DragonTree Programming Language
#  File: Interpreter.py
# =================================

from core.Lexer import Lexer
from core.Parser import Parser


class Interpreter:
    def __init__(self, debug=False):
        self.debug = debug

        self.env = {}

        self.line = 1
        self.string = None

        self.parser = Parser(self.env)

    def interpret(self, string):
        self.string = string

        tokens = Lexer(string).lex()

        if self.debug:
            print("Tokens:")

            for token in tokens:
                print(f"  - {token}")

            ast = self.parser.parse(tokens)

            if ast:
                ast.evaluate()

            self.line += 1

            print()

        else:
            ast = self.parser.parse(tokens)

            if ast:
                ast.evaluate()

            self.line += 1
