extern crate tuple_list;

use std::io;

macro_rules! parse_input {
    ($x:expr, $t:ident) => ($x.trim().parse::<$t>().unwrap())
}

fn main() {
    use tuple_list::tuple_list;
    let mut input_line = String::new();
    io::stdin().read_line(&mut input_line).unwrap();
    let inputs = input_line.split(" ").collect::<Vec<_>>();
    println!("{}", parse_input!(inputs[0], String));
    println!("{}", parse_input!(inputs[1], String));

    let a;
    let b;
    let c;

    let tuple_list!(a, b, c) = tuple_list!(10, false, "foo");
    println!("{}, {}, {}", a, b, c);
}