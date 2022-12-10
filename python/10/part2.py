import time


def pixel(c, r):
    c = c % 40
    if not c:
        print('\n', end='')
    pixels = [r-1, r, r+1]
    if c in pixels:
        print('#', end='')
    else:
        print('.', end='')


def part2(x):
    with open(x, "r") as f:
        cycle, r = 0, 1
        cmds = [line.split() for line in f.read().splitlines()]
        for cmd in cmds:
            if cmd[0] == 'noop':
                pixel(cycle, r)
                cycle += 1
            else:
                val = int(cmd[1])
                pixel(cycle, r)
                cycle += 1
                pixel(cycle, r)
                cycle += 1
                r += val
        print('\n')


# --- 0.0033750534057617188 seconds - --

start_time = time.time()
part2("input")
print("--- %s seconds ---" % (time.time() - start_time))
