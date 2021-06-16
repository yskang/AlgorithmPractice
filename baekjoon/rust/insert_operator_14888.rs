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

struct Operator {
    plus: i64,
    minus: i64,
    multiples: i64,
    divides: i64,
}

fn build_operator(op: &Operator, offset: (i64, i64, i64, i64)) -> Operator {
    Operator {
        plus: op.plus + offset.0,
        minus: op.minus + offset.1,
        multiples: op.multiples + offset.2,
        divides: op.divides + offset.3,
    }
}

fn dfs(
    ns: &Vec<i64>,
    idx: usize,
    res: i64,
    operator: Operator,
    min_max: &mut (i64, i64),
) {
    if idx == ns.len() {
        min_max.0 = min(min_max.0, res);
        min_max.1 = max(min_max.1, res);
        return;
    }
    if operator.plus != 0 {
        dfs(ns, idx + 1, res + ns[idx], build_operator(&operator, (-1, 0, 0, 0)), min_max);
    }
    if operator.minus != 0 {
        dfs(ns, idx + 1, res - ns[idx], build_operator(&operator, (0, -1, 0, 0)), min_max);
    }
    if operator.multiples != 0 {
        dfs(ns, idx + 1, res * ns[idx], build_operator(&operator, (0, 0, -1, 0)), min_max);
    }
    if operator.divides != 0 {
        let sign_a = if res > 0 { 1 } else { -1 };
        let sign_b = if ns[idx] > 0 { 1 } else { -1 };
        dfs(
            ns,
            idx + 1,
            sign_a * sign_b * (res.abs() / ns[idx].abs()),
            build_operator(&operator, (0, 0, 0, -1)),
            min_max,
        );
    }
}

fn solution(ns: Vec<i64>, ops: Operator) -> String {
    let mut min_max = (i64::MAX, i64::MIN);
    dfs(&ns, 1, ns[0], ops, &mut min_max);
    String::from(format!("{}\n{}", min_max.1, min_max.0))
}

fn main() {
    let mut reader = BufReader::new(stdin());
    let mut writer = BufWriter::new(stdout());
    read_to_tuple!(reader, i64);
    let ns = read_to_vector!(reader, i64);
    let (plus, minus, multiples, divides) = read_to_tuple!(reader, i64, i64, i64, i64);
    let mut operator = Operator {
        plus: plus,
        minus: minus,
        multiples: multiples,
        divides: divides,
    };

    writeln!(writer, "{}", solution(ns, operator)).unwrap();
    writer.flush().unwrap();
}
