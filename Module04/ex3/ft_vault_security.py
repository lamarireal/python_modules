import sys


def secure_archive(filename: str, mode: str = 'r', content: str = "") -> tuple[bool, str]:
    try:
        if mode == 'r':
            with open(filename, 'r', encoding='utf-8') as f:
                data = f.read()
            return (True, data)
        
        elif mode == 'w':
            with open(filename, 'w', encoding='utf-8') as f:
                f.write(content)
            return (True, "Content successfully written to file")
        
        else:
            return (False, f"Unsupported mode: {mode}")

    except Exception as e:
        return (False, str(e))


def main():
    print("=== Cyber Archives Security ===")

    print("Using 'secure_archive' to read from a nonexistent file:")
    print(secure_archive('/not/existing/file', 'r'))

    print("\nUsing 'secure_archive' to read from an inaccessible file:")
    print(secure_archive('/etc/master.passwd', 'r'))

    print("\nUsing 'secure_archive' to read from a regular file:")
    secure_archive('ancient_fragment.txt', 'w', 
                   "[FRAGMENT 001] Digital preservation protocols established 2087\n"
                   "[FRAGMENT 002] Knowledge must survive the entropy wars\n"
                   "[FRAGMENT 003] Every byte saved is a victory against oblivion\n")
    print(secure_archive('ancient_fragment.txt', 'r'))

    print("\nUsing 'secure_archive' to write previous content to a new file:")
    result_read = secure_archive('ancient_fragment.txt', 'r')
    if result_read[0]:
        print(secure_archive('new_vault_entry.txt', 'w', result_read[1]))


if __name__ == "__main__":
    main()
