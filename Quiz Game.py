import time
questions=("1. What is the capital of Pakistan?","2. When did Pakistan become independent?","3. Provinces in Pakistan?")
options=(("1. Lahore","2. Islamabad","3. Karachi"),
         ("1. 1943","2. 1947","3. 1950"),
         ("1. 5","2. 3","3. 1"))
score=0
answers=(2,2,1)
name=input("Your name : ")
time.sleep(0.3)
print(f"{name}! Welcome to a quiz game.")
for i in range(len(questions)):
    time.sleep(1)
    print()
    print(questions[i])
    time.sleep(1)
    for option in options[i]:
        time.sleep(0.7)
        print(option)
    while True:
        try:
            time.sleep(1.5)
            guess=int(input("Enter the option number (1-4) : "))
            if guess>=1 and guess<=4:
                break
            else:
                print("Invalid option number!")
        except ValueError:
            print("Enter a valid number")
    if guess==answers[i]:
        score+=1

print("Calculating Total Score...")
time.sleep(2)
print(f"Your total score is {score} out of 3")