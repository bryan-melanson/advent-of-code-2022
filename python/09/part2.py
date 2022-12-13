import time


def move_knot(tail, rel):
    moves = dict({(-2, -2): (-1, -1),
                  (-2, -1): (-1, -1),
                  (-2, 0): (-1, 0),
                  (-2, 1): (-1, 1),
                  (-2, 2): (-1, 1),
                  (2, -2): (1, -1),
                  (2, -1): (1, -1),
                  (2, 0): (1, 0),
                  (2, 1): (1, 1),
                  (2, 2): (1, 1),
                  (-1, 2): (-1, 1),
                  (0, 2): (0, 1),
                  (1, 2): (1, 1),
                  (-1, -2): (-1, -1),
                  (0, -2): (0, -1),
                  (1, -2): (1, -1)})
    move = moves.get(rel)
    if move:
        tail[0] += move[0]
        tail[1] += move[1]
    return tail


def move_head(head, dir):
    x, y = 0, 1
    if dir == 'U':
        head[y] += 1
    elif dir == 'D':
        head[y] -= 1
    elif dir == 'L':
        head[x] -= 1
    elif dir == 'R':
        head[x] += 1
    return head


def part2(x):
    with open(x, "r") as f:
        x, y = 0, 1
        visited = {(0, 0)}
        knots = [[0, 0] for _ in range(10)]
        moves = [line.split() for line in f.read().splitlines()]
        for line in moves:
            dir, steps = line[x], int(line[y])
            for _ in range(steps):
                knots[0] = move_head(knots[0], dir)
                for i in range(1, len(knots)):
                    rel = knots[i-1][x] - \
                        knots[i][x], knots[i-1][y]-knots[i][y]
                    knots[i] = move_knot(knots[i], rel)
                visited.add(tuple(knots[9]))
        return (len(visited))

# --- 0.4715099334716797 seconds ---


test_val = 36
if part2("test") == test_val:
    start_time = time.time()
    print('Solution is {}'.format(part2("input")))
    print("--- %s seconds ---" % (time.time() - start_time))
else:
    print("Test failed")
