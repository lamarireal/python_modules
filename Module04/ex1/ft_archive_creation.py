import sys


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
        file = open(arg, 'r')
        lines = file.readlines()

        print("---\n")
        content_original = "".join(lines)
        print(content_original.strip())
        print("\n---")

    except (FileNotFoundError, PermissionError) as e:
        print(f"Error opening file '{arg}': {e}")
        return
    except Exception as e:
        print(f"Error opening file '{arg}': {e}")
        return

    finally:
        if file is not None:
            file.close()
            print(f"File '{arg}' closed.")

    print("\nTransform data:")
    print("---\n")

    data_transform = ""

    for line in lines:
        mod_line = line.rstrip('\n') + '#\n'

        data_transform += mod_line
        print(mod_line, end='')
    data_transform = data_transform.rstrip('\n')

    print("\n---")

    new_file = input("Enter new file name (or empty): ")
    new_archive = None

    if new_file == '':
        print("Not saving data.")
        return

    try:
        print(f"Saving data to '{new_file}'")
        new_archive = open(new_file, 'w')
        new_archive.write(data_transform + '\n')
        print(f"Data saved in file '{new_file}'.")
    except Exception as e:
        print(f"Error opening file: '{new_file}': {e}")
    finally:
        if new_archive is not None:
            new_archive.close()


if __name__ == "__main__":
    main()
