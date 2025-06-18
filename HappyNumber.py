def is_happy(n):
    seen = set()
    while n != 1 and n not in seen:
        seen.add(n)
        n = sum(int(d)**2 for d in str(n))
    return n == 1

nums = [10, 501, 22, 37, 100, 999, 87, 351]
happy_nums = [n for n in nums if is_happy(n)]

print("Happy Numbers:", happy_nums)
print("Count of Happy Numbers:", len(happy_nums))
