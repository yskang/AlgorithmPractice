use std::io::{stdin, stdout, BufRead, BufReader, BufWriter, Write};
use std::collections::HashMap;

fn dfs(graph: &mut Vec<Vec<usize>>, node: usize, visited: &mut Vec<bool>, line: &mut Vec<usize>) {
    match visited[node] {
        true => {
            return;
        },
        false => {
            visited.insert(node, true);
        },
        _ => {
            return;
        },
    }
    for child in graph[node].iter_mut() {
        dfs(graph, *child, visited, line);
    }
    line.push(node);
}

fn solution(n: usize, m: usize, g: &mut Vec<Vec<usize>>) {
    println!("n: {}, m: {}, g: {:?}", n, m, g);
    let mut visited: Vec<bool> = vec![false; n+1];
    let mut line: Vec<usize> = Vec::new();

    for node in 0..n+1 {
        if !visited[node] {
            dfs(g, node, &mut visited, &mut line);
        }
    }

    // line.map(|x| String::from(x))
    //     .collect::<Vec<_>>()
    //     .join(" ");
    println!("{:?}", line);
}


fn main() {
    let mut buf = BufReader::new(stdin());
    let mut out = BufWriter::new(stdout());
    let mut buffer = String::new();

    buf.read_line(&mut buffer).unwrap();
    // println!("{:?}", buffer);
    let mut values: Vec<usize>;
    let n: usize;
    let m: usize;
    values = buffer.split_whitespace()
                    .map(|x| x.parse::<usize>().unwrap())
                    .collect();
    n = values[0];
    m = values[1];
    // println!("{}, {}", n, m);
    let mut g: Vec<Vec<usize>> = vec![Vec::new(); n+1];
    for _ in 0..m {
        buffer.clear();
        buf.read_line(&mut buffer).unwrap();
        values.clear();
        values = buffer.split_whitespace()
                        .map(|x| x.parse::<usize>().unwrap())
                        .collect();
        g[values[0]].push(values[1])
    }
    // println!("{:?}", g);
    solution(n, m, &mut g);
}