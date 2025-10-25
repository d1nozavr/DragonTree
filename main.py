"""
DragonTree
Runner
"""

from core.Interpreter import Interpreter

if __name__ == "__main__":
    interpreter = Interpreter()

    file_path = input("'file'.dt → ")
    file = open(file_path, "r").readlines()

    for line in file:
        if line:
            interpreter.interpret(line)
