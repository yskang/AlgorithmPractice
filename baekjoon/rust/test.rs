use std::collections::{BTreeMap, HashMap, HashSet};
use std::mem::swap;

fn main() {
    let mut v: Vec<(&str, usize)> = Vec::new();
    v.push(("Hello", 1));
    v.push(("World", 2));
    v.push(("Good", 3));
    v.push(("Morning", 4));
    v.push(("YSKang", 5));
    println!("{:?}", v);


    let h: HashMap<i64, i64> = HashMap::new();
    h.insert(1, 2);
    h.insert(3, 4);
    for 
}

fn fun_a(s: &Vec<&str>) {
    println!("{:?}", s);
    println!("{}", s.join(""));
}
