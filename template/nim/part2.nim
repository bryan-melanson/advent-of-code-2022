proc solution(path: string): int = 
    let file = open(path)
    var line: string
    result = 0
    while file.read_line(line):
        echo line

proc part2*() =
    const TEST = 0
    if solution("test") == TEST:
        echo solution("input")
    
