def part2(x):
    with open(x, "r") as f:
        return sum(sorted([sum([int(calorie) for calorie in calories.split('\n')])
                           for calories in f.read().split("\n\n")])[-3:])


test_val = 45000
if part2("test") == test_val:
    print('Solution is {}'.format(part2("input")))
else:
    print("Test failed")
