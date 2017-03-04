import bisect
from collections import Iterable


def merge(*iters):
    if not len(iters):
        raise BaseException("Iterator list should be specified.")

    for it in iters:
        if not isinstance(it, Iterable):
            raise TypeError("All the objects should be iterable.")

    result = []
    iterator_list = iters[:]
    d = dict()

    # fill by first values
    for i in iterator_list:
        try:
            value = next(i)
        except StopIteration:
            continue

        if value in d:
            d[value].append(i)
        else:
            d[value] = [i]

    values = sorted(d.keys())

    while len(d):
        # minimal value in list has zero index
        v = values[0]

        # get necessary iterator
        it = d[v][0]
        iter_end = False

        try:
            next_value = next(it)
        except StopIteration:
            iter_end = True

        d[v].remove(it)

        # if there are no iterators with
        # that value - delete it from list
        if not len(d[v]):
            del d[v]
            values.remove(v)

        # if iterator not at the end,
        # continue work with one
        if not iter_end:
            if next_value in d:
                d[next_value].append(it)
            else:
                d[next_value] = [it]

            if next_value not in values:
                bisect.insort(values, next_value)

        # add value to ordered result list
        result.append(v)

    return result


