def part2(x):
    max = [0, 0, 0]
    with open(x, "r") as f:
        data = f.read().splitlines()
        val = 0
        for line in data:
            if line == '':
                val = 0
                max = sorted(max)
            else:
                val += int(line)
            for i in range(3):
                if val > max[i]:
                    max[i] = val
                    break
    return sum(max)


test_val = 45000
if part2("test") == test_val:
    print('Solution is {}'.format(part2("input")))
else:
    print("Test failed")
