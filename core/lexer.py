"""
DragonTree
Lexical analyzer
"""

import re
from collections import namedtuple

Token = namedtuple("Token", ["type", "value"])


class Lexer:
    KEYWORDS = {"output"}

    TOKEN_SPECIFICATION = [
        ("NUMBER", r"\d+(\.\d*)?"),
        ("ID", r"[a-zA-Z_][a-zA-Z_0-9]*"),
        ("OP", r"[:]=|==|!=|<=|>=|[+\-*/=<>]"),
        ("SKIP", r"[ \t+]"),
        ("NEWLINE", r"\n"),
        ("LPAREN", r"\("),
        ("RPAREN", r"\)"),
        ("MISMATCH", r"."),
    ]

    def __init__(self):
        self.tok_regex = "|".join(
            f"(?P<{name}>{pattern})" for name, pattern in self.TOKEN_SPECIFICATION
        )

    def lex(self, string):
        for match in re.finditer(self.tok_regex, string):
            kind = match.lastgroup
            value = match.group()

            match kind:
                case "NUMBER":
                    yield Token(kind, float(value) if "." in value else int(value))

                case "ID":
                    yield Token(
                        value.upper() if value in self.KEYWORDS else "ID", value
                    )

                case "NEWLINE" | "SKIP":
                    continue

                case "OP" | "LPAREN" | "RPAREN":
                    yield Token(kind, value)

                case "MISMATCH":
                    raise SyntaxError(f"Unexpected character: {value!r}")
