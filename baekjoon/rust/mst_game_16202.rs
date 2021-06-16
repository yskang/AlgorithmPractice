// Title: MST 게임
// Link: https://www.acmicpc.net/problem/16202

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

fn find(x: usize, parents: &mut Vec<usize>) -> usize {
    if x == parents[x] {
        return x;
    }
    let p = find(parents[x], parents);
    parents[x] = p;
    p
}

fn union(mut x: usize, mut y: usize, parents: &mut Vec<usize>) {
    x = find(x, parents);
    y = find(y, parents);
    if x != y {
        parents[y] = x;
    }
}

fn kruskal(
    edges: Vec<(usize, usize, usize)>,
    parents: &mut Vec<usize>,
    mut num_node: usize,
) -> (usize, bool) {
    let mut cost = 0;
    let mut i = 0;
    while num_node - 1 > 0 {
        if i >= edges.len() {
            return (0, false);
        }
        let (c, s, e) = edges[i];
        if find(s, parents) != find(e, parents) {
            cost += c;
            union(s, e, parents);
            num_node -= 1;
        }
        i += 1;
    }
    (cost, true)
}

fn solution_kruskal(edges: Vec<(usize, usize, usize)>, num_node: usize, k: usize) -> String {
    let mut ans = vec![0; k];
    for i in 0..k {
        let mut parents = (0..num_node + 1).collect::<Vec<usize>>();
        let (cost, valid) = kruskal(edges[i + 1..].to_vec(), &mut parents, num_node);
        ans[i] = cost;
        if !valid {
            break;
        }
    }
    ans.iter()
        .map(|x| x.to_string())
        .collect::<Vec<String>>()
        .join(" ")
}

fn main() {
    let mut reader = BufReader::new(stdin());
    let mut writer = BufWriter::new(stdout());

    let (n, m, k) = read_to_tuple!(reader, usize, usize, usize);
    let mut edges = vec![(0, 0, 0)];

    for i in 0..m {
        let (a, b) = read_to_tuple!(reader, usize, usize);
        edges.push((i + 1, a, b));
    }

    writeln!(writer, "{}", solution_kruskal(edges, n, k)).unwrap();
    writer.flush().unwrap();
}
