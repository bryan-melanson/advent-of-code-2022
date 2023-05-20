proc solution(path: string): int =
    let file = open(path)
    var line: string 
    result = 0
    while file.read_line(line): 
        echo line


let TEST = 0

proc part1*() =
    if (solution("test") == TEST):
        echo solution("input")
