import sys


class ArchiveError(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(message)


def main():
    if len(sys.argv) != 2:
        print(f"Usage: {sys.argv[0]} <file>")
        return

    arg = sys.argv[1]

    print("=== Cyber Archives Recovery & Preservation ===")
    print(f"Accessing file '{arg}'")
    file = None
    try:
        try:
            file = open(arg, 'r', encoding='utf-8')
        except (FileNotFoundError, PermissionError) as e:
            raise ArchiveError(str(e))

        print("---")
        content = file.read()
        print(content.strip())
        print("---")

    except ArchiveError as e:
        print(f"Error opening file '{arg}': {e.message}")

    finally:
        if file is not None:
            file.close()
            print(f"File '{arg}' closed.")

    print("\nTransform data:")


if __name__ == "__main__":
    main()
