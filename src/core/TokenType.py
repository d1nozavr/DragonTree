# =================================
#  DragonTree Programming Language
#  TokenType
# =================================

from enum import Enum


class TokenType(Enum):
    INT_LITERAL = "INT_LITERAL"
    FLOAT_LITERAL = "FLOAT_LITERAL"
    STRING_LITERAL = "STRING_LITERAL"

    LITERAL = "LITERAL"

    OPERATOR = "OPERATOR"

    IDENTIFIER = "IDENTIFIER"

    KEYWORD = "KEYWORD"

    NUMBER = "NUMBER"
    STRING = "STRING"

    COLON = "COLON"

    LPAREN = "LPAREN"
    RPAREN = "RPAREN"
    LBRACE = "LBRACE"
    RBRACE = "RBRACE"

    EOF = "EOF"
