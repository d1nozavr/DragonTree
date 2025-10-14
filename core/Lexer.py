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

        while self.pos < len(string):
            if string[self.pos].isdigit():
                number = ""

                while self.pos < len(string) and string[self.pos].isdigit():
                    number += string[self.pos]
                    self.pos += 1

                tokens.append(Token(TokenType.NUMBER, int(number)))
                continue

            elif string[self.pos] == "+":
                tokens.append(Token(TokenType.PLUS, "+"))
                self.pos += 1

            elif string[self.pos] == "-":
                tokens.append(Token(TokenType.MINUS, "-"))
                self.pos += 1

            elif string[self.pos] == "*":
                tokens.append(Token(TokenType.MULTIPLY, "*"))
                self.pos += 1

            elif string[self.pos] == "/":
                tokens.append(Token(TokenType.DIVIDE, "/"))
                self.pos += 1

            elif string[self.pos] == ":":
                tokens.append(Token(TokenType.COLON, ":"))
                self.pos += 1

            else:
                raise RuntimeError(f"unknown token at {self.pos}")

        tokens.append(Token(TokenType.EOF, "EOF"))
        return tokens
