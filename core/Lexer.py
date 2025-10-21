from core.Token import Token
from core.TokenType import TokenType


class Lexer:
    def __init__(self, _string):
        self._pos: int = 0

        self._string: str = _string

        self._length: int = len(self._string)

        self._tokens: list = []

    def lex(self):
        while self._pos < self._length:
            if self._string[self._pos].isdigit():
                number = ""

                while self._pos < self._length and self._string[self._pos].isdigit():
                    number += self._string[self._pos]
                    self._pos += 1

                self._tokens.append(Token(TokenType.NUMBER, int(number)))
                continue

            elif self._string[self._pos] == "+":
                self._tokens.append(Token(TokenType.PLUS))
                self._pos += 1

            elif self._string[self._pos] == "-":
                self._tokens.append(Token(TokenType.MINUS))
                self._pos += 1

            elif self._string[self._pos] == "*":
                self._tokens.append(Token(TokenType.MULTIPLY))
                self._pos += 1

            elif self._string[self._pos] == "/":
                self._tokens.append(Token(TokenType.DIVIDE))
                self._pos += 1

            elif self._string[self._pos] == ":":
                self._tokens.append(Token(TokenType.COLON))
                self._pos += 1

            else:
                raise RuntimeError(f"unknown token at {self._pos}")

        self._tokens.append(Token(TokenType.EOF))
        return self._tokens
