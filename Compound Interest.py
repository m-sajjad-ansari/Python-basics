import time
while True:
    try:
        principle=float(input("Enter principle amount : "))
        if principle>=0:
            break
        else:
            print("Principle can never be negative")
    except ValueError:
        print("Invalid input")

while True:
    try:
        t=float(input("Enter total time in years : "))
        if t>=0:
            break
        else:
            print("Time can never be negative")
    except ValueError:
        print("Invalid input")

while True:
    try:
        rate=float(input("Enter rate amount : "))
        if rate>=0:
            break
        else:
            print("Rate can never be negative")
    except ValueError:
        print("Invalid input")

result=principle*pow((1+(rate/100)),t)
result=round(result,2)
print("Calculating amount...")
time.sleep(2)
print(f"Compounded amount after {t} years is {result}")