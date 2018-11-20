/* A crate for prime number operations. */

pub mod prime {
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

    /**
     * Pollard's rho algorithm for prime factorization
     *
     * TODO: WHY does this output 8 as a factor for 8?  P Rho isn't supposed to generate trivial
     * factors.
     */

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
}
