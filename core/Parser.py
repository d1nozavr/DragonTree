"""
DragonTree
Parser
"""

from core.Ast import (
    Assign,
    BinaryOperation,
    Identifier,
    Number,
    Output,
    String,
    UnaryOperation,
)
from core.TokenType import TokenType


class Parser:
    def __init__(self, tokens, env):
        self.env = env

        self.tokens: list = tokens

        self.pos: int = 0
        self.length: int = len(self.tokens)

    def peek(self):
        return self.tokens[self.pos] if self.pos < self.length else None

    def advance(self):
        self.pos += 1

    def expect(self, type):
        if self.peek().type == type:
            self.advance()

        else:
            raise ValueError(f"Expected '{type}', got {self.peek().type}")

    def parse(self):
        if self.peek().type != TokenType.EOF:
            return self.statement()

    def statement(self):
        token = self.peek()

        if token.type == TokenType.KEYWORD:
            match token.value:
                case "output":
                    self.advance()

                    if self.peek().type == TokenType.COLON:
                        self.advance()

                        rhs = self.expr()

                        return Output(rhs)

                    raise SyntaxError(f"Need ':' after 'output' at pos {self.pos}")

        elif token.type == TokenType.IDENTIFIER:
            name = token.value
            self.advance()

            if self.peek().type == TokenType.EQUAL:
                self.advance()

                rhs = self.expr()

                return Assign(self.env, name, rhs)

        raise SyntaxError(f"Invalid syntax: {self.peek().value} at pos {self.pos}")

    def expr(self):
        lhs = self.term()

        while True:
            token = self.peek()

            if token.type in (TokenType.PLUS, TokenType.MINUS):
                op = token.value
                self.advance()

                rhs = self.term()

                lhs = BinaryOperation(lhs, op, rhs)

                continue

            break

        return lhs

    def term(self):
        lhs = self.factor()

        while True:
            token = self.peek()

            if token.type in (
                TokenType.STAR,
                TokenType.SLASH,
                TokenType.DOUBLE_SLASH,
                TokenType.PERCENT,
            ):
                op = token.value
                self.advance()

                rhs = self.factor()

                lhs = BinaryOperation(lhs, op, rhs)

                continue

            break

        return lhs

    def factor(self):
        token = self.peek()

        if token.type in (TokenType.PLUS, TokenType.MINUS):
            op = token.value
            self.advance()

            expr = self.factor()
            return UnaryOperation(op, expr)

        return self.power()

    def power(self):
        lhs = self.atom()

        token = self.peek()
        if token.type == TokenType.DOUBLE_STAR:
            op = token.value
            self.advance()

            rhs = self.factor()

            lhs = BinaryOperation(lhs, op, rhs)

        return lhs

    def atom(self):
        token = self.peek()

        if token.type == TokenType.NUMBER:
            self.advance()
            return Number(token.value)

        elif token.type == TokenType.STRING:
            self.advance()
            return String(token.value)

        elif token.type == TokenType.IDENTIFIER:
            self.advance()
            return Identifier(self.env, token.value)

        elif token.type == TokenType.LPAREN:
            self.advance()

            val = self.expr()

            self.expect(TokenType.RPAREN)

            return val

        raise RuntimeError(f"Unexpected token '{token.value}' at pos {self.pos}")
