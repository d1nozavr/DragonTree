# =================================
#  DragonTree Programming Language
# =================================

from pathlib import Path
from core.Interpreter import Interpreter


def main():
    print("DragonTree v0.0.2-alpha")  # :TODO: Remove this line in non-alpha version
    print()

    file_path = Path(input("Path to 'file'.dt → "))

    try:
        if not file_path.is_file():
            raise FileExistsError(f"'{file_path}' not a file or not exist")

        if not file_path.exists():
            raise FileNotFoundError(f"File '{file_path}' not found")

        lines = file_path.read_text(encoding="utf-8").splitlines()

        for line in lines:
            interpreter.interpret(line)

    except FileExistsError as FER:
        print("Error 'FileExistsError':")
        print(f"  → {FER}")

    except FileNotFoundError as FNFE:
        print("Error 'FileNotFoundError':")
        print(f"  → {FNFE}")


if __name__ == "__main__":
    interpreter = Interpreter()
    main()
