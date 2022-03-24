use std::io::{stdin, stdout, BufRead, BufReader, BufWriter, Write};
use std::collections::HashMap;

struct UnionFind {
    sizes: Vec<usize>,
    rank: Vec<usize>,
    parent: Vec<usize>
}

impl UnionFind {
    fn new(n: usize) -> UnionFind {
        UnionFind {
            sizes : vec![1; n],
            rank : vec![1; n],
            parent : (0..n).collect(),
        }
    }

    fn find(&mut self, x: usize) -> usize {
        if self.parent[x] != x {
            self.parent[x] = self.find(self.parent[x]);
        }
        self.parent[x]
    }

    fn union(&mut self, x: usize, y:usize) {
        let xset = self.find(x);
        let yset = self.find(y);

        if xset == yset {
            return;
        }

        if self.rank[xset] < self.rank[yset] {
            self.parent[xset] = yset;
            self.sizes[yset] += self.sizes[xset];
        } else if self.rank[xset] > self.rank[yset] {
            self.parent[yset] = xset;
            self.sizes[xset] += self.sizes[yset];
        } else {
            self.parent[yset] = xset;
            self.rank[xset] = self.rank[yset] + 1;
            self.sizes[xset] += self.sizes[yset];
        }
    }

    fn get_size(&mut self, x: usize) -> usize {
        let i = self.find(x);
        self.sizes[i]
    }
}


fn main() {
    let mut buf = BufReader::new(stdin());
    let mut out = BufWriter::new(stdout());
    let t: u128;
    let mut line = String::new();
    
    buf.read_line(&mut line).unwrap();
    t = line.trim().parse().unwrap();

    for _ in 0..t {
        let mut name_to_int = HashMap::<String, usize>::new();
        let f: usize;
        let mut line = String::new();
        buf.read_line(&mut line).unwrap();
        f = line.trim().parse().unwrap();

        let mut disjoint = UnionFind::new(2*f+1);

        for _ in 0..f {
            let mut line = String::new();
            buf.read_line(&mut line).unwrap();
            let friends = line
                            .split_whitespace()
                            .map(|x| String::from(x))
                            .collect::<Vec<_>>();
            
            match name_to_int.get(&friends[0]) {
                Some(_) => (),
                None => {
                   name_to_int.insert(friends[0].to_string(), name_to_int.len());
                }
            }
 
            match name_to_int.get(&friends[1]) {
                Some(_) => (),
                None => {
                    name_to_int.insert(friends[1].to_string(), name_to_int.len());
                }
            }

            disjoint.union(*name_to_int.get(&friends[0]).unwrap(), *name_to_int.get(&friends[1]).unwrap());
            writeln!(out, "{}", disjoint.get_size(*name_to_int.get(&friends[0]).unwrap())).unwrap();
        }
    }
    out.flush().unwrap();
}