# =================================
#  DragonTree Programming Language
#  File: Parser.py
# =================================

from core.Ast import (
    Assign,
    BinaryOperation,
    FloatLiteral,
    Identifier,
    IntLiteral,
    Output,
    StringLiteral,
    UnaryOperation,
)
from core.TokenType import TokenType


class Parser:
    def __init__(self, env, tokens):
        self.env = env

        self.tokens = tokens

        self.pos = 0
        self.length = len(self.tokens)

    def parse(self):
        if self._peek().type != TokenType.EOF:
            return self.__statement()

    def __statement(self):
        token = self._peek()

        match token.type:
            case TokenType.KEYWORD:
                match token.value:
                    case "output":
                        self._advance()

                        if self._peek().type == TokenType.COLON:
                            self._advance()

                            rhs = self.__expr()

                            return Output(rhs)

                        raise SyntaxError(f"Need ':' after 'output' at pos {self.pos}")

            case TokenType.IDENTIFIER:
                lhs = token.value
                self._advance()

                token = self._peek()
                if token.type == TokenType.OPERATOR and token.value == "=":
                    self._advance()

                    token = self._peek()
                    if token.type == TokenType.KEYWORD and token.value == "getline":
                        rhs = input()
                        return Assign(self.env, lhs, rhs)

                    rhs = self.__expr()
                    return Assign(self.env, lhs, rhs)

                raise NameError(f"Unknown name '{lhs}'")

            case _:
                raise SyntaxError("Invalid syntax")

    def __expr(self):
        lhs = self.__term()

        while True:
            token = self._peek()

            if token.type == TokenType.OPERATOR and token.value in ("+", "-"):
                op = token.value
                self._advance()

                rhs = self.__term()

                lhs = BinaryOperation(lhs, op, rhs)

                continue

            break

        return lhs

    def __term(self):
        lhs = self.__factor()

        while True:
            token = self._peek()

            if token.type == TokenType.OPERATOR and token.value in (
                "*",
                "/",
                "//",
                "%",
            ):
                op = token.value
                self._advance()

                rhs = self.__factor()

                lhs = BinaryOperation(lhs, op, rhs)

                continue

            break

        return lhs

    def __factor(self):
        token = self._peek()

        if token.type == TokenType.OPERATOR and token.value in ("+", "-"):
            op = token.value
            self._advance()

            expr = self.__factor()
            return UnaryOperation(op, expr)

        return self.__power()

    def __power(self):
        lhs = self.__atom()

        token = self._peek()
        if token.type == TokenType.OPERATOR and token.value == "**":
            op = "**"
            self._advance()

            rhs = self.__factor()

            lhs = BinaryOperation(lhs, op, rhs)

        return lhs

    def __atom(self):
        token = self._peek()

        match token.type:
            case TokenType.INT_LITERAL:
                self._advance()
                return IntLiteral(token.value)

            case TokenType.FLOAT_LITERAL:
                self._advance()
                return FloatLiteral(token.value)

            case TokenType.STRING_LITERAL:
                self._advance()
                return StringLiteral(token.value)

            case TokenType.IDENTIFIER:
                self._advance()
                return Identifier(self.env, token.value)

            case TokenType.LPAREN:
                self._advance()

                rhs = self.__expr()

                self._expect(TokenType.RPAREN)

                return rhs

            case _:
                raise RuntimeError(f"Unexpected token '{token.value}', pos {self.pos}")

    def _peek(self):
        return self.tokens[self.pos] if self.pos < self.length else None

    def _advance(self):
        self.pos += 1

    def _expect(self, type):
        if self._peek().type == type:
            self._advance()

        else:
            raise ValueError(f"Expected '{type}', got '{self._peek().type}'")
