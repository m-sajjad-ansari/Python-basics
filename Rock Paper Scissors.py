import random
import time

print("Let's play rock paper scissors game!")
options = ("Rock", "Paper", "Scissors")
computer = random.randint(1, 3)
time.sleep(1.5)
while True:
    try:
        print("Select from the options (1-3) : ")
        time.sleep(1)
        print("Let's Play : ")
        for i in range(0, 3):
            time.sleep(1)
            print(options[i])
        time.sleep(2)
        player=int(input("Shoot : "))
        if player >= 1 and player <= 3:
            break
        else:
            print("Invalid option")
    except ValueError:
        print("Enter a valid integer!")

print("Calculating winner...")
time.sleep(2)
if player == computer:
    print("Match Drawn!")
elif (computer==1 and player==3) or (computer==2 and player==1) or (computer==3 and player==2):
    print("I won!")
else:
    print("You won!")