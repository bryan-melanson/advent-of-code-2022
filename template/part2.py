def part2(x):
	with open(x, "r") as f:
		data = f.read().splitlines()
	val = 0
	return val

test_val = 0
if part2("test") == test_val:
	print('Solution is {}'.format(part2("input")))
else:
	print("Test failed")