import time


def overlap(vals):
    return ((int(vals[0][0]) <= int(vals[1][1])
             and int(vals[0][1]) >= int(vals[1][0])) or (int(vals[1][0]) <= int(vals[0][1])
                                                         and int(vals[1][1]) >= int(vals[0][0])))


def part2(x):
    with open(x, "r") as f:
        data = [[vals.split('-') for vals in line.split(',')]
                for line in f.read().splitlines()]
        return len(list(filter(overlap, data)))


test_val = 4
if part2("test") == test_val:
    start_time = time.time()
    print('Solution is {}'.format(part2("input")))
    print("--- %s seconds ---" % (time.time() - start_time))
else:
    print("Test failed")
