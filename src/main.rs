use colored::Colorize;
use std::{
    io::{stdout, Write},
    thread::sleep,
    time,
};

const SPACE_COUNT: i8 = 10;
const TREE_SIZE: i8 = 4;
const OFFSET: i8 = 32;

fn main() {
    draw_tree();
}

fn draw_tree() {
    draw_top();
    draw_base();
}

fn draw_top() {
    for i in 0..TREE_SIZE {
        draw_triangular_shape(i);
    }
}

fn draw_base() {
    let star_count = TREE_SIZE + 1;

    for _t in 0..TREE_SIZE {
        for _o in 0..OFFSET - TREE_SIZE / 2 {
            print(" ");
        }

        for _s in 0..SPACE_COUNT / 2 {
            print(" ");
        }

        for _s in 0..star_count {
            print_with_delay("*".truecolor(218, 88, 66), 25);
        }

        print("\n")
    }
}

fn draw_triangular_shape(step: i8) {
    let mut tmp_space_count = SPACE_COUNT;
    let mut star_count: i8 = 1 + step * 2;

    while tmp_space_count > 0 {
        if tmp_space_count <= 2 {
            star_count += 2;
            tmp_space_count -= 2;
        }

        for _o in 0..OFFSET - step {
            print(" ");
        }

        for _s in 0..tmp_space_count / 2 {
            print(" ");
        }

        for _s in 0..star_count {
            print_with_delay("*".truecolor(99, 215, 81), 25);
        }

        print("\n");

        tmp_space_count -= 2;
        star_count += 2;
    }
}

fn print_with_delay<T: std::fmt::Display>(printable: T, delay: u64) {
    print(printable);
    stdout().flush().expect("Failed to flush!");
    sleep(time::Duration::from_millis(delay));
}

fn print<T: std::fmt::Display>(printable: T) {
    print!("{}", printable);
    stdout().flush().expect("Failed to flush!");
}
