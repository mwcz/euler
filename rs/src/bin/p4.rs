// Problem 4
//
// A palindromic number reads the same both ways. The
// largest palindrome made from the product of two
// 2-digit numbers is 9009 = 91 * 99.
//
// Find the largest palindrome made from the product
// of two 3-digit numbers.

extern crate euler;

use euler::num::digit;

fn main() {
    fn is_palindrome(n: u128) -> bool {
        let mag = (n as f64).log10() as u128;
        let halfmag = 1 + mag / 2;
        for i in 0..halfmag {
            let d1 = digit(n, i as u32);
            let d2 = digit(n, (mag - i) as u32);

            if d1 != d2 {
                return false;
            }
        }

        return true;
    }

    let mut largest = 0;

    for n in 100..999 {
        for m in 100..999 {
            let nm = n * m;
            let p = is_palindrome(nm);
            if nm > largest && p {
                largest = nm;
            }
        }
    }

    println!("{}", largest);
}
