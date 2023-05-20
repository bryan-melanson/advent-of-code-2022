import strutils
import std/sequtils
import std/algorithm

proc solution(path:string):int =
    let file = open(path)
    defer: file.close()

    var total = 0
    var totals = newSeq[int]()

    for line in file.lines():
        if line.len < 1:
            totals.add(total)
            total = 0
            continue
        total += parseInt(line)
    totals.add(total) 
    return sorted(totals)[^3 .. ^1].foldl(a+b) 

proc part2*(): void =
    let TEST = 45000
    if solution("test") == TEST:
        echo solution("input")
