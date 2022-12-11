import time


def inspect(monkey, x):
    op = monkey['op'].split()
    arg1, arg2, arg3 = op[0], op[1], op[2]
    val1, val2 = 0, 0
    if arg1 == 'old':
        val1 = x
    if arg3 == 'old':
        val2 = x
    else:
        val2 = int(arg3)
    if arg2 == '*':
        return (val1 * val2)
    elif arg2 == '+':
        return (val1 + val2)


def test(monkeys, true, false, x):
    return


def part1(x):
    with open(x, "r") as f:
        data = [[i.strip() for i in line.splitlines()]
                for line in f.read().split('\n\n')]
        count = [0] * len(data)
        monkeys = [{} for _ in data]
        for val in enumerate(data):
            num = val[0]
            items = [int(i.strip())
                     for i in val[1][1].split(':')[-1].split(',')]
            op = val[1][2].split('=')[-1].strip()
            test = int(val[1][3].split('by')[-1].strip())
            true = int(val[1][4].split('monkey')[-1].strip())
            false = int(val[1][5].split('monkey')[-1].strip())
            monkeys[num]['items'] = items
            monkeys[num]['op'] = op
            monkeys[num]['test'] = test
            monkeys[num]['true'] = true
            monkeys[num]['false'] = false
        for _ in range(20):
            for m in enumerate(monkeys):
                num, monkey = m[0], m[1]
                if monkey['items']:
                    while monkey['items']:
                        count[num] += 1
                        item = monkey['items'].pop(0)
                        item = inspect(monkey, item)
                        item //= 3
                        if (item % monkey['test'] == 0):
                            monkeys[monkey['true']]['items'].append(item)
                        else:
                            monkeys[monkey['false']]['items'].append(item)
        count = (sorted(count, reverse=false))
        return count[0]*count[1]


# --- 0.059660911560058594 seconds ---

test_val = 10605
if part1("test") == test_val:
    start_time = time.time()
    print('Solution is {}'.format(part1("input")))
    print("--- %s seconds ---" % (time.time() - start_time))
else:
    print("Test failed")
