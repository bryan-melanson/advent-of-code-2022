import time
import re


def get_idx(x):
    matches = re.finditer(
        r'(.)(?!\1)(.)(?!\1|\2)(.)(?!\1|\2|\3)(.)(.){3}', x)
    for match in matches:
        start = match.span()[0]
        if start >= 3:
            return start + 4


def part1(x):
    with open(x, "r") as f:
        data = f.read().splitlines()
        return (get_idx(data[0]))

# --- 0.00022721290588378906 seconds ---


test_val = 7
if part1("test") == test_val:
    start_time = time.time()
    print('Solution is {}'.format(part1("input")))
    print("--- %s seconds ---" % (time.time() - start_time))
else:
    print("Test failed")
