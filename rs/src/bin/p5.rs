// Problem 5
//
// 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any
// remainder.
//
// What is the smallest positive number that is evenly divisible by all of the numbers from 1 to
// 20?

extern crate euler;

fn main() {
    // smart approach, break down 2..20 into prime factors and multiply the together to get the
    // answer.

    // essential prime factors:
    // 2    2
    // 3    3
    // 4    2
    // 5    5
    // 6
    // 7    7
    // 8    2
    // 9    3
    // 10
    // 11   11
    // 12
    // 13   13
    // 14
    // 15
    // 16   2
    // 17   17
    // 18
    // 19   19
    // 20

    let a = 2 * 3 * 2 * 5 * 7 * 2 * 3 * 11 * 13 * 2 * 17 * 19;

    // brute force approach, runs in 16-17 seconds on my t450s.
    // let mut a: u128 = 0;
    // for i in 1..10000000000 {
    //     if i % 2 == 0
    //         && i % 3 == 0
    //         && i % 4 == 0
    //         && i % 5 == 0
    //         && i % 6 == 0
    //         && i % 7 == 0
    //         && i % 8 == 0
    //         && i % 9 == 0
    //         && i % 10 == 0
    //         && i % 11 == 0
    //         && i % 12 == 0
    //         && i % 13 == 0
    //         && i % 14 == 0
    //         && i % 15 == 0
    //         && i % 16 == 0
    //         && i % 17 == 0
    //         && i % 18 == 0
    //         && i % 19 == 0
    //         && i % 20 == 0
    //     {
    //         a = i;
    //         break;
    //     }
    // }

    println!("{}", a);
}
