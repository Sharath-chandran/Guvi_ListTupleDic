# Total need to be Rs.10/-
Total_Rupee = 10

# Coins used 1/-, 2/-, 5/-, 10/-
# while using 10/- coin
for ten in range(0, Total_Rupee//10 + 1):
    # while using 5/- coin
    for five in range(0, (Total_Rupee - 10*ten)//5 + 1):
        # while using 2/- coin
        for two in range(0, (Total_Rupee - 10*ten - 5*five)//2 + 1):
            # while using 1/- coin
            for one in range(0, (Total_Rupee - 10*ten - 5*five - 2*two) + 1):

                if 10*ten + 5*five + 2*two + one == Total_Rupee:
                    print(f"10s:{ten}, 5s:{five}, 2s:{two}, 1s:{one}")

print("These are the possible ways to make Rs.10/-")