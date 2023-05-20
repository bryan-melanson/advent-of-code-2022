fn solution(data: String) -> u32 {
    let mut total = 0;
    let entries: Vec<String> = data.lines().map(|line| line.to_string()).collect();
    for entry in entries {
        let score = match &*entry {
            "A X" => 4,
            "A Y" => 8,
            "A Z" => 3,
            "B X" => 1,
            "B Y" => 5,
            "B Z" => 9,
            "C X" => 7,
            "C Y" => 2,
            "C Z" => 6,
            _ => 0,
        };
        total += score;
    }
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
