"""
DragonTree
Token & TokenType
"""

from enum import Enum


class TokenType(Enum):
    """Token Types"""

    # keywords
    OUTPUT = "OUTPUT"
    VAR = "VAR"

    # identifiers and literals
    IDENTIFIER = "IDENTIFIER"
    NUMBER = "NUMBER"
    STRING = "STRING"

    # operators
    PLUS = "PLUS"
    MINUS = "MINUS"
    MULTIPLY = "MULTIPLY"
    DIVIDE = "DIVIDE"

    # special tokens
    COMMENT = "COMMENT"
    EOF = "EOF"


class Token:
    """Token"""

    def __init__(self, type: TokenType, value):
        self.type = type
        self.value = value

    def __repr__(self):
        return f"{self.type}: {self.value}"
