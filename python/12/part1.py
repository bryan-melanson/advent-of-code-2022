import time
from collections import deque


def part1(x):
    with open(x, "r") as f:
        data = [list(line) for line in f.read().splitlines()]
        for row in range(len(data)):
            for col in range(len(data[0])):
                if data[row][col] == "S":
                    start = (row, col)
                if data[row][col] == "E":
                    end = (row, col)
                    data[row][col] = 'z'

        queue = deque([(start[0], start[1], 0)])
        visited = set()

        while queue:
            row, col, val = queue.popleft()
            if (row, col) == end:
                return val
            if (row, col) in visited:
                continue
            visited.add((row, col))
            for r, c in [(-1, 0), (0, -1), (1, 0), (0, 1)]:
                if (len(data) > row+r >= 0 and len(data[0]) > col+c >= 0):
                    if ((row, col) == start) or (ord(data[row+r][col+c]) <= ord(data[row][col])+1):
                        queue.append((row+r, col+c, val+1))
        return val

# --- 0.055726051330566406 seconds ---


test_val = 31
if part1("test") == test_val:
    start_time = time.time()
    print('Solution is {}'.format(part1("input")))
    print("--- %s seconds ---" % (time.time() - start_time))
else:
    print("Test failed")