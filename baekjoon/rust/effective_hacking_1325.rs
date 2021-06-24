// Title: 효율적인 해킹
// Link: https://www.acmicpc.net/problem/1325

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
                    boundaries.push(*index.get(&vv).unwrap());
                    to_do.push(("POSTVISIT", vv));

                    let mut rev: Vec<(&str, usize)> = Vec::new();
                    for w in edges.entry(vv).or_default().iter() {
                        rev.push(("VISITEDGE", *w));
                    }
                    rev.reverse();

                    for tup in rev {
                        to_do.push(tup);
                    }
                } else if operation_type == "VISITEDGE" {
                    if !index.contains_key(&vv) {
                        to_do.push(("VISIT", vv))
                    } else if !identified.contains(&vv) {
                        while *index.get(&vv).unwrap() < *boundaries.last().unwrap() {
                            boundaries.pop();
                        }
                    }
                } else {
                    if *boundaries.last().unwrap() == index[&vv] {
                        boundaries.pop();
                        let mut scc: HashSet<usize> = HashSet::new();
                        for t in stack[*index.get(&vv).unwrap()..].iter_mut() {
                            scc.insert(*t);
                        }
                        stack.resize(*index.get(&vv).unwrap(), 0);
                        for s in scc.iter() {
                            identified.insert(*s);
                        }
                        sccs.push(scc);
                    }
                }
            }
        }
    }
    sccs
}

fn solution(
    n: usize,
    mut pairs: HashMap<usize, HashSet<usize>>,
    mut starts: HashSet<usize>,
    mut pairs_rev: HashMap<usize, HashSet<usize>>,
) -> String {
    let mut counts: HashMap<usize, HashSet<usize>> = HashMap::new();
    let mut nodes = (1..n + 1).collect::<Vec<usize>>();
    let mut new_node = n + 1;
    let mut scc_map: HashMap<usize, HashSet<usize>> = HashMap::new();

    for scc in get_scc_iter(&mut nodes, &mut pairs) {
        if scc.len() > 1 {
            scc_map.insert(new_node, scc.clone());
            let mut outs: HashSet<usize> = HashSet::new();
            let mut ins: HashSet<usize> = HashSet::new();
            for node in scc.iter() {
                pairs.entry(*node).or_default().iter().for_each(|x| {
                    outs.insert(*x);
                });
                pairs_rev.entry(*node).or_default().iter().for_each(|x| {
                    ins.insert(*x);
                });
            }
            outs.retain(|x| !scc.contains(x));
            ins.retain(|x| !scc.contains(x));
            outs.iter().for_each(|x| {
                pairs.entry(new_node).or_default().insert(*x);
            });

            for node in ins.iter() {
                pairs.entry(*node).or_default().retain(|x| !scc.contains(x));
                pairs.entry(*node).or_default().insert(new_node);
            }

            for node in outs.iter() {
                pairs_rev
                    .entry(*node)
                    .or_default()
                    .retain(|x| !scc.contains(x));
                pairs_rev.entry(*node).or_default().insert(new_node);
            }

            counts.insert(new_node, scc);
            if ins.len() == 0 {
                starts.insert(new_node);
            }
            new_node += 1;
        }
    }

    let mut temp: HashSet<usize> = HashSet::new();
    loop {
        for node in starts.iter() {
            for manto in pairs.entry(*node).or_default().iter() {
                if counts.entry(*node).or_default().len() == 0 {
                    counts.entry(*node).or_default().insert(*node);
                }

                if counts.entry(*manto).or_default().len() == 0 {
                    counts.entry(*manto).or_default().insert(*manto);
                }

                let temp2 = counts.entry(*node).or_default().clone();
                for x in temp2.iter() {
                    counts.entry(*manto).or_default().insert(*x);
                }

                pairs_rev.entry(*manto).or_default().remove(&node);
                if pairs_rev.entry(*manto).or_default().len() == 0 {
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

    let mut res: Vec<usize> = vec![];

    let mut counts_lens: HashMap<usize, usize> = HashMap::new();

    let nodes = counts.keys().cloned().collect::<Vec<_>>();
    for node in nodes {
        counts_lens.insert(node, (counts.entry(node).or_default()).len());
    }

    let max_count = counts_lens.values().max().unwrap();

    let nodes = counts_lens.keys().cloned().collect::<Vec<_>>();
    for node in nodes {
        if let Some(len) = counts_lens.get(&node) {
            if len == max_count {
                res.push(node);
            }
        }
    }

    let mut ans: HashSet<usize> = HashSet::new();
    for r in res {
        if scc_map.contains_key(&r) {
            for c in scc_map.get(&r).unwrap() {
                ans.insert(*c);
            }
        } else {
            ans.insert(r);
        }
    }
    let mut vec_ans: Vec<usize> = ans.into_iter().collect();
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
        pairs.entry(manti).or_default().insert(manto);
        pairs_rev.entry(manto).or_default().insert(manti);
        starts.remove(&manto);
    }

    writeln!(writer, "{}", solution(n, pairs, starts, pairs_rev)).unwrap();
    writer.flush().unwrap();
}
