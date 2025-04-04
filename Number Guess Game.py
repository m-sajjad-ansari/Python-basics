import random
import time

n = random.randint(1, 100)
print("I have think a number between 1 and 100")
time.sleep(1)
print("You have five chances only")
for i in range(5):
    while True:
        try:
            guess = int(input("Guess the number : "))
            if guess >= 0 and guess <= 100:
                break
            else:
                print("Out of range!")
        except ValueError:
            print("Invalid input!")
    if guess>n:
        print("Guess is high")
    elif guess<n:
        print("Guess is low")
    else:
        print("Wait a minute let me check again...")
        time.sleep(2)
        print("You guessed it correctly")
        quit()
print("Chances finished")
print("You didn't guessed!")