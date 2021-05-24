use std::io::{BufRead};

fn main() {
    let mut r: i64;
    let mut c: i64;
    let mut rg: i64;
    let mut cg: i64;
    let mut rp: i64;
    let mut cp: i64;

    let mut line = String::new();
    std::io::stdin().read_line(&mut line);
    let mut line_in: Vec::<i64> = line
                                    .trim()
                                    .split_whitespace()
                                    .into_iter()
                                    .map(|x| x.parse::<i64>().unwrap())
                                    .collect();
    r = line_in[0];
    c = line_in[1];
    
    line.clear();
    std::io::stdin().read_line(&mut line);
    line_in = line
                .trim()
                .split_whitespace()
                .into_iter()
                .map(|x| x.parse::<i64>().unwrap())
                .collect();
    rg = line_in[0];
    cg = line_in[1];
    rp = line_in[2];
    cp = line_in[3];
    
    let mut lines = String::new();
    for i in 0..r {
        std::io::stdin().read_line(&mut lines);
        lines = lines
                .trim()
                .parse::<String>()
                .unwrap();
        println!("{}", lines);
        lines.clear();
    }

    let mut v: Vec<i64> = vec![10, 20, 30, 40, -2, 3];
    println!("{:?}", v);
    v.sort();
    v.reverse();
    println!("{:?}", v);

}