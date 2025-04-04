import time
foods=[]
prices=[]
total=0

while True:
    try:
        item=input("Item you wanted to purchase (or Q to quit): ").capitalize()
        if item=='Q':
            break
        else:
            price = float(input(f"Price of {item} in $ : "))
            if price>=0:
                foods.append(item)
                prices.append(price)
            else:
                print("Price of an item can never be negative!")
    except ValueError:
        print("Invalid input!")

print("Calculating your total...")
time.sleep(2)
total=sum(prices)
print(f"Your total bill is {total}")