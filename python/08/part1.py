import time

def check_left(data,i,j):
    tallest = data[i][j]
    while (j > 0):
        j = j-1
        if (data[i][j] >= tallest):
            return False
    return True

def check_right(data,i,j):
    tallest = data[i][j]
    while (j < len(data[0])-1):
        j = j+1
        if (data[i][j] >= tallest):
            return False
    return True

def check_up(data,i,j):
    tallest = data[i][j]
    while (i > 0):
        i = i-1
        if (data[i][j] >= tallest):
            return False
    return True

def check_down(data,i,j):
    tallest = data[i][j]
    while (i < len(data)-1):
        i = i+1
        if (data[i][j] >= tallest):
            return False
    return True

def visible(data,i,j):
    return check_right(data,i,j) or check_left(data,i,j) or check_up(data,i,j) or check_down(data,i,j)

def part1(x):
    with open(x, "r") as f:
        data = [list(line) for line in f.read().splitlines()]
        trees = len(data) * 2 + (len(data[0])-2) * 2
        for i in range(1,len(data)-1):
            for j in range(1,len(data[0])-1):
                if (visible(data,i,j)):
                    trees += 1
    return trees

# --- 0.0226669311523 seconds ---

test_val = 21
if part1("test") == test_val:
    start_time = time.time()
    print('Solution is {}'.format(part1("input")))
    print("--- %s seconds ---" % (time.time() - start_time))
else:
    print("Test failed")
