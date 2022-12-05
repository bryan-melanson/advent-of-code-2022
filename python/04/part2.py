import time


def overlap(vals):
    vals = [list(map(int, i)) for i in vals]
    return ((vals[0][0] <= vals[1][1]
             and vals[0][1] >= vals[1][0]) or (vals[1][0] <= vals[0][1] and vals[1][1] >= vals[0][0]))


def part2(x):
    with open(x, "r") as f:
        data = [[vals.split('-') for vals in line.split(',')]
                for line in f.read().splitlines()]
        return len(list(filter(overlap, data)))
# --- 0.005255222320556641 seconds ---


test_val = 4
if part2("test") == test_val:
    start_time = time.time()
    print('Solution is {}'.format(part2("input")))
    print("--- %s seconds ---" % (time.time() - start_time))
else:
    print("Test failed")
