fn fib(n: i32) -> i64 {
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
    f2
}

fn even(n: i64) -> bool {
    n % 2 == 0
}

fn fibsum() -> i64 {
    let mut sum: i64 = 0;
    let mut f: i64 = 0;
    let mut i: i32 = 1;
    while f < 4000000 {
        if even(f) {
            sum += f;
        }
        f = fib(i);
        i += 1;
    }
    sum
}

fn main() {
    println!("the answer is {}", fibsum());
}
