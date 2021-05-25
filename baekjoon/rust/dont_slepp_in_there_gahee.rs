use std::io::{stdin};

fn main() {
    let r: usize;
    let rp: usize;
    let cp: usize;

    let mut line = String::new();
    stdin().read_line(&mut line).expect("can't read input");
    let rc_in: Vec::<usize> = line
                                .trim()
                                .split_whitespace()
                                .into_iter()
                                .map(|x| x.parse::<usize>().unwrap())
                                .collect();
    r = rc_in[0];
    
    let mut line = String::new();
    stdin().read_line(&mut line).expect("can't read input");
    let gprc_in: Vec::<usize> = line
                                .trim()
                                .split_whitespace()
                                .into_iter()
                                .map(|x| x.parse::<usize>().unwrap())
                                .collect();
    rp = gprc_in[2];
    cp = gprc_in[3];
    
    let mut count_p = 0;
    let mut lines = String::new();
    for _ in 0..r {
        std::io::stdin().read_line(&mut lines).expect("can't read input");
        lines = lines
                .trim()
                .parse::<String>()
                .unwrap();
        count_p = count_p + lines.matches("P").count();
        lines.clear();
    }

    match count_p {
        value if value == cp*rp => println!("0"),
        _ => println!("1"),
    }
 
}