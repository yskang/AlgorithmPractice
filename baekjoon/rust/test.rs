use std::collections::BTreeMap;

fn main() {
    let mut map = BTreeMap::new();
    map.insert(3, "c");
    map.insert(0, "x");
    map.insert(2, "a");

    for (key, value) in map.iter() {
        println!("{} {}", key, value);
    }

    let mut iter = map.iter_mut();
    while let Some((k, v)) = iter.next() {
        println!("{} {}", k, v);
    }

    map.insert(0, "z");
    println!("{:?}", map);
}
