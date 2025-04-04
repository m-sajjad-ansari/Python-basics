import time

while True:
    try:
        n = int(input("Enter rows (1-9) : "))
        if n > 0 and n < 10:
            break
        else:
            print("Rows out of range!")
    except ValueError:
        print("Invalid input!")

#     1
#    2 2
#   3   3
#  4     4
# 5       5
#  4     4
#   3   3
#    2 2
#     1

for rows in range(1,n+1):
    for i in range(n,0,-1):
        if i == rows:
            print(i,end="")
        else:
            print(" ",end="")
    for i in range(2,n+1):
        if i==rows:
            print(i,end="")
        else:
            print(" ",end="")
    print()

for rows in range(n-1,0,-1):
    for i in range(n, 0, -1):
        if i == rows:
            print(i, end="")
        else:
            print(" ", end="")
    for i in range(2, n + 1):
        if i == rows:
            print(i, end="")
        else:
            print(" ", end="")
    print()