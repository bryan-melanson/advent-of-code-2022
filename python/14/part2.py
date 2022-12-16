import time


def initialize(data):
    rocks = set()
    for line in range(len(data)):
        for item in range(len(data[line])-1):
            x1, y1 = map(int, data[line][item].strip().split(','))
            x2, y2 = map(int, data[line][item+1].strip().split(','))
            if (x2 == x1):
                if y2 > y1:
                    foo = [(x2, y) for y in range(y1, y2+1)]
                else:
                    foo = [(x2, y) for y in range(y2, y1+1)]
            else:
                if x2 > x1:
                    foo = [(x, y2) for x in range(x1, x2+1)]
                else:
                    foo = [(x, y2) for x in range(x2, x1+1)]
            rocks |= set(foo)
    return rocks


def part2(x):
    with open(x, "r") as f:
        data = [line.split('->') for line in f.read().splitlines()]
        rocks = initialize(data)
        done = False
        count = 0
        floor = max(rocks, key=lambda x: x[1])[1] + 2
        while not done:
            sand_x, sand_y = 500, 0
            blocked = False
            while not blocked and not done:
                if (sand_x, sand_y+1) not in rocks:
                    sand_y += 1
                elif (sand_x-1, sand_y+1) not in rocks:
                    sand_x -= 1
                    sand_y += 1
                elif (sand_x+1, sand_y+1) not in rocks:
                    sand_x += 1
                    sand_y += 1
                else:
                    count += 1
                    rocks.add((sand_x, sand_y))
                    blocked = True
                if (sand_y+1 >= floor):
                    count += 1
                    rocks.add((sand_x, sand_y))
                    blocked = True;
                elif ((sand_x, sand_y) == (500,0)):
                    done = True
        return count

# --- 1.16048502922 seconds ---

test_val = 93
if part2("test") == test_val:
    print('Passed test value')
    start_time = time.time()
    print('Solution is {}'.format(part2("input")))
    print("--- %s seconds ---" % (time.time() - start_time))
else:
    print("Test failed")
