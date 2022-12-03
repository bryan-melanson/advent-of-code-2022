rules = {'A X': 0 + 3,
         'A Y': 3 + 1,
         'A Z': 6 + 2,
         'B X': 0 + 1,
         'B Y': 3 + 2,
         'B Z': 6 + 3,
         'C X': 0 + 2,
         'C Y': 3 + 3,
         'C Z': 6 + 1
         }


def part2(x):
    with open(x, "r") as f:
        return sum([rules[x] for x in f.read().splitlines()])


test_val = 12
if part2("./test") == test_val:
    print('Solution is {}'.format(part2("./input")))
else:
    print("Test failed")
