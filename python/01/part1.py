def part1(x):
    with open(x, "r") as f:
        return max([sum([int(calorie) for calorie in calories.split('\n')])
                    for calories in f.read().split("\n\n")])


test_val = 24000
if part1("./test") == test_val:
    print('Solution is {}'.format(part1("./input")))
else:
    print("Test failed")
