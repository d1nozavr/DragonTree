"""
DragonTree
Token & TokenType
"""

from enum import Enum


class TokenType(Enum):
    """Token Types"""

    PLUS = "PLUS"
    MINUS = "MINUS"
    MULTIPLY = "MULTIPLY"
    DIVIDE = "DIVIDE"
    COLON = "COLON"

    NUMBER = "NUMBER"

    EOF = "EOF"


class Token:
    """Token"""

    def __init__(self, type: TokenType, value):
        self.type = type
        self.value = value

    def __repr__(self):
        return f"{self.type}: {self.value}"
