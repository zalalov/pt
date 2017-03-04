from pt.merge import merge


if __name__ == "__main__":
    """
    * 0, 10, 20, 30, 40, 50, 60 ...
    * 0, 5, 10, 15, 20, 25, 30 ...
    * 0, 20, 40, 60, 80, 100, 120 ...

    result: 0, 0, 0, 5, 10, 10, 15, 20, 20, 20, 25, 30, 40, 40, 40 ...

    """
    l = merge(
        iter(xrange(0, 1000, 100)),
        iter(xrange(0, 1000, 1000)),
        iter(xrange(0, 1000, 1)),
        iter(xrange(0, 1000, 90)),
        iter(xrange(0, 1000, 10)),
        iter(xrange(0, 500, 50)),
        iter(xrange(0, 50, 4)),
        iter(xrange(0, 500, 15)),
        iter(xrange(0, 50, 5)),
        iter(xrange(0, 5000, 50)),
        iter(xrange(0, 100, 20)),
        iter(xrange(0, 100, 2))
    )

    print l
    print
    print
    print "Sorted" if l == sorted(l) else "Failed"
