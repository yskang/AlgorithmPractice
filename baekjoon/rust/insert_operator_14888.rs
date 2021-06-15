// Title: 연산자 끼워넣기
// Link: https://www.acmicpc.net/problem/14888

use std::cmp::{max, min};
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

fn dfs(
    ns: &Vec<i64>,
    idx: i64,
    res: i64,
    plus: i64,
    minus: i64,
    multiples: i64,
    divides: i64,
    minimum: &mut Vec<i64>,
    maximum: &mut Vec<i64>,
    call: &mut Vec<i64>,
) {
    call[0] = call[0] + 1;
    if idx == ns.len() as i64 {
        minimum[0] = min(minimum[0], res);
        maximum[0] = max(maximum[0], res);
        return;
    }
    if plus != 0 {
        dfs(
            ns,
            idx + 1,
            res + ns[idx as usize],
            plus - 1,
            minus,
            multiples,
            divides,
            minimum,
            maximum,
            call,
        );
    }
    if minus != 0 {
        dfs(
            ns,
            idx + 1,
            res - ns[idx as usize],
            plus,
            minus - 1,
            multiples,
            divides,
            minimum,
            maximum,
            call,
        );
    }
    if multiples != 0 {
        dfs(
            ns,
            idx + 1,
            res * ns[idx as usize],
            plus,
            minus,
            multiples - 1,
            divides,
            minimum,
            maximum,
            call,
        );
    }
    if divides != 0 {
        let sign_a = if res > 0 { 1 } else { -1 };
        let sign_b = if ns[idx as usize] > 0 { 1 } else { -1 };
        dfs(
            ns,
            idx + 1,
            sign_a * sign_b * (res.abs() / ns[idx as usize].abs()),
            plus,
            minus,
            multiples,
            divides - 1,
            minimum,
            maximum,
            call,
        );
    }
}

fn solution(ns: Vec<i64>, ops: Vec<i64>) -> String {
    let mut minimum = vec![i64::MAX];
    let mut maximum = vec![i64::MIN];
    let mut call = vec![0];

    dfs(
        &ns,
        1,
        ns[0],
        ops[0],
        ops[1],
        ops[2],
        ops[3],
        &mut minimum,
        &mut maximum,
        &mut call,
    );
    String::from(format!("{}\n{}", maximum[0], minimum[0]))
}

fn main() {
    let mut reader = BufReader::new(stdin());
    let mut writer = BufWriter::new(stdout());

    read_to_tuple!(reader, i64);
    let ns = read_to_vector!(reader, i64);
    let ops = read_to_vector!(reader, i64);

    writeln!(writer, "{}", solution(ns, ops)).unwrap();
    writer.flush().unwrap();
}