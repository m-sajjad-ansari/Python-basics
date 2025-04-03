import time
while True:
    try:
        a=int(input("First number : "))
        break
    except ValueError:
        print("Enter a number!")

while True:
        operation=input("Operation (+,-,/,*) : ")
        if operation=="+" or operation=="-" or operation=="*" or operation=="/":
            break
        else:
            print("Invalid operation...")

while True:
    try:
        b=int(input("Number : "))
        break
    except ValueError:
        print("Enter a number!")

if operation=="+":
    result=a+b
elif operation=="-":
    result=a-b
elif operation=="/":
    result=a/b
else:
    result=a*b

print("Calculating result...")
time.sleep(2)
print(f"Result is {result}")