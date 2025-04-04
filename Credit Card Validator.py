import time

while True:
    try:
        card = int(input("Enter the card number (do not include spaces or hyphens) : "))
        if card >= 0:
            break
        else:
            print("Invalid Card number")
    except ValueError:
        print("Card number cannot contain letters other than digits!")

cardList = str(card)
cardList = cardList[::-1]
print(cardList)
odd = 0
for i in cardList[::2]:
    odd += int(i)

even = 0
for i in cardList[1::2]:
    i = int(i) * 2
    if i >= 10:
        i = (1 + (i % 10))
    even += i

print("Validating card number...")
time.sleep(2)
if (odd + even) % 10 == 0:
    print("VALID!")
else:
    print("NOT VALID!")
