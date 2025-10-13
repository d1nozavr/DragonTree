"""
DragonTree
Lexer
"""

from core.Token import Token, TokenType


class Lexer:
    """Lexer for DragonTree"""

    def __init__(self):
        self.pos = 0

    def lex(self, string):
        tokens = []

        for index in range(len(string)):
            if string[index] == "+":
                tokens.append(Token(TokenType.PLUS, "+"))
                self.pos += 1

            elif string[index] == "-":
                tokens.append(Token(TokenType.MINUS, "-"))
                self.pos += 1

            elif string[index] == "*":
                tokens.append(Token(TokenType.MULTIPLY, "*"))
                self.pos += 1

            elif string[index] == "/":
                tokens.append(Token(TokenType.DIVIDE, "/"))
                self.pos += 1

            else:
                return f"error: unknown token at pos {self.pos + 1}"

        return tokens
