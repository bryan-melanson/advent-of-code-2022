rules = {'A X': 1 + 3,
         'A Y': 1 + 6,
         'A Z': 1 + 0,
         'B X': 2 + 0,
         'B Y': 2 + 3,
         'B Z': 2 + 6,
         'C X': 3 + 6,
         'C Y': 3 + 0,
         'C Z': 3 + 3
         }


def part1(x):
    with open(x, "r") as f:
        return sum([rules[x] for x in f.read().splitlines()])


test_val = 15
if part1("./test") == test_val:
    print('Solution is {}'.format(part1("./input")))
else:
    print("Test failed")
