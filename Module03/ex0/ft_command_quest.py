import sys


def ft_command_quest():
    print("=== Command Quest ===")

    print(f"Program name: {sys.argv[0]}")
    total = len(sys.argv)
    if total < 2:
        print("No arguments provided!")
    else:
        print(f"Arguments received: {total - 1}")
        for args in range(1, total):
            print(f"Argument {args}: {sys.argv[args]}")

    print(f"Total arguments: {total}")


if __name__ == "__main__":
    ft_command_quest()
