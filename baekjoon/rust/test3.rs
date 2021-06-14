// Title: 문제제목
// Link: https://www.acmicpc.net/problem/test3

use std::collections::{BTreeMap, HashMap, HashSet};
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

fn main() {
    let mut reader = BufReader::new(stdin());
    let mut writer = BufWriter::new(stdout());
    let mut buffer = String::new();

}