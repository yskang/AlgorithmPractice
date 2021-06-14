// Title: GCD(n, k) = 1
// Link: https://www.acmicpc.net/problem/13926
// Link: https://www.acmicpc.net/problem/11689

use std::collections::{BTreeMap, HashMap, HashSet};
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

fn rho(n, f1) {
    
}

fn get_factoring(n: i64, s: &HashSet<i64>, f_dict: &HashMap<i64, bool>) {
    f_dict.insert(n, true);
    let f = rho(n, f1);

    if n == 4 || n == 8 or n == 16 {
        s.push(2);
        return
    } else if n == 25 || n == 125 {
        s.put(5);
        return
    } else if n == 9 || n == 27 || n == 81 {
        s.put(3);
        return
    }

    if 
}

fn num_gcd(n: i64) -> i64 {
    if n == 1 {
        return 1;
    }
    let mut factors = HashSet::<i64>::new();
    let mut f_dict = HashMap::<i64, bool>::new();
    get_factoring(n, &factors, &f_dict);
    let up = 1;
    let down = 1;
    for f in factors {
        up *= (f - 1);
        down *= f;
    }
    (n * up / down) as i64
}


fn main() {
    let mut reader = BufReader::new(stdin());
    let mut writer = BufWriter::new(stdout());

    let n = read_to_tuple!(reader, i64);
    writeln!(writer, "{}", num_gcd(n)).unwrap();
    writer.flush().unwrap();
}