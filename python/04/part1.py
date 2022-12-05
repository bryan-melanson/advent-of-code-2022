import time


def contained(vals):
    vals = [list(map(int, i)) for i in vals]
    return (vals[0][0] <= vals[1][0] and vals[0][1] >= vals[1][1]) or (vals[1][0] <= vals[0][0] and vals[1][1] >= vals[0][1])


def part1(x):
    with open(x, "r") as f:
        data = [[vals.split('-') for vals in line.split(',')]
                for line in f.read().splitlines()]
        return len(list(filter(contained, data)))
# --- 0.005724906921386719 seconds ---


test_val = 2
if part1("test") == test_val:
    start_time = time.time()
    print('Solution is {}'.format(part1("input")))
    print("--- %s seconds ---" % (time.time() - start_time))
else:
    print("Test failed")
