use std::io::{stdin, stdout, BufRead, BufReader, BufWriter, Write};
use std::collections::{HashMap, HashSet};


struct Graph {
    childs_of: HashMap<usize, HashSet<usize>>,
}

impl Graph {
    fn new() -> Graph {
        Graph {
            childs_of: HashMap::new(),
        }
    }

    fn add_node(&mut self, node: &usize) {
        if !self.childs_of.contains_key(node) {
            self.childs_of.insert(*node, HashSet::new());
        }
    }

    fn add_edge(&mut self, x: &usize, y: &usize) {
        if let Some(v) = self.childs_of.get_mut(x) {
            v.insert(*y);
        }
    }
}


fn dfs(graph: &Graph, node: usize, visited: &mut Vec<bool>, line: &mut Vec<usize>) {
    if let Some(v) = visited.get(node) {
        if *v {
            return;
        } else {
            visited[node] = true;
        }
    }

    if let Some(v) = graph.childs_of.get(&node) {
        let mut iter = v.iter();
        while let Some(child) = iter.next() {
            dfs(graph, *child, visited, line);
        }
    }

    line.push(node);
}


fn solution(n: usize, g: &Graph) -> String {
    // println!("n: {}, m: {}, g: {:?}", n, m, g);
    let mut visited: Vec<bool> = vec![false; n+1];
    let mut line: Vec<usize> = Vec::new();

    for node in 1..n+1 {
        if !visited[node] {
            dfs(g, node, &mut visited, &mut line);
        }
    }
    line.reverse();
    let ans = line.iter().map(|x| x.to_string())
        .collect::<Vec<_>>()
        .join(" ");
    ans
}


fn main() {
    let mut buf = BufReader::new(stdin());
    let mut out = BufWriter::new(stdout());
    let mut buffer = String::new();

    buf.read_line(&mut buffer).unwrap();
    let mut values: Vec<usize>;
    let n: usize;
    let m: usize;
    values = buffer.split_whitespace()
                    .map(|x| x.parse::<usize>().unwrap())
                    .collect();
    n = values[0];
    m = values[1];

    let mut graph = Graph::new();

    for _ in 0..m {
        buffer.clear();
        buf.read_line(&mut buffer).unwrap();
        values.clear();
        values = buffer.split_whitespace()
                        .map(|x| x.parse::<usize>().unwrap())
                        .collect();

        graph.add_node(&values[0]);
        graph.add_node(&values[1]);
        graph.add_edge(&values[0], &values[1]);
    }
    writeln!(out, "{}", solution(n, &graph)).unwrap();
    out.flush().unwrap();
}