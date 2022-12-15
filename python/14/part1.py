import time


def part1(x):
    with open(x, "r") as f:
        data = [blocks.splitlines() for blocks in f.read().split('\n\n')]
        print(data)


test_val = 13
if part1("test") == test_val:
    start_time = time.time()
    print('Solution is {}'.format(part1("input")))
    print("--- %s seconds ---" % (time.time() - start_time))
else:
    print("Test failed")