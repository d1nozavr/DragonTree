"""
DragonTree
Parser
"""

from core.Ast import (
    BinOpNode,
    NumberNode,
    OutputNode,
    StringNode,
    VariableNode,
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

    def parse(self):
        if self.peek().type != TokenType.EOF:
            result = self.statement()
            return result

    def statement(self):
        token = self.peek()

        if token.type == TokenType.ID:
            return self.assignment()

        elif token.type == TokenType.OUTPUT:
            self.advance()

            token = self.peek()
            if token.type == TokenType.COLON:
                self.advance()

                right = self.expr()

                return OutputNode(right).evaluate()

            raise SyntaxError("Need ':' after 'output'")

        raise SyntaxError(f"Invalid syntax {self.peek()}")

    def assignment(self):
        name = self.peek().value
        self.advance()

        if self.peek().type == TokenType.EQUALS:
            self.advance()
            value = self.expr()

            self.env[name] = value

        else:
            raise SyntaxError(f"Need '=' after {name} at pos {self.pos}")

    def expr(self):
        left = self.term()

        while True:
            token = self.peek()

            if token.type in (TokenType.PLUS, TokenType.MINUS):
                operation = token
                self.advance()

                right = self.term()

                left = BinOpNode(left, operation.value, right).evaluate()

                continue

            break
        return left

    def term(self):
        left = self.factor()

        while True:
            token = self.peek()

            if token.type in (TokenType.MULTIPLY, TokenType.DIVIDE):
                operation = token
                self.advance()

                right = self.factor()

                left = BinOpNode(left, operation.value, right).evaluate()

                continue

            break
        return left

    def factor(self):
        token = self.peek()

        if token.type == TokenType.NUMBER:
            self.advance()
            return NumberNode(token.value).evaluate()

        elif token.type == TokenType.STRING:
            self.advance()
            return StringNode(token.value).evaluate()

        elif token.type == TokenType.ID:
            self.advance()
            return VariableNode(self.env[token.value]).evaluate()

        elif token.type == TokenType.PLUS:
            self.advance()

            right = self.factor()
            return BinOpNode(None, token.value, right).evaluate()

        elif token.type == TokenType.MINUS:
            self.advance()

            right = self.factor()
            return BinOpNode(None, token.value, right).evaluate()

        raise RuntimeError(f"Unexpected token '{token.value}' at pos {self.pos}")
