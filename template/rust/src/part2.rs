use std::fs;

fn solution(data:String) -> u32 {
    0    
}

pub fn print_solution() {
    let input = String::from("./input");
    let test = String::from("./test");

    let data = fs::read_to_string(test)
        .expect("Should have been able to read the file");

    let test_val = 0;

    if solution(data) != test_val {
        println!("Test failed");
    } else {
        println!("{}", solution(input));
    }
}

