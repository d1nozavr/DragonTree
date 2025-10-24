"""
DragonTree
Ast
"""


class NumberNode:
    def __init__(self, value):
        self.value = value

    def evaluate(self):
        return self.value


class BinOpNode:
    def __init__(self, left, operation, right):
        self.left = left
        self.operation = operation
        self.right = right

    def evaluate(self):
        match self.operation:
            case "+":
                return self.left + self.right

            case "-":
                if self.left:
                    return self.left - self.right

                return -self.right

            case "*":
                return self.left * self.right

            case "/":
                return self.left / self.right

            case _:
                return f"Uknown operator: '{self.operation}'"
