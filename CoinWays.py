total = 10

print("Ways to make Rs.10:")
for ten in range(0, total//10 + 1):
    for five in range(0, (total - 10*ten)//5 + 1):
        for two in range(0, (total - 10*ten - 5*five)//2 + 1):
            for one in range(0, (total - 10*ten - 5*five - 2*two) + 1):
                if 10*ten + 5*five + 2*two + one == total:
                    print(f"10s:{ten}, 5s:{five}, 2s:{two}, 1s:{one}")
