import time


def part2(x):
    with open(x, "r") as f:
        blocks = f.read().split('\n\n')
        print(blocks)


test_val = 13
if part2("test") == test_val:
    start_time = time.time()
    print('Solution is {}'.format(part2("input")))
    print("--- %s seconds ---" % (time.time() - start_time))
else:
    print("Test failed")