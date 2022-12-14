import time
from collections import deque


def checkPath(start, end, nodes):
    val = 0
    queue = deque([(start[0], start[1], val)])
    visited = set()
    while queue:
        row, col, val = queue.popleft()
        if (row, col) == end:
            return val
        if (row, col) in visited:
            continue
        visited.add((row, col))
        for r, c in [(-1, 0), (0, -1), (1, 0), (0, 1)]:
            if (len(nodes) > row+r >= 0 and len(nodes[0]) > col+c >= 0):
                if (ord(nodes[row+r][col+c]) <= ord(nodes[row][col])+1):
                    queue.append((row+r, col+c, val+1))
    return 999


def part2(col):
    with open(col, "r") as f:
        data = [list(line) for line in f.read().splitlines()]
        start, end = (0,0)
        starts, vals = [],[]
        for row in range(len(data)):
            for col in range(len(data[0])):
                if data[row][col] == 'S':
                    data[row][col] = 'a'
                    starts.append((row, col))
                if data[row][col] == 'a':
                    starts.append((row, col))
                if data[row][col] == "E":
                    end = (row, col)
                    data[row][col] = 'z'
        for start in starts:
            vals.append(checkPath(start, end, data))
        return(min(vals))
# --- 2.41329789162 seconds ---

test_val = 29
if part2("test") == test_val:
    start_time = time.time()
    print('Solution is {}'.format(part2("input")))
    print("--- %s seconds ---" % (time.time() - start_time))
else:
    print("Test failed")
