import config
from pt.fgen import fgen


def eternal_gen():
    handlers = []

    for filename in config.FGEN_FILES:
        handlers.append(fgen(filename))

    while True:
        print "\n".join([next(h).strip() for h in handlers])


if __name__ == "__main__":
    eternal_gen()
