use itertools::Itertools;

fn solution(data: String) -> u32 {
    data.split("\n\n")
        .map(|elf| {
            elf.lines()
                .filter_map(|s| s.parse::<u32>().ok())
                .sum::<u32>()
        })
        .sorted()
        .rev()
        .take(3)
        .sum::<u32>()
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
