def frequencies(ns):
    result = {}
    for n in ns:
        if n not in result:
            result[n] = 0
        result[n] += 1
    return result


def second(pair):
    return pair[1]


def mode(ns):
    fs = frequencies(ns)
    return max(fs.items(), key=second)[0]

# Alternative using lambda's
def mode2(ns):
    return max(frequencies(ns), key=lambda pair: pair[1])[0]