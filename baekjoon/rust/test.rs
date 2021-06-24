use std::collections::{BTreeMap, HashMap, HashSet};
use std::mem::swap;

#[derive(Debug)]
struct MyBox {
    key: usize,
    set: HashSet<usize>,
}

impl MyBox {
    fn new(key: usize, set: HashSet<usize>) -> MyBox {
        MyBox { key: key, set: set }
    }

    fn extend(&mut self, other: &MyBox) {
        self.set.extend(other.set);
    }
}

fn main() {
    let mut v: Vec<MyBox> = Vec::new();
    v.push(MyBox::new(0, HashSet::new()));
    v.push(MyBox::new(1, HashSet::new()));
    v.push(MyBox::new(2, HashSet::new()));
    v.push(MyBox::new(3, HashSet::new()));
    v.push(MyBox::new(4, HashSet::new()));
    v.push(MyBox::new(5, HashSet::new()));

    println!("{:?}", v);

    v[0].set.insert(0);
    v[0].set.insert(1);
    v[0].set.insert(2);
    v[1].set.insert(2);
    v[1].set.insert(3);
    v[1].set.insert(4);
    v[1].set.insert(5);

    println!("{:?}", v);

    v[0].extend(&v[1]);
}
