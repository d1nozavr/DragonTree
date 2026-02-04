# =================================
#  DragonTree Programming Language
#  Lexer
# =================================


from core.Token import Token
from core.TokenType import TokenType


class Lexer:
    def __init__(self, string):
        self.string = string

        self.pos = 0
        self.length = len(self.string)

        self.tokens = []

        self.KEYWORDS = {"output", "getline", "if", "else"}
        self.OPERATORS = {
            "+",
            "-",
            "*",
            "**",
            "/",
            "//",
            "%",
            "=",
            "!",
            "==",
            "!=",
            "<",
            ">",
            "<=",
            ">=",
        }
        self.IGNORED = {" ", "#", "\n", "\r", "\t"}

    def tokenize(self):
        while self.pos < self.length:
            if self._peek() in self.IGNORED:
                if self._peek() == "#":
                    while self.pos < self.length:
                        self._advance()

                else:
                    self._advance()

            elif self._peek().isdigit():
                self.__lex_number_literal()

            elif self._peek() == '"':
                self.__lex_string_literal()

            elif self._peek().isalpha():
                self.__lex_word()

            elif self._peek() in self.OPERATORS:
                self.__lex_operator()

            elif self._peek() == ":":
                self._add_token(TokenType.COLON, ":")
                self._advance()

            elif self._peek() == "(":
                self._add_token(TokenType.LPAREN, "(")
                self._advance()

            elif self._peek() == ")":
                self._add_token(TokenType.RPAREN, ")")
                self._advance()

            elif self._peek() == "{":
                self._add_token(TokenType.LBRACE, "{")
                self._advance()

            elif self._peek() == "}":
                self._add_token(TokenType.RBRACE, "}")
                self._advance()

            else:
                raise Exception(f"Unknown token '{self._peek()}' at pos {self.pos}")

        self._add_token(TokenType.EOF, "EOF")
        return self.tokens

    def __lex_number_literal(self):
        number_literal = ""

        while self.pos < self.length and (
            self._peek().isdigit() or self._peek() == "."
        ):
            number_literal += self._peek()
            self._advance()

        if "." in number_literal and number_literal.count(".") == 1:
            self._add_token(TokenType.LITERAL, float(number_literal))

        elif "." in number_literal and number_literal.count(".") > 1:
            raise SyntaxError(f"Too much '.' in '{number_literal}'")

        else:
            self._add_token(TokenType.LITERAL, int(number_literal))

    def __lex_string_literal(self):
        string_literal = ""

        self._advance()

        while self.pos < self.length:
            if self._peek() == '"':
                self._advance()
                self._add_token(TokenType.LITERAL, string_literal)
                break

            string_literal += self._peek()
            self._advance()

    def __lex_word(self):
        word = ""

        while self.pos < self.length and self._peek().isalnum():
            word += self._peek()
            self._advance()

        if word in self.KEYWORDS:
            self._add_token(TokenType.KEYWORD, word)

        else:
            self._add_token(TokenType.IDENTIFIER, word)

    def __lex_operator(self):
        op = self._peek()

        if op == "*":
            self._advance()

            if self._peek() == "*":
                op = "**"

        elif op == "/":
            self._advance()

            if self._peek() == "/":
                op = "//"

        elif op == "=":
            self._advance()

            if self._peek() == "=":
                op = "=="

        elif op == "!":
            self._advance()

            if self._peek() == "=":
                op = "!="

        elif op == "<":
            self._advance()

            if self._peek() == "=":
                op = "<="

        elif op == ">":
            self._advance()

            if self._peek() == "=":
                op = ">="

        self._add_token(TokenType.OPERATOR, op)
        self._advance()

    def _peek(self):
        return self.string[self.pos]

    def _advance(self):
        self.pos += 1

    def _add_token(self, type, value):
        self.tokens.append(Token(type, value))
