"""
DragonTree
Interpreter
"""

from core.Lexer import Lexer
from core.Parser import Parser


class Interpreter:
    def __init__(self, debug=False):
        self.env: dict = {}
        self.debug: bool = debug

    def interpret(self, string):
        tokens = Lexer(string).lex()
        parser = Parser(tokens, self.env)

        if self.debug:
            print("Tokens:")
            for token in tokens:
                print(f"  - {token}")

            parser.parse()
            print()

        else:
            parser.parse()
