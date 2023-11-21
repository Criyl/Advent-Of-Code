fn solve(_input: &str) -> String {
    let result = "Hello, World";
    println!("{}", result);
    return String::from(result);
}

fn main() {
    solve("Actual Case");
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_solve() {
        assert_eq!(solve("Test Case 1"), String::from("Hello, World"));
    }
}
