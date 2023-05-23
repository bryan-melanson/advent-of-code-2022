use std::collections::HashSet;

fn char_to_val(c: char) -> u32 {
    match c {
        'a'..='z' => c as u32 - 'a' as u32 + 1,
        'A'..='Z' => c as u32 - 'A' as u32 + 27,
        _ => 0,
    }
}

fn solution(_data: String) -> u32 {
    let mut total = 0;
    let _val = _data.lines().map(|line| line).for_each(|line| {
        let (s1, s2) = line.split_at(line.len() / 2);
        let set: HashSet<_> = s1.chars().collect();
        s2.chars()
            .filter(|c| set.contains(c))
            .take(1)
            .for_each(|c: char| total += char_to_val(c));
    });
    total
}

pub fn print_solution(test_val: u32) {
    let input = std::fs::read_to_string("./input").unwrap();
    let test = std::fs::read_to_string("./test").unwrap();

    if solution(test) != test_val {
        println!("Test failed");
    } else {
        println!("{}", solution(input));
    }
}
