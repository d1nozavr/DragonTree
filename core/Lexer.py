"""
DragonTree
Lexer
"""

from core.Token import Token
from core.TokenType import TokenType


class Lexer:
    def __init__(self, string):
        self.string: str = string
        self.pos: int = 0
        self.length: int = len(self.string)

        self.tokens: list = []

    def peek(self):
        return self.string[self.pos] if self.pos < self.length else None

    def advance(self):
        self.pos += 1

    def lex(self):
        while self.pos < self.length:
            if self.peek() == " " or self.peek() == "\n":
                self.advance()

            elif self.peek().isdigit():
                number = ""

                while self.pos < self.length and self.peek().isdigit():
                    number += self.peek()
                    self.advance()

                self.tokens.append(Token(TokenType.NUMBER, int(number)))

            elif self.peek().isalpha():
                word = ""

                while self.pos < self.length and self.peek().isalnum():
                    word += self.peek()
                    self.advance()

                if word == "output":
                    self.tokens.append(Token(TokenType.OUTPUT, word))

                else:
                    self.tokens.append(Token(TokenType.ID, word))

            elif self.peek() == '"':
                string = ""

                self.advance()

                while self.pos < self.length:
                    string += self.peek()
                    self.advance()

                    if self.peek() == '"':
                        self.advance()
                        self.tokens.append(Token(TokenType.STRING, string))
                        break

            elif self.peek() == "+":
                self.tokens.append(Token(TokenType.PLUS, "+"))
                self.advance()

            elif self.peek() == "-":
                self.tokens.append(Token(TokenType.MINUS, "-"))
                self.advance()

            elif self.peek() == "*":
                self.tokens.append(Token(TokenType.MULTIPLY, "*"))
                self.advance()

            elif self.peek() == "/":
                self.tokens.append(Token(TokenType.DIVIDE, "/"))
                self.advance()

            elif self.peek() == "=":
                self.tokens.append(Token(TokenType.EQUALS, "="))
                self.advance()

            elif self.peek() == ":":
                self.tokens.append(Token(TokenType.COLON, ":"))
                self.advance()

            else:
                raise RuntimeError(f"Unknown token '{self.peek()}' at pos {self.pos}")

        self.tokens.append(Token(TokenType.EOF, "EOF"))
        return self.tokens
