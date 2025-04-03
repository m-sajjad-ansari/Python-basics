import time
print("Welcome to weight conversion program!")
time.sleep(1.3)
unit=input("Enter unit Kilogram or Pound (K or L) : ").capitalize()
while True:
    if unit=="K" or unit=="L":
        break
    else:
        unit=input("Enter K or L only : ").capitalize()

while True:
    try:
        weight=float(input("Enter Weight : "))
        if weight>=0:
            break
        else:
            print("Weight can never be negative!")
    except ValueError:
        print("Invalid Weight!")

if unit=="K":
    weight*=2.205
else:
    weight/=2.205

print("Calculating results...")
time.sleep(2)
weight=round(weight,2)
print(f"The converted weight is {weight}")