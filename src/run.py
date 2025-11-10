# =================================
#  DragonTree Programming Language
#  File: run.py
# =================================

from os import name, system
from pathlib import Path
from sys import exit

from core.Interpreter import Interpreter


def clear_console():
    if name == "nt":
        system("cls")

    else:
        system("clear")


if __name__ == "__main__":
    interpreter = Interpreter(debug=False)

    print("DragonTree v0.0.2-alpha")
    print()
    print("Select Interpreter Mode:")
    print("  1. Interactive Mode (enter code line by line)")
    print("  2. File Mode (run code from a file)")
    print()

    mode = int(input("> "))

    clear_console()

    match mode:
        case 1:
            print("DragonTree v0.0.2-alpha")
            print()

            while True:
                line = input(">>> ")

                if line == "quit" or line == "exit":
                    break

                elif line == "clear":
                    clear_console()

                    print("DragonTree v0.0.2-alpha")
                    print()

                else:
                    try:
                        interpreter.interpret(line)

                    except Exception as e:
                        print(f"Error '{type(e).__name__}':")
                        print(f"  ↓ File '-', line {interpreter.line}")
                        print()
                        print(f"  ↓ {interpreter.string.strip()}")
                        print(f"  ↓ {'↑' * len(interpreter.string.strip())}")
                        print()
                        print(f"  → {e}")

        case 2:
            print("DragonTree v0.0.2-alpha")
            print()

            file_path = Path(input("Path to file → "))

            clear_console()

            print("DragonTree v0.0.2-alpha")
            print()

            try:
                if not file_path.is_file():
                    raise FileExistsError(
                        f"'{file_path}' is not a file or does not exist"
                    )

                if not file_path.exists():
                    raise FileNotFoundError(f"File '{file_path}' was not found")

                if file_path.suffix != ".dt":
                    raise ValueError(
                        f"Invalid file suffix '{file_path.suffix}', expected '.dt'"
                    )

                lines = file_path.read_text(encoding="utf-8").splitlines()

                for line in lines:
                    interpreter.interpret(line)

            except FileExistsError as fer:
                print("Error 'FileExistsError':")
                print(f"  → {fer}")

            except FileNotFoundError as fnfe:
                print("Error 'FileNotFoundError':")
                print(f"  → {fnfe}")

            except Exception as e:
                print(f"Error '{type(e).__name__}':")
                print(f"  ↓ File '{file_path}', line {interpreter.line}")
                print()
                print(f"  ↓ {interpreter.string.strip()}")
                print(f"  ↓ {'↑' * len(interpreter.string.strip())}")
                print()
                print(f"  → {e}")

        case _:
            exit(0)
