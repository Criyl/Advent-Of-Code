fn solve(_input: &str) -> String {
    let result = "Hello, World";
    return String::from(result);
}

fn main() {
    println!("{}", solve("Actual Case"));
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_solve() {
        assert_eq!(solve("Test Case 1"), String::from("Hello, Place"));
    }
}
