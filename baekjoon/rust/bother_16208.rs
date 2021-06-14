// Title: 귀찮음
// Link: https://www.acmicpc.net/problem/16208

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

fn solution(mut sticks: Vec<i64>) -> String {
    let mut ans = 0;
    let mut len_stick: i64 = sticks.iter().sum();
    sticks.sort_unstable();

    for stick in sticks {
        len_stick -= stick;
        ans += stick * len_stick
    }

    ans.to_string()
}

fn main() {
    let mut reader = BufReader::new(stdin());
    let mut writer = BufWriter::new(stdout());

    read_to_tuple!(reader, i64);
    let sticks = read_to_vector!(reader, i64);
    writeln!(writer, "{}", solution(sticks)).unwrap();
    writer.flush().unwrap();
}
