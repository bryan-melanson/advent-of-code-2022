import time


def part1(x):
    with open(x, "r") as f:
        data = f.read().splitlines()
        sizes = {}
        dirs = []
        for line in data:
            line = line.split()
            if line[0] == '$':
                if line[1] == 'cd':
                    dir = line[2]
                    if (dir == '..'):
                        dirs.pop()
                    else:
                        dirs.append(dir)
            elif line[0] != 'dir':
                val = line[0]
                for i in range(len(dirs)):
                    dir = '_'.join(dirs[:i+1])
                    if dir not in sizes:
                        sizes[dir] = 0
                    sizes[dir] += int(val)
        return (sum(value
                    for value in sizes.values() if value <= 100000))


# --- 0.00467681884765625 seconds ---

test_val = 95437
if part1("test") == test_val:
    start_time = time.time()
    print('Solution is {}'.format(part1("input")))
    print("--- %s seconds ---" % (time.time() - start_time))
else:
    print("Test failed")
