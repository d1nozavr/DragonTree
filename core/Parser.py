"""
DragonTree
Parser
"""

from core.Ast import (
    BinOpNode,
    NumberNode,
)
from core.TokenType import TokenType


class Parser:
    def __init__(self, tokens):
        self.tokens: list = tokens

        self.pos: int = 0
        self.length: int = len(self.tokens)

    def peek(self):
        return self.tokens[self.pos] if self.pos < self.length else None

    def advance(self):
        self.pos += 1

    def parse(self):
        return self.expr()

    def expr(self):
        left = self.term()

        if self.peek().type in (TokenType.PLUS, TokenType.MINUS):
            operation = self.peek()
            self.advance()

            right = self.term()

            left = BinOpNode(left, operation.value, right).evaluate()

        return left

    def term(self):
        left = self.factor()

        if self.peek().type in (TokenType.MULTIPLY, TokenType.DIVIDE):
            operation = self.peek()
            self.advance()

            right = self.factor()

            left = BinOpNode(left, operation.value, right).evaluate()

        return left

    def factor(self):
        token = self.peek()

        if token.type == TokenType.NUMBER:
            self.advance()
            return NumberNode(token.value).evaluate()
