use std::time::Instant;

fn solution(_data: String) -> u32 {
    0
}

pub fn print_solution(test_val: u32) {
    let start = Instant::now();

    let input = std::fs::read_to_string("./input").unwrap();
    let test = std::fs::read_to_string("./test").unwrap();

    if solution(test) != test_val {
        println!("Test failed");
    } else {
        println!("{}", solution(input));
        let duration = start.elapsed();
        println!("Elapsed time: {:.2?}", duration);
    }
}
