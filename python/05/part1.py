import time
import re


def move_crates(crates, moves):
    for i in moves:
        for num in range(int(i[0])):
            if crates[int(i[1])-1]:
                temp = crates[int(i[1])-1].pop()
                crates[int(i[2])-1].append(temp)
    return crates


def part1(x):
    with open(x, "r") as f:
        data = f.read().split('\n\n')
        crates = [[x.group() for x in re.finditer('\[.\]|\s{4}', i)]
                  for i in data[0].splitlines()]
        crates.reverse()
        del crates[0]
        rows = [[x.group() for x in re.finditer('\d\s', i)]
                for i in data[0].splitlines()][-1]
        moves = [[x.group() for x in re.finditer('\d+', i)]
                 for i in data[1].splitlines()]
        stacks = [[] for i in range(len(rows))]
        for line in crates:
            crate_idx = 0
            for val in range(len(line)):
                if re.search('\[.\]', line[val]):
                    stacks[crate_idx].append(
                        re.findall('[a-zA-Z]', line[val])[0])
                crate_idx += 1
        stacks = move_crates(stacks, moves)
        text = [i.pop() for i in stacks]
        return "".join(text)
# --- 0.005235195159912109 seconds - --


test_val = 'CMZ'
if part1("test") == test_val:
    start_time = time.time()
    print('Solution is {}'.format(part1("input")))
    print("--- %s seconds ---" % (time.time() - start_time))
else:
    print("Test failed")
