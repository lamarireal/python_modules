import sys


def main():
    if len(sys.argv) != 2:
        print(f"Usage: {sys.argv[0]} <file>")
        return

    arg = sys.argv[1]

    print("=== Cyber Archives Recovery ===")
    print(f"Accessing file '{arg}'")
    file = None
    try:
        file = open(arg, 'r')

        print("---\n")
        content = file.read()
        print(content.strip())
        print("\n---")
    except (FileNotFoundError, PermissionError) as e:
        print(f"Error opening file '{arg}': {e}")
    except Exception as e:
        print(f"Error opening file '{arg}': {e}")
    finally:
        if file is not None:
            file.close()
            print(f"File '{arg}' closed.")


if __name__ == "__main__":
    main()
