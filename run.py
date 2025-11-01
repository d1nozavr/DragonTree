"""
DragonTree
Run
"""

from pathlib import Path

from core.Interpreter import Interpreter

if __name__ == "__main__":
    interpreter = Interpreter(debug=False)

    print("DragonTree v0.0.2-alpha")
    print()
    print("Select interpreter mode:")
    print("  1. Single")
    print("  2. File")

    mode = int(input("> "))

    match mode:
        case 1:
            while True:
                line = input(">>> ")

                if line == "break":
                    break

                interpreter.interpret(line)

        case 2:
            path = input("'file'.dt → ")
            file_path = Path(path)

            try:
                if not file_path.is_file():
                    raise Exception(f"'{path}' is not file")

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
                print(f"  → {e}")

        case _:
            raise RuntimeError("Unknown interpreter mode")
