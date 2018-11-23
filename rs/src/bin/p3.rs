// Problem 3
//
// The prime factors of 13195 are 5, 7, 13 and 29.
// What is the largest prime factor of the number 600851475143 ?

extern crate euler;

use euler::prime;

fn main() {
    let mut n: u128 = 600851475143;

    loop {
        let f = prime::p_rho(n);
        if n == f {
            println!("{:?}", f);
            break;
        }
        n = n / f;
    }

    // let primes100 = prime::primes(100);
    // println!("{:#?}", primes100);
    // for i in 1..28 {
    //     let f = prime::p_rho(i);
    //     let gcd = prime::gcd(f[0], i);
    //     println!("{} -> {:?} -> {}", i, f, gcd);
    // }
}
