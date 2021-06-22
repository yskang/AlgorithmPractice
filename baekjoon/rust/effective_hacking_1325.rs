// Title: 효율적인 해킹
// Link: https://www.acmicpc.net/problem/1325

use std::cmp::max;
use std::collections::{HashMap, HashSet};
use std::io::{stdin, stdout, BufRead, BufReader, BufWriter, Write};
use std::mem::swap;

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

fn get_scc_iter(
    vertices: &mut Vec<usize>,
    edges: &mut HashMap<usize, HashSet<usize>>,
) -> Vec<HashSet<usize>> {
    let mut sccs: Vec<HashSet<usize>> = Vec::new();
    let mut identified: HashSet<usize> = HashSet::new();
    let mut stack: Vec<usize> = Vec::new();
    let mut index: HashMap<usize, usize> = HashMap::new();
    let mut boundaries: Vec<usize> = Vec::new();

    for v in vertices {
        if !index.contains_key(&v) {
            let mut to_do: Vec<(&str, usize)> = vec![("VISIT", *v)];
            while to_do.len() > 0 {
                let (operation_type, vv) = to_do.pop().unwrap();
                if operation_type == "VISIT" {
                    index.insert(vv, stack.len());
                    stack.push(vv);
                    boundaries.push(index[&vv]);
                    to_do.push(("POSTVISIT", vv));
                    let rev: Vec<(&str, usize)> = Vec::new();
                    for w in edges[&vv] {
                        rev.push(("VISITEDGE", w))
                    }
                    rev.reverse();
                    for tup in rev {
                        to_do.push(tup);
                    }
                } else if operation_type == "VISITEDGE" {
                    if !index.contains_key(&vv) {
                        to_do.push(("VISIT", vv))
                    } else if !identified.contains(&vv) {
                        while index[&vv] < *boundaries.last().unwrap() {
                            boundaries.pop();
                        }
                    }
                } else {
                    if *boundaries.last().unwrap() == index[&vv] {
                        boundaries.pop();
                        let mut scc: HashSet<usize> = HashSet::new();
                        for t in stack[index[&vv]..].iter_mut() {
                            scc.insert(*t);
                        }
                        for s in scc {
                            identified.insert(s);
                        }
                        sccs.push(scc);
                        stack.resize(index[&vv], 0);
                    }
                }
            }
        }
    }
    sccs
}

fn solution(
    n: usize,
    pairs: HashMap<usize, HashSet<usize>>,
    starts: HashSet<usize>,
    pairs_rev: HashMap<usize, HashSet<usize>>,
) -> String {
    let mut counts: HashMap<usize, HashSet<usize>> = HashMap::new();
    let mut nodes = (1..n + 1).collect::<Vec<usize>>();
    let mut new_node = n + 1;
    let mut scc_map: HashMap<usize, HashSet<usize>> = HashMap::new();

    for scc in get_scc_iter(&mut nodes, &mut pairs) {
        if scc.len() > 1 {
            scc_map.insert(new_node, HashSet::new());
            let mut outs: HashSet<usize> = HashSet::new();
            let mut ins: HashSet<usize> = HashSet::new();
            for node in scc {
                pairs.get(&node).unwrap().iter().for_each(|x| {
                    outs.insert(*x);
                });
                pairs_rev.get(&node).unwrap().iter().for_each(|x| {
                    ins.insert(*x);
                });
            }
            outs.retain(|x| !scc.contains(x));
            ins.retain(|x| !scc.contains(x));
            outs.iter().for_each(|x| {
                pairs.get(&new_node).unwrap().insert(*x);
            });

            for node in ins {
                pairs.get(&node).unwrap().retain(|x| !scc.contains(x));
                pairs.get(&node).unwrap().insert(new_node);
            }

            for node in outs {
                pairs_rev.get(&node).unwrap().retain(|x| !scc.contains(x));
                pairs_rev.get(&node).unwrap().insert(new_node);
            }

            counts.insert(new_node, scc);
            if ins.len() == 0 {
                starts.insert(new_node);
            }
            new_node += 1;
        }
    }

    let temp: HashSet<usize> = HashSet::new();
    loop {
        for node in starts {
            for manto in pairs.get(&node).unwrap() {
                if counts.get(&node).unwrap().len() == 0 {
                    counts.get(&node).unwrap().insert(node);
                }
                if counts.get(manto).unwrap().len() == 0 {
                    counts.get(manto).unwrap().insert(*manto);
                }
                counts.get(&node).unwrap().iter().for_each(|x| {
                    counts.get(manto).unwrap().insert(*x);
                });
                pairs_rev.get(manto).unwrap().remove(&node);
                if pairs_rev.get(manto).unwrap().len() == 0 {
                    temp.insert(*manto);
                }
            }
        }
        swap(&mut starts, &mut temp);
        temp.clear();
        if starts.len() == 0 {
            break;
        }
    }

    let res: Vec<usize> = vec![];

    let counts_lens: HashMap<usize, usize> = HashMap::new();
    for (node, _) in counts {
        counts_lens.insert(node, (counts.get(&node).unwrap()).len());
    }

    let mut max_count = counts_lens.values().max().unwrap();
    for (node, _) in counts_lens {
        if counts_lens.get(&node).unwrap() == max_count {
            res.push(node);
        }
    }
    let ans: HashSet<usize> = HashSet::new();
    for r in res {
        if scc_map.contains_key(&r) {
            for c in scc_map.get(&r).unwrap() {
                ans.insert(*c);
            }
        } else {
            ans.insert(r);
        }
    }
    let vec_ans: Vec<usize> = ans.into_iter().collect();
    vec_ans.sort();
    vec_ans
        .iter()
        .map(|x| x.to_string())
        .collect::<Vec<String>>()
        .join(" ")
}

fn main() {
    let mut reader = BufReader::new(stdin());
    let mut writer = BufWriter::new(stdout());

    let (n, m) = read_to_tuple!(reader, usize, usize);
    let mut pairs: HashMap<usize, HashSet<usize>> = HashMap::new();
    let mut pairs_rev: HashMap<usize, HashSet<usize>> = HashMap::new();
    let mut starts: HashSet<usize> = (1..n + 1).collect();

    for _ in 0..m {
        let (manti, manto) = read_to_tuple!(reader, usize, usize);
        if let Some(mantos) = pairs.get(&manti) {
            mantos.insert(manto);
        } else {
            pairs.insert(manti, (manto..manto + 1).collect());
        }
        if let Some(mantis) = pairs.get(&manto) {
            mantis.insert(manti);
        } else {
            pairs.insert(manto, (manti..manti + 1).collect());
        }
        starts.remove(&manto);
    }

    writeln!(writer, "{}", solution(n, pairs, starts, pairs_rev)).unwrap();
    writer.flush().unwrap();
}
