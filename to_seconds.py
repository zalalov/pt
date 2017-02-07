from sys import argv
from pt.delta import to_seconds


if __name__ == "__main__":
    if len(argv) < 2:
        raise IndexError("Invalid input.")

    print to_seconds(argv[1])
