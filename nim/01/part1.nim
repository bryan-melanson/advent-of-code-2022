import strutils

proc solution(path:string):int =
  let file = open(path)
  defer: file.close()

  var total = 0

  for line in file.lines():
    if line.len < 1:
        total = 0
        continue
    total += parseInt(line)
    if total > result: result = total

proc part1*(): void =
    let TEST = 24000
    if solution("test") == TEST:
        echo solution("input")