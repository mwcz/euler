/// What is the n'th digit of a given number?
/// Indexing for the requested digit starts with 0 at the least significant digit.  For example, digit(54321, 2) will return 3.
pub fn digit(n: u128, d: u32) -> u8 {
    return ((n / (10 as u128).pow(d)) % 10) as u8;
}

/// Get the nth Fibonacci number.
pub fn fib(n: i32) -> i64 {
    let mut f1: i64 = 0;
    let mut f2: i64 = 1;
    let mut ft: i64;
    let mut i: i32 = n - 1;

    while i > 0 {
        ft = f2;
        f2 = f1 + f2;
        f1 = ft;
        i -= 1;
    }

    return f2;
}

/// Is the given number a palindrome?
pub fn is_palindrome(n: u128) -> bool {
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

/// Prime number generation and operations.
pub fn primes(count: u128) -> Vec<u128> {
    let mut ps: Vec<u128> = vec![];
    let mut sieve = vec![true; count as usize];

    for p in 2..count {
        if sieve[p as usize] {
            ps.push(p);
            for i in (p * p..count).step_by(p as usize) {
                sieve[i as usize] = false;
            }
        }
    }

    return ps;
}

/// Is a number prime?
pub fn is_prime(n: u128) -> bool {
    if n == 2 {
        return true;
    }
    if n == 3 {
        return true;
    }
    if n % 2 == 0 {
        return false;
    }
    if n % 3 == 0 {
        return false;
    }

    let mut i = 5;
    let mut w = 2;

    while i * i <= n {
        if n % i == 0 {
            return false;
        }

        i += w;
        w = 6 - w;
    }

    return true;
}

/// What are the prime factors of a given number? (Pollard rho algorithm)
// TODO: WHY does this output 8 as a factor for 8?  P Rho isn't supposed to generate trivial
pub fn p_rho(n: u128) -> u128 {
    if n == 0 {
        return 0;
    } else if n == 1 {
        return 1;
    } else if n == 2 {
        return 2;
    } else {
        let mut x_fixed: i128 = 2;
        let mut cycle_size = 2;
        let mut x: i128 = 2;
        let mut factor = 1;

        while factor == 1 {
            let mut count = 1;
            while count <= cycle_size && factor <= 1 {
                x = (x * x + 1) % (n as i128);
                factor = gcd((x - x_fixed).abs() as u128, n);
                count += 1;
            }
            cycle_size *= 2;
            x_fixed = x;
        }
        return factor;
    }
}

/// What is the greatest common denominator of two numbers?
pub fn gcd(a_in: u128, b_in: u128) -> u128 {
    let mut a = a_in;
    let mut b = b_in;
    while a % b != 0 {
        let tmp = b;
        b = a % b;
        a = tmp;
    }
    return b;
}
