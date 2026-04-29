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
    lines = []

    try:
        try:
            file = open(arg, 'r', encoding='utf-8')
            lines = file.readlines()
        except (FileNotFoundError, PermissionError) as e:
            raise ArchiveError(str(e))

        print("---\n")
        content_original = "".join(lines)
        print(content_original.strip())
        print("\n---")

    except ArchiveError as e:
        print(f"Error opening file '{arg}': {e.message}")
        return

    finally:
        if file is not None:
            file.close()
            print(f"File '{arg}' closed.")

    print("\nTransform data:")
    print("---\n")

    data_transform = ""

    for line in lines:
        mod_line = line.rstrip('\n\r') + '#\n'

        data_transform += mod_line
        print(mod_line, end='')
    data_transform.rstrip('\n\n')

    print("\n---")

    new_file = input("Enter new file name (or empty): ")
    new_archive = None

    if new_file == '':
        print("Not saving data.")
        return

    try:
        print(f"Saving data to '{new_file}'")
        new_archive = open(new_file, 'w', encoding='utf-8')
        new_archive.write(data_transform)
        print(f"Data saved in file '{new_file}'\n")
    except Exception as e:
        print(f"Save error: {e}")
        return
    finally:
        if new_archive is not None:
            new_archive.close()


if __name__ == "__main__":
    main()
