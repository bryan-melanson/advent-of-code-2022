import time
from ast import literal_eval
from functools import cmp_to_key

VALID, INVALID, NA = 1, -1, 0


def check(a, b):
    valid = NA
    for idx in range(max(len(a), len(b))):
        if idx >= len(a):
            return VALID
        if idx >= len(b):
            return INVALID
        l, r = a[idx], b[idx]
        valid = NA
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


def swap(A, i, j):
    temp = A[i]
    A[i] = A[j]
    A[j] = temp


def bubbleSort(A):
    for k in range(len(A) - 1):
        for i in range(len(A) - 1 - k):
            if check(A[i], A[i + 1]) == INVALID:
                swap(A, i, i + 1)


# def part2(x):
#     with open(x, "r") as f:
#         pairs = [literal_eval(pair)
#                  for pair in f.read().splitlines() if pair != '']
#         pairs.append([[2]])
#         pairs.append([[6]])
#         bubbleSort(pairs)
#         idx_l, idx_r = 1, 1
#         for i in range(len(pairs)):
#             if pairs[i] == [[2]]:
#                 idx_l = i+1
#             if pairs[i] == [[6]]:
#                 idx_r = i+1
#         return idx_l * idx_r

# --- 0.49914121627807617 seconds - --


def part2(x):
    with open(x, "r") as f:
        pairs = [literal_eval(pair)
                 for pair in f.read().splitlines() if pair != '']
        x, y = 1, 2
        for i in range(len(pairs)):
            if (check(pairs[i], [[2]]) == VALID):
                x += 1
            if (check(pairs[i], [[6]]) == VALID):
                y += 1
        return x*y

# --- 0.0273067951202 seconds ---


test_val = 140
if part2("test") == test_val:
    start_time = time.time()
    print('Solution is {}'.format(part2("input")))
    print("--- %s seconds ---" % (time.time() - start_time))
else:
    print("Test failed")
