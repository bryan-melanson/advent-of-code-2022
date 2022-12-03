def vals(x):
    if x.isupper():
        return ord(x)-38
    else:
        return ord(x)-96


def part2(x):
    with open(x, "r") as f:
        data = f.read().splitlines()
        new = [data[i:i+3]
               for i in range(0, len(data), 3)]
        return sum((vals(list(set(i[0]) & set(i[1]) & set(i[2]))[0]))
                   for i in new)


test_val = 70
if part2("test") == test_val:
    print('Solution is {}'.format(part2("input")))
else:
    print("Test failed")
