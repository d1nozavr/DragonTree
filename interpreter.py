"""
DragonTree
Interpreter
Not final variant
"""

import core.Lexer


def main():
    Lexer = core.Lexer.Lexer()
    print("DragonTree 0.0.1 (pre-alpha)")
    print("Type 'quit' to quit")

    while True:
        string = input("→ ")

        if string:
            if string == "quit":
                break
            print(Lexer.lex(string))


if __name__ == "__main__":
    main()
