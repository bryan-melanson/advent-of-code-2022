import time
import re


def get_idx(x):
    match = re.search(
        r'(.)(?!\1)(.)(?!\1|\2)(.)(?!\1|\2|\3)(.)(.){3}', x)
    return match.span()[0] + 4


def part1(x):
    with open(x, "r") as f:
        data = f.read().splitlines()
        return (get_idx(data[0]))

# --- 0.003361940383911133 seconds ---


test_val = 7
if part1("test") == test_val:
    start_time = time.time()
    print('Solution is {}'.format(part1("input")))
    print("--- %s seconds ---" % (time.time() - start_time))
else:
    print("Test failed")
