// Title: 스타트와 링크
// Link: https://www.acmicpc.net/problem/14889

use std::cmp::min;
use std::collections::VecDeque;
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
    n: usize,
    ans: &mut usize,
    depth: usize,
    target: usize,
    special: &Vec<Vec<usize>>,
    team: &mut Vec<usize>,
    all_cases: &mut VecDeque<usize>,
) {
    if depth == target {
        all_cases.push_back(*ans);
    } else {
        for i in n + 1..target * 2 + 1 {
            for member in team.iter_mut() {
                *ans +=
                    special[*member as usize][i as usize] + special[i as usize][*member as usize];
            }
            team.push(i);
            dfs(i, ans, depth + 1, target, special, team, all_cases);
        }
    }
    team.pop().unwrap();
    for member in team {
        *ans -= special[*member as usize][n as usize] + special[n as usize][*member as usize];
    }
}

fn solution(n: usize, s: Vec<Vec<usize>>) -> String {
    let mut all_cases: VecDeque<usize> = VecDeque::new();
    let mut ans = 0;

    for i in 1..n + 2 - n / 2 {
        dfs(i, &mut ans, 1, n / 2, &s, &mut vec![i], &mut all_cases);
    }

    let mut min_diff = usize::MAX;
    while all_cases.len() > 0 {
        let front = all_cases.pop_front().unwrap();
        let back = all_cases.pop_back().unwrap();
        min_diff = min(
            min_diff,
            if front > back {
                front - back
            } else {
                back - front
            },
        );
    }
    return min_diff.to_string();
}

fn main() {
    let mut reader = BufReader::new(stdin());
    let mut writer = BufWriter::new(stdout());

    let n = read_to_tuple!(reader, usize);
    let mut s = vec![vec![0; n]];
    for _ in 0..n {
        s.push([vec![0usize], read_to_vector!(reader, usize)].concat());
    }
    writeln!(writer, "{}", solution(n, s)).unwrap();
    writer.flush().unwrap();
}
