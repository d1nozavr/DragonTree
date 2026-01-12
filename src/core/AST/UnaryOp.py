# =================================
#  DragonTree Programming Language
#  AST - Unary Operation
# =================================

from core.AST.Node import Node


class UnaryOp(Node):
    def __init__(self, op, expr):
        self.op = op
        self.expr = expr

    def evaluate(self):
        val = self.expr.evaluate()

        match self.op:
            case "+":
                return +val

            case "-":
                return -val

            case _:
                raise ValueError(f"Unknown unary operator '{self.op}'")
