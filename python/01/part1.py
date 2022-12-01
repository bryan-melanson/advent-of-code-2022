def part1(x):
    max = 0
    with open(x, "r") as f:
        data = f.read().splitlines()
        val = 0
        for line in data:
            if line == '':
                val = 0
            else:
                val += int(line)
            if (val > max):
                max = val
    return max


test_val = 24000
if part1("test") == test_val:
    print('Solution is {}'.format(part1("input")))
else:
    print("Test failed")
