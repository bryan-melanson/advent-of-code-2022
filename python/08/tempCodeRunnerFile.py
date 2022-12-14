def part1(x):
#     with open(x, "r") as f:
#         data = [list(line) for line in f.read().splitlines()]
#         trees = len(data) * 2 + (len(data[0])-2) * 2
#         for i in range(1,len(data)-1):
#             for j in range(1,len(data[0])-1):
#                 if (visible(data,i,j)):
#                     trees += 1
#     return trees