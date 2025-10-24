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
        results = self.expr()
        
        return results

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
        
        elif token.type == TokenType.PLUS:
            self.advance()

            right = self.factor()
            return BinOpNode(None, token.value, right).evaluate()
        
        elif token.type == TokenType.MINUS:
            self.advance()

            right = self.factor()
            return BinOpNode(None, token.value, right).evaluate()
        
        raise RuntimeError(f"Unexpected token '{token}' at pos {self.pos}")
