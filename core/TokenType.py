"""
DragonTree
TokenType
"""

from enum import Enum


class TokenType(Enum):
    NUMBER = "NUMBER"
    ID = "ID"

    PLUS = "PLUS"
    MINUS = "MINUS"
    MULTIPLY = "MULTIPLY"
    DIVIDE = "DIVIDE"
    COLON = "COLON"

    OUTPUT = "OUTPUT"

    EOF = "EOF"
