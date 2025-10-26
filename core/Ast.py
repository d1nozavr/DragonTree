"""
DragonTree
Ast
"""


class NumberNode:
    def __init__(self, value):
        try:
            self.value = int(value)

        except ValueError:
            raise ValueError(f"Type 'int' != Type '{type(value).__name__}'")

    def evaluate(self):
        return self.value


class StringNode:
    def __init__(self, value):
        self.value = value

    def evaluate(self):
        return f"{self.value}"


class VariableNode:
    def __init__(self, value):
        self.value = value

    def evaluate(self):
        if isinstance(self.value, int):
            return NumberNode(self.value).evaluate()

        return StringNode(self.value).evaluate()


class BinOpNode:
    def __init__(self, left, operation, right):
        self.left = left
        self.operation = operation
        self.right = right

    def evaluate(self):
        match self.operation:
            case "+":
                if self.left:
                    return self.left + self.right

                return self.right

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


class OutputNode:
    def __init__(self, value):
        self.value = value

    def evaluate(self):
        print(f"{self.value}")
