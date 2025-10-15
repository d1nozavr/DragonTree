"""
DragonTree
Interpreter
"""

import os

from core.lexer import Lexer

if __name__ == "__main__":
    lexer = Lexer()

    print("DragonTree [v0.0.1 (alpha)]")
    file_path = input("Path to 'file'.dt → ")

    if os.path.isfile(file_path):
        file = open(file_path, "r").read()

        tokens = list(lexer.lex(file))

        for token in tokens:
            print(token)
