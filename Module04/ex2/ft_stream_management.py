import sys


def ft_save_data(file_path: str, data: str) -> bool:
    new_archive = None
    try:
        print(f"Saving data to '{file_path}'")
        new_archive = open(file_path, 'w')
        new_archive.write(data)
        new_archive.flush()
        return True
    except Exception as e:
        sys.stderr.write(f"[STDERR] Error opening file '{file_path}': {e}\n")
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
        file = open(arg, 'r')
        lines = file.readlines()

        print("---\n")
        content_original = "".join(lines)
        print(content_original.strip())
        print("\n---")

    except (FileNotFoundError, PermissionError) as e:
        sys.stderr.write(f"[STDERR] Error opening file '{arg}': {e}\n")
        return
    except Exception as e:
        sys.stderr.write(f"[STDERR] Error opening file '{arg}': {e}\n")
        return
    finally:
        if file is not None:
            file.close()
            print(f"File '{arg}' closed.")

    print("\nTransform data:")
    print("---")

    transformed_content = ""
    for line in lines:
        mod_line = line.rstrip('\n') + '#\n'
        transformed_content += mod_line
        sys.stdout.write(mod_line)
        sys.stdout.flush()

    print("---")

    sys.stdout.write("Enter new file name (or empty): ")
    sys.stdout.flush()
    new_file = sys.stdin.readline().strip()

    if not new_file:
        print("Not saving data.")
        return

    if ft_save_data(new_file, transformed_content):
        print(f"Data saved in file '{new_file}'.")
    else:
        print("Data not saved.")


if __name__ == "__main__":
    main()
