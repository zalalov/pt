def to_seconds(value):
    if not isinstance(value, basestring):
        raise ValueError("Invalid value.")

    convert_map = {
        "s": " 1 ",
        "m": " 60 ",
        "h": " 3600 "
    }

    value = reduce(lambda x, y: x.replace(*y), convert_map.iteritems(), value)

    try:
        return int(reduce(lambda x, y: float(x) * float(y), value.split()))
    except ValueError:
        raise ValueError("Invalid value.")
