import time
import re


def get_idx(x):
    match = re.search(
        r'(.)(?!\1)(.)(?!\1|\2)(.)(?!\1|\2|\3)(.)(?!\1|\2|\3|\4)(.)(?!\1|\2|\3|\4|\5)(.)(?!\1|\2|\3|\4|\5|\6)(.)(?!\1|\2|\3|\4|\5|\6|\7)(.)(?!\1|\2|\3|\4|\5|\6|\7|\8)(.)(?!\1|\2|\3|\4|\5|\6|\7|\8|\9)(.)(?!\1|\2|\3|\4|\5|\6|\7|\8|\9|\10)(.)(?!\1|\2|\3|\4|\5|\6|\7|\8|\9|\10|\11)(.)(?!\1|\2|\3|\4|\5|\6|\7|\8|\9|\10|\11|\12)(.)(?!\1|\2|\3|\4|\5|\6|\7|\8|\9|\10|\11|\12|\13)(.)', x)
    return match.span()[1]


def part2(x):
    with open(x, "r") as f:
        data = f.read()
        return (get_idx(data))

# --- 0.004179954528808594 seconds ---


test_val = 19
if part2("test") == test_val:
    start_time = time.time()
    print('Solution is {}'.format(part2("input")))
    print("--- %s seconds ---" % (time.time() - start_time))
else:
    print("Test failed")
