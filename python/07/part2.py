import time


def part2(x):
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
                    dir = '/'+'/'.join(dirs[1:i+1])
                    if dir not in sizes:
                        sizes[dir] = 0
                    sizes[dir] += int(val)

        total = 70000000
        used = sizes['/']
        space = total - used
        update = 30000000

        return (min(size for size in sizes.values() if (space + size) >= update))


# --- 0.00467681884765625 seconds ---

test_val = 24933642

if part2("test") == test_val:
    start_time = time.time()
    print('Solution is {}'.format(part2("input")))
    print("--- %s seconds ---" % (time.time() - start_time))
else:
    print("Test failed")
