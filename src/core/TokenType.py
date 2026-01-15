# =================================
#  DragonTree Programming Language
#  TokenType
# =================================

from enum import Enum


class TokenType(Enum):
    NUMBER = "NUMBER"
    STRING = "STRING"

    LITERAL = "LITERAL"

    OPERATOR = "OPERATOR"

    IDENTIFIER = "IDENTIFIER"
    KEYWORD = "KEYWORD"

    COLON = "COLON"

    LPAREN = "LPAREN"
    RPAREN = "RPAREN"
    LBRACE = "LBRACE"
    RBRACE = "RBRACE"

    EOF = "EOF"
