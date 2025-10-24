"""
DragonTree
Runner
"""

from core.Lexer import Lexer
from core.Parser import Parser


def help():
    print("Help:")
    print("  - 'quit'")


def main(debug=False):
    print("DragonTree v0.0.1 (alpha)")
    print("Type 'help' for more information.")

    while True:
        string = input("→ ")

        if string:
            if string == "quit":
                break

            elif string == "help":
                help()

            else:
                tokens = Lexer(string).lex()
                parser = Parser(tokens).parse()

                if debug:
                    print("Tokens:")

                    for token in tokens:
                        print(f"  - {token}")

                    print(f"Result: {parser} type={type(parser)}")

                else:
                    print(f"{parser}")


if __name__ == "__main__":
    main(debug=False)
