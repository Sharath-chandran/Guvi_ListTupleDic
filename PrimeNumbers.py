# From the number list, Identify the Prime number
numbers = [10, 501, 22, 37, 100, 999, 87, 351]

# Defines number less than 2 is not a prime number
def is_prime(n):
    if n < 2:
        return False
# If number is divisible by any number in that range, it is not a prime number
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

prime_nums = [n for n in numbers if is_prime(n)]
print("Prime Numbers:", prime_nums)
print("Count of Prime Numbers:", len(prime_nums))
