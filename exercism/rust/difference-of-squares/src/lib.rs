pub fn square_of_sum(n: u32) -> u32 {
    // unimplemented!("square of sum of 1...{}", n)
    if n <= 1 {
        1
    } else {
        (0..n + 1).sum::<u32>().pow(2)
    }
}

pub fn sum_of_squares(n: u32) -> u32 {
    if n <= 1 {
        1
    } else {
        (0..n + 1).fold(0, |a, b| a + b.pow(2))
    }
}

pub fn difference(n: u32) -> u32 {
    square_of_sum(n) - sum_of_squares(n)
}
