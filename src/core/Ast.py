# =================================
#  DragonTree Programming Language
#  File: Ast.py
# =================================


class ASTNode:
    def evaluate(self):
        raise NotImplementedError("NotImplement 'ASTNode'")


class IntLiteral(ASTNode):
    def __init__(self, value):
        self.value = value

    def evaluate(self):
        return self.value


class FloatLiteral(ASTNode):
    def __init__(self, value):
        self.value = value

    def evaluate(self):
        return self.value


class StringLiteral(ASTNode):
    def __init__(self, value):
        self.value = value

    def evaluate(self):
        return self.value


class Identifier(ASTNode):
    def __init__(self, env, name):
        self.env = env
        self.name = name

    def evaluate(self):
        if self.name in self.env:
            return self.env[self.name]

        raise NameError(f"Name '{self.name}' is not defined")


class BinaryOperation(ASTNode):
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
                return lval // rval

            case "%":
                return lval % rval

            case "**":
                return lval**rval

            case _:
                raise ValueError(f"Unknown operator '{self.op}'")


class UnaryOperation(ASTNode):
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


class Assign(ASTNode):
    def __init__(self, env, name, expr):
        self.env = env

        self.name = name
        self.expr = expr

    def evaluate(self):
        val = self.expr.evaluate()
        self.env[self.name] = val


class Output(ASTNode):
    def __init__(self, expr):
        self.expr = expr

    def evaluate(self):
        val = self.expr.evaluate()
        print(f"{val}")
