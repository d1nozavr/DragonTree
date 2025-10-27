"""
DragonTree
TokenType
"""

from enum import Enum


class TokenType(Enum):
    NUMBER = "NUMBER"
    STRING = "STRING"

    ID = "ID"
    EQUALS = "EQUALS"

    PLUS = "PLUS"
    MINUS = "MINUS"
    MULTIPLY = "MULTIPLY"
    DIVIDE = "DIVIDE"
    PERCENT = "PERCENT"

    COLON = "COLON"

    KEYWORD = "KEYWORD"

    EOF = "EOF"
