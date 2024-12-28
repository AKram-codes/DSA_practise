def fact_iterative(n):
    #time complexity is O(n)
    #space complexity is O(1)
    result = 1
    for i in range(1, n+1):
        result *= i
    return result

def fact_recursive(n):
    #time complexity is O(n)
    #space complexity is O(n)
    if n == 0 or n == 1:
        return 1
    return n * fact_recursive(n-1)
cache = {}
def fact_cache(n):
    #time complexity is O(n)
    #space complexity is O(n)
    if n in cache:
        return cache[n]
    if n == 0 or n == 1:
        return 1
    cache[n] = n * fact_cache(n-1)
    return cache[n]
def fact_precompute(n):
    #time complexity is O(1) after precomputation
    #space complexity is O(n)
    factorials = [1]*(n+1)
    for i in range(1,n+1):
        factorials[i] = factorials[i-1]*i
    return factorials[n]
def main():
    print(fact_iterative(5))
    print(fact_recursive(5))
    print(fact_cache(5))
    print(fact_precompute(5))
if __name__ == "__main__":
    main()