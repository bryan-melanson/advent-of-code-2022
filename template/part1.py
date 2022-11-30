def part1(x):
	with open(x, "r") as f:
		data = f.read().splitlines()
	val = 0
	return val

test_val = 0
if part1("test") == test_val:
	print('Solution is {}'.format(part1("input")))
else:
	print("Test failed")