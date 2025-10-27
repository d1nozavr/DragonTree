"""
DragonTree
Ast
"""


class NumberNode:
    def __init__(self, value):
        if isinstance(value, int):
            self.value = int(value)

        elif isinstance(value, float):
            self.value = float(value)

        else:
            raise ValueError(
                f"Type '{type(value).__name__}' is not number ('int', 'float')"
            )

    def evaluate(self):
        return self.value


class StringNode:
    def __init__(self, value):
        self.value = value

    def evaluate(self):
        return self.value


class VariableNode:
    def __init__(self, value):
        self.value = value

    def evaluate(self):
        if isinstance(self.value, (int, float)):
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
