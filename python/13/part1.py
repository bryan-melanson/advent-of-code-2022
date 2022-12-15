import time
from ast import literal_eval

VALID, INVALID, NA = 1, -1, 0


def check(a, b):
    valid = NA
    for idx in range(max(len(a), len(b))):
        if idx >= len(a):
            return VALID
        if idx >= len(b):
            return INVALID
        l, r = a[idx], b[idx]
        if type(l) == int and type(r) == int:
            if l < r:
                valid = VALID
            elif l > r:
                valid = INVALID
            else:
                continue
        elif type(l) == list and type(r) == list:
            valid = check(l, r)
        elif type(l) == list and type(r) == int:
            valid = check(l, [r])
        elif type(l) == int and type(r) == list:
            valid = check([l], r)
        if valid != NA:
            return valid
    return valid


def part1(x):
    with open(x, "r") as f:
        pairs = [pair.splitlines() for pair in f.read().split('\n\n')]
        count, idx = 0, 1
        for pair in pairs:
            a = literal_eval(pair[0])
            b = literal_eval(pair[1])
            valid = check(a, b)
            if (valid == VALID):
                count += idx
            idx += 1
    return count

# --- 0.04009699821472168 seconds ---


test_val = 13
if part1("test") == test_val:
    start_time = time.time()
    print('Solution is {}'.format(part1("input")))
    print("--- %s seconds ---" % (time.time() - start_time))
else:
    print("Test failed")
