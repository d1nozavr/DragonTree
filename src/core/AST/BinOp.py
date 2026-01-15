# =================================
#  DragonTree Programming Language
#  AST - Binary Operation
# =================================

from core.AST.Node import Node


class BinOp(Node):
    def __init__(self, lhs, op, rhs):
        self.lhs = lhs
        self.op = op
        self.rhs = rhs

    def evaluate(self):
        lval = self.lhs.evaluate()
        rval = self.rhs.evaluate()

        match self.op:
            case "+":
                return lval + rval

            case "-":
                return lval - rval

            case "*":
                return lval * rval

            case "/":
                if rval == 0:
                    raise ZeroDivisionError("Division by zero")

                return lval / rval

            case "//":
                if rval == 0:
                    raise ZeroDivisionError("Division by zero")

                return lval // rval

            case "%":
                return lval % rval

            case "**":
                return lval**rval

            case "==":
                return lval == rval

            case "!=":
                return lval != rval

            case "<":
                return lval < rval

            case "<=":
                return lval <= rval

            case ">":
                return lval > rval

            case ">=":
                return lval >= rval

            case _:
                raise ValueError(f"Unknown operator '{self.op}'")
