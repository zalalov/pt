from pt.merge import merge


if __name__ == "__main__":
    """
    * 0, 10, 20, 30, 40, 50, 60 ...
    * 0, 5, 10, 15, 20, 25, 30 ...
    * 0, 20, 40, 60, 80, 100, 120 ...

    result: 0, 0, 0, 5, 10, 10, 15, 20, 20, 20, 25, 30, 40, 40, 40 ...

    """
    print merge(
        iter(xrange(0, 1000, 10)),
        iter(xrange(0, 50, 5)),
        iter(xrange(0, 100, 20))
    )
    print merge(None)
