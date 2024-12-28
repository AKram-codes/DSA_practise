def is_palindrome(x: int) -> bool:
    if x < 0 and (x % 10 == 0 and x != 0):
        return False
    rev_half = 0
    while x > rev_half:
        rev_half = rev_half * 10 + x % 10
        x = x // 10
    return x == rev_half or x == rev_half // 10
def main():
    x = 121
    print(is_palindrome(x))
    print(x)
    
if __name__ == "__main__":
    main()