#8.Sum of numbers at prime factors
#test case not passed

def is_prime(n):
    """Check if a number is prime."""
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def prime_factors(n):
    """Return a list of prime factors of n."""
    factors = []
    for i in range(2, n + 1):
        while n % i == 0 and is_prime(i):
            if i not in factors:  # Avoid duplicates
                factors.append(i)
            n //= i
    return factors

def sum_of_prime_factors(n):
    """Return the sum of prime factors of n."""
    factors = prime_factors(n)
    return sum(factors)

# Example usage
number = int(input("Enter a number: "))
result = sum_of_prime_factors(number)
print(f"The sum of prime factors of {number} is: {result}")
