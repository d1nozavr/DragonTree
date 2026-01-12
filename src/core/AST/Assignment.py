# =================================
#  DragonTree Programming Language
#  AST - Assignment Statement
# =================================

from core.AST.Node import Node


class Assignment(Node):
    def __init__(self, env, name, expr):
        self.env = env

        self.name = name
        self.expr = expr

    def evaluate(self):
        val = self.expr.evaluate()
        self.env[self.name] = val
