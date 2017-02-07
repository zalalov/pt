import heapq
from collections import Iterable


def merge(*iters):
    if not len(iters):
        raise BaseException("Iterator list should be specified.")

    for it in iters:
        if not isinstance(it, Iterable):
            raise TypeError("All the objects should be iterable.")

    return list(heapq.merge(*iters))
