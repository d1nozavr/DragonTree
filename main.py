"""
DragonTree
Runner for DragonTree
Warning! > It's will soon replaced by 'shell'
"""

from core.Lexer import Lexer

if __name__ == "__main__":
    print("DragonTree v0.0.1 (alpha)")
    print("Type 'quit' for quit")

    while True:
        string = input("→ ")

        if string == "quit":
            break

        tokens = Lexer(string).lex()

        print(f"{tokens}")
