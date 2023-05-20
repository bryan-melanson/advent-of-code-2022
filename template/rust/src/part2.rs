fn solution(path: String) -> u32 {
    let _data = std::fs::read_to_string(path);
    0
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
