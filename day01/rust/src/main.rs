
use std::fs::File;
use std::io::Read;

fn main() {
    //part_one(String::from("112234"));
    part_one(read_input());
    part_two(read_input());
}

fn read_input() -> String{
    //String::from("12345")

    let mut file = File::open("../input.txt").expect("file not found");
    let mut content = String::new();
    file.read_to_string(&mut content).expect("Could not read file");
    content
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

fn char_to_int(c : char) -> u32{
    let mut string = String::new();
    string.push(c);
    string.parse().expect("Cannot parse: Not a number!")
}

fn part_one(input : String){

    let input = &make_circular(&(input.trim()));
    let input = input.as_bytes();

    let mut index = 0;
    let mut checksum = 0;

    while index < input.len() - 1{
        let left_n = char_to_int(input[index] as char);
        let right_n = char_to_int(input[index + 1] as char);
        if left_n == right_n{
            checksum += left_n;
        }
        index += 1;
    }
    println!("Solution part 1: {}", checksum);
}

fn part_two(input : String){
    let input = input.as_bytes();
    let mut checksum = 0;
    let mut index_left = 0;
    let mut index_right = input.len() / 2;
    while index_left < input.len() / 2 {
        let left = char_to_int(input[index_left] as char);
        let right = char_to_int(input[index_right] as char);
        if left == right{
            checksum += left*2;
        }
        index_left += 1;
        index_right += 1;
    }
    println!("Solution part 2: {}", checksum);
}
