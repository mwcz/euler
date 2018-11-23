// Problem
//
// The sum of the squares of the first ten natural numbers is,
// 1^2 + 2^2 + ... + 10^2 = 385
//
// The square of the sum of the first ten natural numbers is,
// (1 + 2 + ... + 10)^2 = 55^2 = 3025
//
// Hence the difference between the sum of the squares of the first ten natural numbers and the
// square of the sum is 3025 − 385 = 2640.
//
// Find the difference between the sum of the squares of the first one hundred natural numbers and
// the square of the sum.

extern crate euler;

fn main() {
    let max = 100;
    let ints = 1..=max;
    let squares = ints.clone().map(|n| n * n);

    // sum of the squares
    let ss = squares.fold(0, |a, b| a + b);
    let sss = (ints.fold(0, |a, b| a + b) as u64).pow(2);

    println!("{:#?}", sss - ss);
}
