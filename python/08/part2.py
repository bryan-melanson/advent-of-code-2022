import time

def check_left(data,i,j):
    tallest = data[i][j]
    count = 0
    while (j > 0):
        j = j-1
        count += 1
        if (data[i][j] >= tallest):
            break
    if count == 0:
        return 1
    else:
        return count

def check_right(data,i,j):
    tallest = data[i][j]
    count = 0
    while (j < len(data[0])-1):
        j = j+1
        count += 1
        if (data[i][j] >= tallest):
            break
    if count == 0:
        return 1
    else:
        return count

def check_up(data,i,j):
    tallest = data[i][j]
    count = 0
    while (i > 0):
        i = i-1
        count += 1
        if (data[i][j] >= tallest):
            break
    if count == 0:
        return 1
    else:
        return count

def check_down(data,i,j):
    tallest = data[i][j]
    count = 0
    while (i < len(data)-1):
        i = i+1
        count += 1
        if (data[i][j] >= tallest):
            break
    if count == 0:
        return 1
    else:
        return count

def visible(data,i,j):
    return check_right(data,i,j) * check_left(data,i,j) * check_up(data,i,j) * check_down(data,i,j)

def part2(x):
    with open(x, "r") as f:
        data = [list(line) for line in f.read().splitlines()]
        trees = 0
        for i in range(0,len(data)-1):
            for j in range(0,len(data[0])):
                v = visible(data,i,j)
                if (v > trees):
                    trees = v
    return trees

# --- 0.0226669311523 seconds ---

test_val = 16
if part2("test") == test_val:
    start_time = time.time()
    print('Solution is {}'.format(part2("input")))
    print("--- %s seconds ---" % (time.time() - start_time))
else:
    print("Test failed")
