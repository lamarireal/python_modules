import sys


class ArchiveError(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(message)


def ft_save_data(file: str, data: str) -> bool:
    new_archive = None

    try:
        print(f"Saving data to '{file}'")
        new_archive = open(file, 'w')
        new_archive.write(data)
        new_archive.flush()
        return True
    except Exception as e:
        sys.stderr.write(f"[STDERR] Error opening file: '{file}': {e}\n")
        return False
    finally:
        if new_archive is not None:
            new_archive.close()


def main() -> None:
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
            file = open(arg, 'r')
            lines = file.readlines()
        except (FileNotFoundError, PermissionError) as e:
            raise ArchiveError(str(e))

        print("---\n")
        content_original = "".join(lines)
        print(content_original.strip())
        print("\n---")

    except ArchiveError as e:
        sys.stderr.write(f"[STDERR] Error opening file '{arg}': {e.message}\n")
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

    print("Enter new file name (or empty): ", end='', flush=True)
    new_file = sys.stdin.readline()
    new_file = new_file.rstrip('\n').strip()

    if new_file == '':
        print("Not saving data.")
        return
    else:
        if ft_save_data(new_file, data_transform) is True:
            print(f"Data saved in file '{new_file}'\n")
        else:
            print("Data not saved.")



if __name__ == "__main__":
    main()
