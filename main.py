"""
DragonTree
Runner
"""

from core.Lexer import Lexer


def main(debug=False):
    print("DragonTree v0.0.1 (alpha)")
    print("Type 'help' for more information.")

    while True:
        string = input("→ ")

        if string:
            if string == "quit":
                break

            tokens = Lexer(string).lex()

            print("Tokens:")

            for token in tokens:
                print(f"  - {token}")


if __name__ == "__main__":
    main()
