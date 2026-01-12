# =================================
#  DragonTree Programming Language
#  AST - Identifier
# =================================

from core.AST.Node import Node


class Identifier(Node):
    def __init__(self, env, name):
        self.env = env
        self.name = name

    def evaluate(self):
        if self.name in self.env:
            return self.env[self.name]

        raise NameError(f"Name '{self.name}' is not defined")
