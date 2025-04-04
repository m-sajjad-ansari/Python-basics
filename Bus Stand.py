import time

menu = {
    "Juice": 30,
    "Burger": 40,
    "Kulfi": 25,
    "Pizza": 100
}
items = []
print("----------My menu----------")
print("Name\t:\tPrice in Rupees")
for key, value in menu.items():
    print(f"{key}\t:\t{value}")
print("---------------------------")
while True:
    try:
        item = input("Item you want to add in cart (or q to exit) : ").capitalize()
        if item == 'Q':
            break
        elif menu.get(item) is not None:
            items.append(item)
        else:
            print("Item not found!")
    except ValueError:
        print("Invalid input!")
total = 0
print("Your order is : ")
print(items)
for i in range(len(items)):
    total += menu.get(items[i])
print("Calculating total...")
time.sleep(2)
print(f"Your total is Rs {total}")