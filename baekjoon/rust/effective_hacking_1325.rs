// Title: 효율적인 해킹
// Link: https://www.acmicpc.net/problem/1325

use std::collections::HashMap;
use std::io::{stdin, stdout, BufRead, BufReader, BufWriter, Write};
use std::mem::swap;
use std::cmp::max;

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

fn get_scc_iter(vertices: &mut Vec<usize>, edges: &mut HashMap<usize, HashSet<usize>) -> 


fn solution(n: usize, pairs: HashMap<usize, HashSet<usize>>, starts: HashSet<usize>, pairs_rev: HashMap<usize, HashSet<usize>>) -> String {
    let mut counts: HashMap<usize, HashSet<usize>> = HashMap::new();
    let mut nodes = (1..n+1).collect::<Vec<usize>>();
    let mut new_node = n+1;
    let mut scc_map: HashMap<usize, HashSet<usize>> = HashMap::new();

    for scc in get_scc_iter(&mut nodes, &mut pairs) {
        if scc.len() > 1 {
            scc_map.insert(new_node, HashSet::new());
            let mut outs: HashSet<usize> = HashSet::new();
            let mut ins: HashSet<usize> = HashSet::new();
            for node in scc {
                pairs.get(node).unwrap().for_each(|x| outs.push(x));
                pairs_rev.get(node).unwrap().for_each(|x| ins.push(x));
            }
            outs.retain(|x| !scc.contains(x));
            int.retain(|x| !scc.contains(x));
            outs.iter().for_each(|x| pairs.get(new_node).unwrap().push(x));

            for node in ins {
                pairs.get(node).unwrap().retain(|x| !scc.contains(x));
                pairs.get(node).unwrap().push(new_node);
            }

            for node in outs {
                pairs_rev.get(node).unwrap().retain(|x| !scc.contains(x));
                pairs_rev.get(node).unwrap().push(new_node);
            }

            counts.insert(new_node, scc);
            if ins.len() == 0 {
                starts.push(new_node);
            }
            new_node += 1;
        }
    }

    let temp: HashSet<usize> = HashSet::new();
    loop {
        for node in starts {
            for manto in pairs.get(node).unwrap() {
                if counts.get(node).unwrap().len() == 0 {
                    counts.get(node).unwrap().push(node);
                }
                if counts.get(manto).unwrap().len() == 0 {
                    counts.get(manto).unwrap().push(manto);
                }
                counts.get(node).unwrap().for_each(|x| counts.get(manto).unwrap().push(x));
                pairs_rev.get(manto).unwrap().remove(node);
                if pairs_rev.get(manto).unwrap().len() == 0 {
                    temp.push(manto);
                }
            }
        }
        swap(starts, temp);
        temp.clear();
        if starts.len() == 0 {
            break;
        }
    }

    let res: Vec<usize> = vec![];

    let counts_lens:HashMap<usize, usize> = HashMap::new();
    for node in counts {
        counts_lens.insert(node, counts.get(node).unwrap());
    }

    let mut max_count = counts_lens.values().iter().max().unwrap();
    for node in counts_lens {
        if counts_lens.get(node).unwrap() == max_count {
            res.push(node);
        }
    }
    let ans: HashSet<usize> = HashSet::new();
    for r in res {
        if scc_map.contains(r) {
            for c in scc_map.get(r).unwrap() {
                ans.push(c);
            }
        } else {
            ans.push(r);
        }
    }
    ans.sort();

    ans.iter().map(|x| x.to_string()).collect::<Vec<String>>().join(" ")
}

fn main() {
    let mut reader = BufReader::new(stdin());
    let mut writer = BufWriter::new(stdout());

    let (n, m) = read_to_tuple!(reader, usize, usize);
    let mut pairs: HashMap<usize, HashSet<usize>> = HashMap::new();
    let mut pairs_rev: HashMap<usize, HashSet<usize>> = HashMap::new();
    let mut starts: HashSet<usize> = (1..n+1).collect();

    for _ in 0..m {
        let (manti, manto) = read_to_tuple!(reader, usize, usize);
        if let Some(mantos) = pairs.get(manti) {
            mantos.push(manto);
        } else {
            pairs[manti].insert(manti, (manto..manto+1).collect());
        }
        if let Some(mantis) = pairs.get(manto) {
            mantis.push(manti);
        } else {
            pairs[manto].insert(manto, (manti..manti+1).collect());
        }
        starts.remove(manto);
    }

    writeln!(writer, "{}", solution(n, pairs, starts, pairs_rev)).unwrap(); 