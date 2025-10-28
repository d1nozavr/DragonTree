"""
DragonTree
TokenType
"""

from enum import Enum


class TokenType(Enum):
    NUMBER = "NUMBER"
    STRING = "STRING"
    IDENTIFIER = "IDENTIFIER"
    KEYWORD = "KEYWORD"

    EQUAL = "EQUAL"

    PLUS = "PLUS"
    MINUS = "MINUS"
    STAR = "STAR"
    DOUBLE_STAR = "DOUBLE_STAR"
    SLASH = "SLASH"
    DOUBLE_SLASH = "DOUBLE_SLASH"
    PERCENT = "PERCENT"
    COLON = "COLON"

    LPAREN = "LPAREN"
    RPAREN = "RPAREN"

    EOF = "EOF"
