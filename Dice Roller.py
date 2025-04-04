import time
import random

#    ●  ┌  ─  │  ┐  └  ┘
diceCreation = {
    1: (
        "┌───────┐",
        "│       │",
        "│   ●   │",
        "│       │",
        "└───────┘"
    ),
    2: (
        "┌───────┐",
        "│ ●     │",
        "│       │",
        "│     ● │",
        "└───────┘"
    ),
    3: (
        "┌───────┐",
        "│ ●     │",
        "│   ●   │",
        "│     ● │",
        "└───────┘"
    ),
    4: (
        "┌───────┐",
        "│ ●   ● │",
        "│       │",
        "│ ●   ● │",
        "└───────┘"
    ),
    5: (
        "┌───────┐",
        "│ ●   ● │",
        "│   ●   │",
        "│ ●   ● │",
        "└───────┘"
    ),
    6: (
        "┌───────┐",
        "│ ●   ● │",
        "│ ●   ● │",
        "│ ●   ● │",
        "└───────┘"
    )
}

dice = []
total = 0
while True:
    try:
        n = int(input("How many dice? (1-4) : "))
        if n > 0 and n < 5:
            break
        else:
            print("Dice out of range")
    except ValueError:
        print("Invalid Input!")
for i in range(n):
    dice.append(random.randint(1, 6))
for i in range(n):
    for line in diceCreation.get(dice[i]):
        print(line)
print()
print("Calculating total...")
time.sleep(2)
total=sum(dice)
print(f"The total is {total}")




















# for i in range(n):
#     for line in diceCreation.get(dice[i]):
#         print(line)