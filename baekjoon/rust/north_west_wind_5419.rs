use std::collections::{BTreeMap, HashMap, HashSet};
use std::io::{stdin, stdout, BufRead, BufReader, BufWriter, Write};

struct BIT {
    n: isize,
    bit: Vec<isize>,
}

impl BIT {
    fn new(n: isize) -> BIT {
        BIT {
            n: n,
            bit: vec![0; (n + 1) as usize],
        }
    }

    fn update(&mut self, mut p: isize, v: isize) {
        while p <= self.n {
            self.bit[p as usize] += v;
            p += p & (-p);
        }
    }

    fn _query(&self, mut b: isize) -> isize {
        let mut s = 0;
        while b > 0 {
            s += self.bit[b as usize];
            b -= b & (-b);
        }
        s
    }

    fn query(&self, a: isize, b: isize) -> isize {
        self._query(b) - self._query(a - 1)
    }
}

fn solution(n: i64, mut islands: BTreeMap<i64, Vec<i64>>, xs: HashMap<i64, i64>) -> String {
    let mut ans = 0;
    let mut bit = BIT::new((n + 1) as isize);

    for (_key, value) in islands.iter_mut() {
        value.sort_unstable();
        for x in value {
            ans += bit.query(1, *xs.get(&x).unwrap() as isize);
            bit.update(*xs.get(&x).unwrap() as isize, 1);
        }
    }
    String::from(ans.to_string())
}

fn main() {
    let mut reader = BufReader::new(stdin());
    let mut writer = BufWriter::new(stdout());
    let mut buffer = String::new();

    reader.read_line(&mut buffer).unwrap();
    let t = buffer.trim().parse::<i64>().unwrap();

    for _ in 0..t {
        buffer.clear();
        reader.read_line(&mut buffer).unwrap();
        let n = buffer.trim().parse::<i64>().unwrap();

        let mut xs_set = HashSet::<i64>::new();
        let mut xs = HashMap::<i64, i64>::new();
        let mut islands = BTreeMap::<i64, Vec<i64>>::new();

        for _ in 0..n {
            buffer.clear();
            reader.read_line(&mut buffer).unwrap();
            let pos = buffer
                .trim()
                .split_whitespace()
                .map(|x| x.parse::<i64>().unwrap())
                .collect::<Vec<_>>();
            xs_set.insert(pos[0]);
            if let Some(v) = islands.get_mut(&(-pos[1])) {
                v.push(pos[0])
            } else {
                islands.insert(-pos[1], vec![pos[0]]);
            }
        }
        let mut index = 1;
        let mut xs_vec = xs_set.into_iter().collect::<Vec<_>>();
        xs_vec.sort_unstable();
        for x in xs_vec {
            xs.insert(x, index);
            index += 1;
        }

        writeln!(writer, "{}", solution(n, islands, xs)).unwrap();
        writer.flush().unwrap();
    }
}
