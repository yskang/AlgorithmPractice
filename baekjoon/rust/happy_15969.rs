use std::io::{self, BufRead};

fn main() {
    let mut line = String::new();
    let stdin = io::stdin();
    let _ = stdin.lock().read_line(&mut line);
    let _n = line.trim().parse::<u128>().unwrap();
    line.clear();
    let _ = stdin.read_line(&mut line);
    let scores: Vec<u128> = line.trim().split(" ").into_iter().map(|x| x.parse::<u128>().unwrap()).collect();

    let mut min: u128 = std::u128::MAX;
    let mut max: u128 = std::u128::MIN;

    scores.into_iter().for_each(|x| {
        if x < min {
            min = x;
        }
        if x > max {
            max = x;
        }
    });

    println!("{}", max-min);
}
