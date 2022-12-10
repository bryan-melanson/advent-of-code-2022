import time


def move_tail(tail, rel):
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


def move_knot(head, dir):
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


def part1(x):
    with open(x, "r") as f:
        x, y = 0, 1
        visited = {(0, 0)}
        head, tail = [0, 0], [0, 0]
        moves = [line.split() for line in f.read().splitlines()]
        for line in moves:
            dir, steps = line[x], int(line[y])
            for _ in range(steps):
                head = move_knot(head, dir)
                rel = head[x] - tail[x], head[y]-tail[y]
                tail = move_tail(tail, rel)
                visited.add(tuple(tail))
        return (len(visited))

# --- 0.059660911560058594 seconds ---


test_val = 13
if part1("test") == test_val:
    start_time = time.time()
    print('Solution is {}'.format(part1("input")))
    print("--- %s seconds ---" % (time.time() - start_time))
else:
    print("Test failed")
