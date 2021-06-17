use std::collections::{BTreeMap, HashMap, HashSet};
use std::mem::swap;

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

    let x = 2;
    let y = 2;
    let z = 2;
    if (x == y) && (y == z) {
        println!("it's same for all words.");
    }

    println!("{}", (10 / 3));

    let mut k = [vec![0], vec![1], vec![3]].concat();
    println!("{:?}", k);

    let aa = 10usize;
    let bb = 100usize;
    println!("{}", bb);

    let vv: Vec<usize> = vec![];
    println!("{:?}", vv);

    let mut v = vec![false; 10];
    println!("{:?}", v);
    v = vec![true; 10];
    println!("{:?}", v);

    let j = (0..10).map(|x| vec![x]).collect::<Vec<_>>();
    println!("{:?}", j);

    let ss: HashSet<usize> = (1..10).collect();
    println!("{:?}", ss);

    let mut graph: HashMap<usize, HashSet<usize>> = HashMap::new();
    println!("{:?}", graph);
    graph.insert(0, HashSet::new());
    println!("{:?}", graph);
    graph.insert(1, (1..5).collect());
    println!("{:?}", graph);

    let mut out: HashSet<usize> = [1, 2, 3].iter().cloned().collect();
    let mut out_2: HashSet<usize> = [2, 3, 4].iter().cloned().collect();
    println!("{:?}", out);
    println!("{:?}", out_2);
    out.retain(|x| !out_2.contains(x));
    println!("{:?}", out);

    let mut j = vec![0, 1, 2];
    let mut jj = vec![4, 5, 6];

    swap(&mut j, &mut jj);

    println!("{:?}", j);
}

fn fun_a(s: &Vec<&str>) {
    println!("{:?}", s);
    println!("{}", s.join(""));
}
