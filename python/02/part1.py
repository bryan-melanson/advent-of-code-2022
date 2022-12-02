value_map = {'X': 1, 'Y': 2, 'Z': 3}
scores = {'win': 6, 'draw': 3, 'lose': 0}

def rules(b,a):
	score = 0
	if a == 'X':
		if b == 'A':
			score = value_map['X'] + scores['draw']
		elif b == 'B':
			score = value_map['X'] + scores['lose']
		else:
			score = value_map['X'] + scores['win']
	if a == 'Y':
		if b == 'A':
			score = value_map['Y'] + scores['win']
		elif b == 'B':
			score = value_map['Y'] + scores['draw']
		else:
			score = value_map['Y'] + scores['lose']

	if a == 'Z':
		if b == 'A':
			score = value_map['Z'] + scores['lose']
		elif b == 'B':
			score = value_map['Z'] + scores['win']
		else:
			score = value_map['Z'] + scores['draw']
	return score


def part1(x):
	val = 0
	with open(x, "r") as f:
		data = f.read().splitlines()
		for line in data:
			vals = line.split(' ')
			val = val + rules(vals[0],vals[1])
	return val


test_val = 15
if part1("./test") == test_val:
    print('Solution is {}'.format(part1("./input")))
else:
    print("Test failed")
