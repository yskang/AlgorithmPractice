fn main() {
    let length = 50;
    let width = 30;

    println!("xxxx");

    println!(
        "The area of the rectangle is {} square pixels.",
        area(length, width)
    );

    println!(
        "The area of the rectangle is {} square pixels.",
        area2(&Rectangle{width: 10, height: 20})
    );

    let square = Rectangle{width: 100, height: 20};

    println!("{:#?}", square);

    println!("area is {}", square.area());

    let s = Rectangle::new(100, 200);

    println!("{:#?}", s);

    let sq = Rectangle::square(20);
    println!("square is {:?}", sq);

    let four = IpAddrKind::v4;
    let six = IpAddrKind::v6;
    
    let home = IpAddr::v4(127, 0, 0, 1);
    let other_home = IpAddr::v6(String::from("::1"));

    println!("{:?}", home);
    println!("{:?}", Message::Quit);
    println!("{:?}", Message::Write(String::from("Hello World")));
    println!("{:?}", Message::Move{x:10, y:20});
    println!("{:?}", Message::ChangeColor(255, 255, 30));

    let q = Message::Quit;
    let w = Message::Write(String::from("this is a message."));

    q.call();
    w.call();

    let some_number = Some(5);
    let some_string = Some("a string");

    let absent_numbere: Option<i32> = None;
    
    let x: i8 = 5;
    let y: Option<i8> = Some(5);

    let sum = x + y.unwrap();
    println!("{}", sum);

    println!("{}", value_in_cents(Coin::Penny));

    let some_u8_value = Some(3u8);
    if let Some(3) = some_u8_value {
        println!("three");
    }

    let coin = Coin::Quarter(String::from("Califonia"));
    
    let mut count = 0;
    // match coin {
        //     Coin::Quarter(state) => println!("State quarter from {:?}!", state),
        //     _ => count += 1,
        // }

    if let Coin::Quarter(state) = coin {
        println!("State quarter from {:?}!", state);
    } else {
        count += 1;
    }

    println!("New build 2");
}

fn value_in_cents(coin: Coin) -> u32 {
    match coin {
        Coin::Penny => {
            println!("Lucky penny!");
            1
        },
        Coin::Nickel => 5,
        Coin::Dime => 10,
        Coin::Quarter(state) => {
            println!("State quarter from {:?}!", state);
            25
        },
    }
}

#[derive(Debug)]
enum Coin {
    Penny,
    Nickel,
    Dime,
    Quarter(String),
}

#[derive(Debug)]
enum Message {
    Quit,
    Move {x: i32, y: i32},
    Write(String),
    ChangeColor(i32, i32, i32),
}

impl Message {
    fn call(&self) {
        println!("{:?}", &self);
    }
}

#[derive(Debug)]
enum IpAddr {
    v4(u8, u8, u8, u8),
    v6(String),
}

#[derive(Debug)]
enum IpAddrKind {
    v4,
    v6,
}

#[derive(Debug)]
struct Rectangle {
    width: u32,
    height: u32,
}

impl Rectangle {
    fn new(width: u32, height: u32) -> Rectangle {
        Rectangle { width: width, height: height }
    }
    fn square(size: u32) -> Rectangle {
        Rectangle { width: size, height: size}
    }
    fn area(&self) -> u32 {
        self.height * self.width
    }
}

fn area(length: u32, width: u32) -> u32 {
    length * width
}

fn area2(square: &Rectangle) -> u32 {
    square.width * square.height
}