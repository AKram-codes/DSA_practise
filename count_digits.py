def iterative_count_digits(n):
    #time complexity is O(d) where d is the number of digits in n
    #space complexity is O(1)
    count = 0
    while n > 0:
        count += 1
        n = n//10
    return count
def string_count_digits(n):
    #time complexity is O(d) where d is the number of digits in
    #space complexity is O(log(n))
    return len(str(n))
import math
def math_count_digits(n):
    #time complexity is O(1)
    #space complexity is O(1)
    return math.floor(math.log10(n))+1
def main():
    print(iterative_count_digits(12345))
    print(string_count_digits(12345))
    print(math_count_digits(12345))
if __name__ == "__main__":
    main()