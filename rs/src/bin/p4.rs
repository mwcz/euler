// Problem 4
//
// A palindromic number reads the same both ways. The
// largest palindrome made from the product of two
// 2-digit numbers is 9009 = 91 * 99.
//
// Find the largest palindrome made from the product
// of two 3-digit numbers.

extern crate euler;

use euler::is_palindrome;

fn main() {
    let mut largest = 0;

    for n in 100..999 {
        for m in 100..=n {
            let nm = n * m;
            let p = is_palindrome(nm);
            if nm > largest && p {
                largest = nm;
            }
        }
    }

    println!("{}", largest);
}
