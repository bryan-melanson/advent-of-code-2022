from time import time

def part2(x):
    with open(x, "r") as f:
        return f.read().splitlines()


test_val = 0
if part2("test") == test_val:
    start_time = time()
    print('Solution is {}'.format(part2("input")))
    print("--- %s seconds ---" % (time.time() - start_time))
else:
    print("Test failed")
