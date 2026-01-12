# =================================
#  DragonTree Programming Language
#  AST - Output Statement
# =================================

from core.AST.Node import Node


class Output(Node):
    def __init__(self, expr):
        self.expr = expr

    def evaluate(self):
        val = self.expr.evaluate()
        print(f"{val}")
