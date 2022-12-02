use std::fs;

fn solution(path: String) -> u32 {
    let data = std::fs::read_to_string(path);
    0
}

pub fn print_solution(test_val: u32) {
    let input = String::from("./input");
    let test = String::from("./test");

    if solution(test) != test_val {
        println!("Test failed");
    } else {
        println!("{}", solution(input));
    }
}
