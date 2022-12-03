def vals(x):
    if x.isupper():
        return ord(x)-38
    else:
        return ord(x)-96


def part1(x):
    with open(x, "r") as f:
        data = [[pack[0:len(pack)//2], pack[len(pack)//2:]]
                for pack in f.read().splitlines()]
        return sum((vals(list(set(i[0]) & set(i[1]))[0]))
                   for i in data)


test_val = 157
if part1("test") == test_val:
    print('Solution is {}'.format(part1("input")))
else:
    print("Test failed")
