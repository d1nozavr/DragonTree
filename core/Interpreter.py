"""
DragonTree
Interpreter
"""

from core.Lexer import Lexer
from core.Parser import Parser


class Interpreter:
    def __init__(self, debug=False):
        self.debug = debug

    def interpret(self, string):
        tokens: list = Lexer(string).lex()
        parser = Parser(tokens).parse()

        if self.debug:
            print("Tokens:")
            for token in tokens:
                print(f"  - {token}")

            if parser:
                print(f"Result: {parser} type={type(parser)}")
                print()

        else:
            if parser:
                print(f"{parser}")
