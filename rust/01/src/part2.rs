fn solution(data: String) -> u32 {
    let val = data.split("\n\n")
        .map(|e| e.lines().map(|c| c.parse::<u32>().unwrap()).sum::<u32>())
        .max()
        .unwrap();
    val
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
