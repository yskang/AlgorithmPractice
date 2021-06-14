// Title: 스텍 수열
// Link: https://www.acmicpc.net/problem/1874

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

fn main() {
    let mut reader = BufReader::new(stdin());
    let mut writer = BufWriter::new(stdout());

    let n = read_to_tuple!(reader, i64);
    let mut nums: Vec<i64> = Vec::new();

    for _ in 0..n {
        nums.push(read_to_tuple!(reader, i64));
    }

    nums.reverse();
    let mut i = 1;
    let mut count = 1;
    let mut result = vec!["+"];
    let mut stack = vec![1];

    loop {
        if !stack.is_empty() && stack.last().unwrap() == nums.last().unwrap() {
            stack.pop();
            nums.pop();
            result.push("-");
            if count == n {
                break;
            }
            count += 1;
        } else {
            i += 1;
            stack.push(i);
            result.push("+");
            if i > n {
                result.clear();
                result.push("NO");
                break;
            }
        }
    }

    writeln!(writer, "{}", result.join("\n")).unwrap();
    writer.flush().unwrap();
}
