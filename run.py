"""
DragonTree
Run
"""

from pathlib import Path

from core.Interpreter import Interpreter

if __name__ == "__main__":
    interpreter = Interpreter(debug=False)

    path = input("'file'.dt → ")
    file_path = Path(path)

    try:
        if not file_path.exists():
            raise FileNotFoundError(f"File '{path}' was not found.")

        if file_path.suffix != ".dt":
            raise ValueError(
                f"Invalid file suffix '{file_path.suffix}'. Expected '.dt'."
            )

        with open(file_path, "r", encoding="utf-8") as file:
            for line in file:
                interpreter.interpret(line)

    except Exception as e:
        print(f"Error '{type(e).__name__}':")
        print(f"  {e}")
