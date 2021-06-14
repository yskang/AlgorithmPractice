use std::collections::BTreeMap;

fn main() {
    let a = (0..10).collect::<Vec<i32>>();
    let b = vec![false; 10];
    let c = a.iter().zip(b);

    let mut d = c.collect::<Vec<_>>();
    d.sort_by_key(|x| -1 * x.0);
    println!("{:?}", d);

    let word = vec!['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i'];
    println!("{:?}", word);
    let iter = word[2..4].iter();

    let s = String::from("helloWorld");
    let vs = s.split("").collect::<Vec<_>>();
    fun_a(&vs);
    fun_a(&vs);
    fun_a(&vs);
    fun_a(&vs);
    fun_a(&vs);
    fun_a(&vs);
    fun_a(&vs);

    let mut v: Vec<usize> = vec![1; 10];
    v[2] = 200;
    println!("{:?}", v);

    println!("{}", v.last().unwrap());
}

fn fun_a(s: &Vec<&str>) {
    println!("{:?}", s);
    println!("{}", s.join(""));
}