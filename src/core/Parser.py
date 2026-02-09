# =================================
#  DragonTree Programming Language
#  Parser
# =================================

from core.AST.Assignment import Assignment
from core.AST.BinOp import BinOp
from core.AST.Identifier import Identifier
from core.AST.Literal import Literal
from core.AST.Output import Output
from core.AST.UnaryOp import UnaryOp
from core.TokenType import TokenType


class Parser:
    def __init__(self, env):
        self.env = env

        self.tokens = None

        self.pos = 0
        self.length = None

        self.if_statement = False
        self.if_statement_result = False

    def parse(self, tokens):
        self.tokens = tokens
        self.length = len(tokens)
        self.pos = 0

        if self._peek().type != TokenType.EOF:
            return self.__statement()

    def __statement(self):
        token = self._peek()

        match token.type:
            case TokenType.KEYWORD:
                match token.value:
                    case "output":
                        self._advance()

                        if self._peek().type == TokenType.COLON:
                            self._advance()

                            rhs = self.__expr()

                            return Output(rhs)

                        raise SyntaxError(f"Need ':' after 'output' at pos {self.pos}")

                    case "if":
                        self._advance()

                        self._expect(TokenType.LPAREN)
                        lhs = self.__expr().evaluate()
                        self._expect(TokenType.RPAREN)

                        if self._peek().type == TokenType.LBRACE:
                            self._advance()

                            rhs = self.__statement()

                            self._expect(TokenType.RBRACE)

                            self.if_statement = True
                            if lhs:
                                self.if_statement_result = True
                                return rhs.evaluate()

                            else:
                                self.if_statement_result = False
                                # return None

                        else:
                            raise SyntaxError(
                                "Statement must be in '{}' at pos " + str(self.pos)
                            )

                    case "else":
                        if self.if_statement and not self.if_statement_result:
                            self._advance()

                            if self._peek().type == TokenType.LBRACE:
                                self._advance()

                                rhs = self.__statement()

                                self._expect(TokenType.RBRACE)

                                return rhs.evaluate()

                            else:
                                raise SyntaxError(
                                    "Statement must be in '{}' at pos " + str(self.pos)
                                )

            case TokenType.IDENTIFIER:
                lhs = token.value
                self._advance()

                token = self._peek()
                if token.type == TokenType.OPERATOR and token.value == "=":
                    self._advance()

                    token = self._peek()
                    if token.type == TokenType.KEYWORD and token.value == "getline":
                        rhs = input()
                        return Assignment(self.env, lhs, rhs)

                    rhs = self.__expr()
                    return Assignment(self.env, lhs, rhs)

                raise NameError(f"Unknown name '{lhs}'")

            case _:
                raise SyntaxError("Invalid syntax")

    def __expr(self):
        lhs = self.__term()

        while True:
            token = self._peek()

            if token.type == TokenType.OPERATOR and token.value in (
                "+",
                "-",
                "==",
                "!=",
                "<",
                ">",
                "<=",
                ">=",
            ):
                op = token.value
                self._advance()

                rhs = self.__term()

                lhs = BinOp(lhs, op, rhs)

                continue

            break

        return lhs

    def __term(self):
        lhs = self.__factor()

        while True:
            token = self._peek()

            if token.type == TokenType.OPERATOR and token.value in (
                "*",
                "/",
                "//",
                "%",
            ):
                op = token.value
                self._advance()

                rhs = self.__factor()

                lhs = BinOp(lhs, op, rhs)

                continue

            break

        return lhs

    def __factor(self):
        token = self._peek()

        if token.type == TokenType.OPERATOR and token.value in ("+", "-"):
            op = token.value
            self._advance()

            expr = self.__factor()
            return UnaryOp(op, expr)

        return self.__power()

    def __power(self):
        lhs = self.__atom()

        token = self._peek()
        if token.type == TokenType.OPERATOR and token.value == "**":
            op = "**"
            self._advance()

            rhs = self.__factor()

            lhs = BinOp(lhs, op, rhs)

        return lhs

    def __atom(self):
        token = self._peek()

        match token.type:
            case TokenType.LITERAL:
                self._advance()
                return Literal(token.value)

            case TokenType.IDENTIFIER:
                self._advance()
                return Identifier(self.env, token.value)

            case TokenType.LPAREN:
                self._advance()

                rhs = self.__expr()

                self._expect(TokenType.RPAREN)

                return rhs

            case _:
                raise RuntimeError(f"Unexpected token '{token.value}', pos {self.pos}")

    def _peek(self):
        return self.tokens[self.pos]

    def _advance(self):
        self.pos += 1

    def _expect(self, type):
        if self._peek().type == type:
            self._advance()

        else:
            raise ValueError(f"Expected '{type}', got '{self._peek().type}'")
