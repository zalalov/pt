import heapq


def merge(*iters):
    return list(heapq.merge(*iters))
