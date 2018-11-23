// Problem 3
//
// The prime factors of 13195 are 5, 7, 13 and 29.
// What is the largest prime factor of the number 600851475143 ?

extern crate euler;

use euler::p_rho;

fn main() {
    let mut n: u128 = 600851475143;

    loop {
        let f = p_rho(n);
        if n == f {
            println!("{:?}", f);
            break;
        }
        n = n / f;
    }
}
