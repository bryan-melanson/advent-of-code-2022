value_map = {'A': 1, 'B': 2, 'C': 3}
scores = {'win': 6, 'draw': 3, 'lose': 0}

def rules(a,b):
	score = 0
	if b == 'X':
		if a == 'A':
			score = value_map['C']
		elif a == 'B':
			score = value_map['A']
		else:
			score = value_map['B']
		score += scores['lose']
	if b == 'Y':
		if a == 'A':
			score = value_map['A']
		elif a == 'B':
			score = value_map['B']
		else:
			score = value_map['C']
		score += scores['draw']
	if b == 'Z':
		if a == 'A':
			score = value_map['B']
		elif a == 'B':
			score = value_map['C']
		else:
			score = value_map['A']
		score += scores['win']
	return score


def part2(x):
	val = 0
	with open(x, "r") as f:
		data = f.read().splitlines()
		for line in data:
			vals = line.split(' ')
			val = val + rules(vals[0],vals[1])
	return val


test_val = 12
if part2("./test") == test_val:
    print('Solution is {}'.format(part2("./input")))
else:
    print("Test failed")
