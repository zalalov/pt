from os import path


def fgen(filename):
    if not path.exists(filename):
        raise IOError("File doesn't exists.")

    with open(filename, "r") as f:
        while True:
            for line in f:
                yield line

            f.seek(0)
