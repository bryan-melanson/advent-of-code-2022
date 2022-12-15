import time
import ast


def check(a, b):
    VALID = 1
    INVALID = -1
    NA = 0
    for idx in range(max(len(a), len(b))):
        if idx >= len(a):
            return VALID
        if idx >= len(b):
            return NA
        l, r = a[idx], b[idx]
        valid = INVALID
        if type(l) == int and type(r) == int:
            if l < r:
                valid = VALID
            elif l > r:
                valid = NA
            else:
                valid = INVALID
                continue
        elif type(l) == list and type(r) == list:
            valid = check(l, r)
        elif type(l) == list and type(r) == int:
            valid = check(l, [r])
        elif type(l) == int and type(r) == list:
            valid = check([l], r)
        if valid != INVALID:
            return valid
    return INVALID


def part2(x):
    with open(x, "r") as f:
        pairs = [ast.literal_eval(pair)
                 for pair in f.read().splitlines() if pair != '']
        x, y = 1, 2
        for i in range(len(pairs)):
            if (check(pairs[i], [[2]])):
                x += 1
            if (check(pairs[i], [[6]])):
                y += 1
        return x*y

# --- 0.06795477867126465 seconds ---


test_val = 140
if part2("test") == test_val:
    start_time = time.time()
    print('Solution is {}'.format(part2("input")))
    print("--- %s seconds ---" % (time.time() - start_time))
else:
    print("Test failed")
