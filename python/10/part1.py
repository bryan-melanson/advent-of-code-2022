import time


def part1(x):
    with open(x, "r") as f:
        cycle, r = 1, 1
        reg = dict({20: 0, 60: 0, 100: 0, 140: 0, 180: 0, 220: 0})
        cmds = [line.split() for line in f.read().splitlines()]
        for cmd in cmds:
            if cmd[0] == 'noop':
                if cycle in reg:
                    reg[cycle] = r
                cycle += 1
            else:
                if cycle in reg:
                    reg[cycle] = r
                val = int(cmd[1])
                cycle += 1
                if cycle in reg:
                    reg[cycle] = r
                cycle += 1
                r += val
        return (sum([reg[i]*i for i in reg]))


# --- 0.059660911560058594 seconds ---

test_val = 13140
if part1("test") == test_val:
    start_time = time.time()
    print('Solution is {}'.format(part1("input")))
    print("--- %s seconds ---" % (time.time() - start_time))
else:
    print("Test failed")
