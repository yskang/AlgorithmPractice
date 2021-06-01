use std::io::{stdin};
use std::collections::HashMap;

struct UnionFind {
    sizes: Vec<usize>,
    rank: Vec<usize>,
    parent: Vec<usize>
}

impl UnionFind {
    fn new(&mut self, n: usize) -> UnionFind {
        self.sizes = vec![1; n];
        self.rank = vec![1; n];
        self.parent = (0..n).collect();
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
    let t: u128;
    let mut line = String::new();
    
    stdin().read_line(&mut line).expect("can't read T.");
    t = line.trim().parse().expect("can't parse to int.");
    for _ in 0..t {
        let mut name_to_int = HashMap::new();
        let f: usize;
        let mut line = String::new();
        stdin().read_line(&mut line).expect("can't read f.");
        f = line.trim().parse().expect("can't parse to int.");

        let disjoint = UnionFind::new(2*f+1);


        for i in 0..f {
            let mut line = String::new();
            stdin().read_line(&mut line).expect("can't read friends");
            let mut name_idx:Vec<usize> = Vec::new();
            line.split_whitespace()
                .map(String::from)
                .for_each(|x| {
                    match name_to_int.get_key_value(&x) {
                        // Some((k, v)) => println!("{} has value {}", k, v),
                        None => {
                                    println!("{} has no value, so create!!", x);
                                    name_to_int.insert(x, name_to_int.len());
                                },
                        _ => ()
                    };
                    name_idx.add(name_to_int.get(x).unwrap());
                });
            disjoint.union(name_to_int[0], name_to_int[1]);
        }
    }
}