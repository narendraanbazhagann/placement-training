def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

n = int(input("Enter a number: "))
sum_primes = sum(i for i in range(2, n + 1) if is_prime(i))
print("Sum of primes up to", n, "is:", sum_primes)
