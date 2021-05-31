use std::io::{stdin};

struct UnionFind {
    p: Vec<usize>
}

impl UnionFind {
    fn new(s: usize) -> UnionFind {
        let p = vec![0; s];
        UnionFind { 
            p
        }
    }

    fn find(&mut self, a: usize) -> usize {
        if self.p[a] < 0 {
            return a
        }
        self.p[a] = self.find(self.p[a]);
        self.p[a]
    }

    fn union(&mut self, mut a: usize, mut b: usize) -> bool {
        a = self.find(a);
        b = self.find(b);
        if a == b {
            return false
        }
        if self.p[a] < self.p[b] {
            self.p[a] += self.p[b];
            self.p[b] = a;
        } else {
            self.p[b] += self.p[a];
            self.p[a] = b;
        }
        true
    }

    fn size(&mut self, a: usize) -> usize {
        self.p[self.find(a)]
    }
}


fn main() {
    let t: u128;
    let mut line = String::new();
    stdin().read_line(&mut line).expect("can't read T.");
    t = line.trim().parse().expect("can't parse to int.");
    for _ in 0..t {
        let f: usize;
        let mut line = String::new();
        stdin().read_line(&mut line).expect("can't read f.");
        f = line.trim().parse().expect("can't parse to int.");

        let mut friends: Vec<Vec<String>> = vec![Vec::new(); f];
        for i in 0..f {
            let mut line = String::new();
            stdin().read_line(&mut line).expect("can't read friends");

            line.split_whitespace()
                .map(String::from)
                .for_each(|x| friends[i].push(x))
        }
        println!("{:?}", friends);
    }
}