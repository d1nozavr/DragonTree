"""
DragonTree
Lexer
"""

from core.Token import Token
from core.TokenType import TokenType


class Lexer:
    def __init__(self, string):
        self.string = string

        self.pos = 0
        self.length = len(self.string)

        self.tokens = []

        self.KEYWORDS = {"output"}

    def add_token(self, type, value):
        self.tokens.append(Token(type, value))

    def peek(self):
        return self.string[self.pos] if self.pos < self.length else None

    def advance(self):
        self.pos += 1

    def lex(self):
        while self.pos < self.length:
            if self.peek() in (" ", "\t", "\r", "\n"):
                self.advance()

            elif self.peek().isdigit():
                self.lex_number()

            elif self.peek().isalpha():
                self.lex_id()

            elif self.peek() == '"':
                self.lex_string()

            elif self.peek() == "+":
                self.add_token(TokenType.PLUS, "+")
                self.advance()

            elif self.peek() == "-":
                self.add_token(TokenType.MINUS, "-")
                self.advance()

            elif self.peek() == "*":
                self.advance()

                if self.peek() == "*":
                    self.advance()
                    self.add_token(TokenType.DOUBLE_STAR, "**")
                
                else:
                    self.advance()
                    self.add_token(TokenType.STAR, "*")

            elif self.peek() == "/":
                self.advance()

                if self.peek() == "/":
                    self.advance()
                    self.add_token(TokenType.DOUBLE_SLASH, "//")
                
                else:
                    self.advance()
                    self.add_token(TokenType.SLASH, "/")

            elif self.peek() == "%":
                self.advance()
                self.add_token(TokenType.PERCENT, "%")

            elif self.peek() == "=":
                self.advance()
                self.add_token(TokenType.EQUAL, "=")

            elif self.peek() == ":":
                self.advance()
                self.add_token(TokenType.COLON, ":")

            else:
                raise RuntimeError(f"Unknown token '{self.peek()}' at pos {self.pos}")

        self.add_token(TokenType.EOF, "EOF")
        return self.tokens

    def lex_number(self):
        number = ""

        while self.pos < self.length and (self.peek().isdigit() or self.peek() == "."):
            number += self.peek()
            self.advance()

        if "." in number and number.count(".") == 1:
            self.tokens.append(Token(TokenType.NUMBER, float(number)))

        elif "." in number and number.count(".") > 1:
            raise SyntaxError(f"Too much dots in '{number}'")

        else:
            self.add_token(TokenType.NUMBER, int(number))

    def lex_id(self):
        id = ""

        while self.pos < self.length and self.peek().isalnum():
            id += self.peek()
            self.advance()

        match id:
            case "output":
                self.add_token(TokenType.KEYWORD, id)

            case _:
                self.add_token(TokenType.IDENTIFIER, id)

    def lex_string(self):
        string = ""

        self.advance()

        while self.pos < self.length:
            if self.peek() == '"':
                self.advance()
                self.add_token(TokenType.STRING, string)
                break

            string += self.peek()
            self.advance()
