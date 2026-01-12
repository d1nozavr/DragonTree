# =================================
#  DragonTree Programming Language
#  AST - Literal
# =================================


from core.AST.Node import Node


class Literal(Node):
    def __init__(self, value):
        self.value = value

    def evaluate(self):
        return self.value
