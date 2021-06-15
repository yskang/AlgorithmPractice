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

type Func_x_n = fn(u128, u128) -> u128;
type Func_n_f = fn(u128, Func_x_n) -> u128;

fn gcd(mut a: u128, mut b: u128) -> u128 {
    if a == 0 {
        return b;
    }
    return gcd(b % a, a);
}

fn f1(mut x: u128, mut n: u128) -> u128 {
    ((x * x) + 1) % n
}

fn f2(mut x: u128, mut n: u128) -> u128 {
    ((x * x) + 2) % n
}

fn f3(mut x: u128, mut n: u128) -> u128 {
    ((x * x) + 3) % n
}

fn rho(mut n: u128, mut f: Func_x_n) -> u128 {
    let mut x = 2;
    let mut y = 2;
    let mut d = 1;
    let mut count = 0;
    while d == 1 {
        x = f(x, n);
        y = f(f(y, n), n);
        if x > y {
            d = gcd(x - y, n);
        } else {
            d = gcd(y - x, n);
        }
        count += 1;
        if count > 100000 {
            return 0;
        }
    }
    if d == n {
        return 0;
    }
    return d;
}

fn get_factoring(n: u128, s: &mut HashSet<u128>, f_dict: &mut HashMap<u128, bool>) {
    f_dict.insert(n, true);

    let f = rho(n, f1);

    if n == 4 || n == 8 || n == 16 {
        s.insert(2);
        return;
    } else if n == 25 || n == 125 {
        s.insert(5);
        return;
    } else if n == 9 || n == 27 || n == 81 {
        s.insert(3);
        return;
    }

    if f == 0 {
        let f_2 = rho(n, f2);
        let f_3 = rho(n, f3);
        if ((f_2 == f_3) && (f_3 == f)) && n != 4 && n != 8 {
            s.insert(n);
        } else {
            if f_2 != 0 {
                let a = n / f_2;
                let b = f_2;
                if !f_dict.contains_key(&a) {
                    get_factoring(a, s, f_dict);
                }
                if !f_dict.contains_key(&b) {
                    get_factoring(b, s, f_dict);
                }
            }
            if f_3 != 0 {
                let a = n / f_3;
                let b = f_3;
                if !f_dict.contains_key(&a) {
                    get_factoring(a, s, f_dict);
                }
                if !f_dict.contains_key(&b) {
                    get_factoring(b, s, f_dict);
                }
            }
        }
    } else {
        if f != 0 {
            let a = n / f;
            let b = f;
            if !f_dict.contains_key(&a) {
                get_factoring(a, s, f_dict);
            }
            if !f_dict.contains_key(&b) {
                get_factoring(b, s, f_dict);
            }
        }
    }
}

fn num_gcd(n: u128) -> u128 {
    if n == 1 {
        return 1;
    }
    let mut factors = HashSet::<u128>::new();
    let mut f_dict = HashMap::<u128, bool>::new();
    get_factoring(n, &mut factors, &mut f_dict);
    let mut up = 1;
    let mut down = 1;
    for f in factors {
        up *= (f - 1);
        down *= f;
    }
    n * up / down
}

fn main() {
    let mut reader = BufReader::new(stdin());
    let mut writer = BufWriter::new(stdout());

    let n = read_to_tuple!(reader, u128);
    writeln!(writer, "{}", num_gcd(n));
    writer.flush().unwrap();
}
