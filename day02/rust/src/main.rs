use std::fs::File;
use std::io::Read;

fn main() {
    part_one(read_input());
    part_two(read_input());
}

fn read_input() -> String{
    let mut file = File::open("../input.txt").expect("file not found");
    let mut content = String::new();
    file.read_to_string(&mut content).expect("Could not read file");
    content
}

fn char_to_int(c : char) -> u32{
    let mut string = String::new();
    string.push(c);
    string.parse().expect("Cannot parse: Not a number!")
}

fn part_one(input : String){
    println!("Here comes day 2 part one");
}

fn part_two(input : String){
    println!("Here comes day 2 part two");
}
