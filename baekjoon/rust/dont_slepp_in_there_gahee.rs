use std::io::{BufRead};

fn main() {
    let mut r: usize;
    let mut c: usize;
    let mut rg: usize;
    let mut cg: usize;
    let mut rp: usize;
    let mut cp: usize;

    let mut line = String::new();
    std::io::stdin().read_line(&mut line);
    let mut line_in: Vec::<usize> = line
                                    .trim()
                                    .split_whitespace()
                                    .into_iter()
                                    .map(|x| x.parse::<usize>().unwrap())
                                    .collect();
    r = line_in[0];
    c = line_in[1];
    
    line.clear();
    std::io::stdin().read_line(&mut line);
    line_in = line
                .trim()
                .split_whitespace()
                .into_iter()
                .map(|x| x.parse::<usize>().unwrap())
                .collect();
    rg = line_in[0];
    cg = line_in[1];
    rp = line_in[2];
    cp = line_in[3];
    
    let mut count_p = 0;
    let mut lines = String::new();
    for i in 0..r {
        std::io::stdin().read_line(&mut lines);
        lines = lines
                .trim()
                .parse::<String>()
                .unwrap();
        count_p = count_p + lines.matches("P").count();
        lines.clear();
    }

    if count_p == (cp*rp).into() {
        println!("0");
    } else {
        println!("1");
    }
 
}