def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

nums = [10, 501, 22, 37, 100, 999, 87, 351]
prime_nums = [n for n in nums if is_prime(n)]

print("Prime Numbers:", prime_nums)
print("Count of Prime Numbers:", len(prime_nums))
