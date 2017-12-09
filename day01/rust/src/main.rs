
use std::fs::File;
use std::io::Read;

fn main() {
    //part_one(String::from("112234"));
    part_one(read_input());
}

fn read_input() -> String{
    //String::from("12345")

    let mut file = File::open("../input.txt").expect("file not found");
    let mut content = String::new();
    file.read_to_string(&mut content).expect("Could not read file");
    content
}

fn part_one(input : String){

    let input = &make_circular(&(input.trim()));
    let input = input.as_bytes();

    let mut index = 0;
    let mut checksum = 0;

    while index < input.len() - 1{
        let mut left_s = String::new();
        left_s.push(input[index] as char);
        let left_n : u32 = left_s.parse().expect("not a number");

        let mut right_s = String::new();
        right_s.push(input[index + 1] as char);
        let right_n : u32 = right_s.parse().expect("not a number");

        if left_n == right_n{
            checksum += left_n;
        }
        index += 1;
    }
    println!("{:?}", checksum);
}

fn make_circular(input : &str) -> String {
    let bytes = input.as_bytes();
    //let last = bytes[&bytes.len() - 1] as char;
    //println!("{:?}", last);
    let first = bytes[0] as char;
    let mut circ = String::from(input);
    circ.push(first);
    circ
}
