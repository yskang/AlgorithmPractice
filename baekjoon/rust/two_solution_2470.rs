// Title: 두 용액
// Link: https://www.acmicpc.net/problem/2470

use std::io::{stdin, stdout, BufRead, BufReader, BufWriter, Write};

macro_rules! read_to_tuple {
    ($buffer:expr, $($t:ty),+) => {{
        let mut line = String::new();
        let buffer = &mut $buffer;
        buffer.read_line(&mut line).unwrap();
        let mut it = line.trim().split_whitespace();
        (
            $(it.next().unwrap().parse::<$t>().unwrap()),+
        )
    }}
}

macro_rules! read_to_vector {
    ($buffer:expr, $t:ty) => {{
        let mut line = String::new();
        let buffer = &mut $buffer;
        buffer.read_line(&mut line).unwrap();
        line.trim()
            .split_whitespace()
            .map(|x| x.parse::<$t>().unwrap())
            .collect::<Vec<$t>>()
    }};
}

fn solution(mut fs: Vec<i64>) -> String {
    fs.sort_by_key(|x| x.abs());
    let mut min_val = i64::MAX;
    let mut ans: Vec<i64> = Vec::new();
    let mut prev = fs[0];

    for f in fs[1..].iter() {
        if (prev + f).abs() < min_val {
            min_val = (prev + f).abs();
            ans = vec![prev, *f];
        }
        prev = *f;
    }
    ans.sort();
    ans.iter()
        .map(|a| a.to_string())
        .collect::<Vec<String>>()
        .join(" ")
}

fn main() {
    let mut reader = BufReader::new(stdin());
    let mut writer = BufWriter::new(stdout());

    read_to_tuple!(reader, i64);
    let fs = read_to_vector!(reader, i64);
    writeln!(writer, "{}", solution(fs)).unwrap();
    writer.flush().unwrap();
}
