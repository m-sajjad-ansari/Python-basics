import random
import time


def display(row):
    print("---------------")
    print(" | ".join(row))
    print("---------------")


def spin():
    symbols = ['🍒', '🍉', '🤑', '🥭']
    results = []
    for i in range(3):
        results.append(random.choice(symbols))
    # return results
    return [random.choice(symbols) for symbol in range(3)]


def prize(row, bet):
    if row[0] == row[1] == row[2]:
        return bet * 3
    else:
        return 0


def main():
    balance = 1000
    print("Welcome to slots game!")
    print("Symbols : 🍒 🍉 🤑 🥭")
    print("The higher you bet the more chances of your winning?!")
    while balance > 0:
        print(f"Your current balance is {balance}")
        while True:
            try:
                bet = int(input("Bet amount : "))
                if (bet > 0) & (bet <= balance):
                    balance -= bet
                    break
                else:
                    print("Invalid bet amount")
            except ValueError:
                print("Invalid input!")
        row = spin()
        print("Spinning the wheel...")
        time.sleep(0.5)
        display(row)
        won = prize(row, bet)
        if won > 0:
            print("Hurrah!")
            print(f"You won Rs {won}")
            balance+=won
            playAgain=input("Do you want to play again?(Y/N) : ").capitalize()
            if playAgain!="Y":
                print(f"Your balance is Rs {balance}")
                print("Hope this game made you happy!")
                quit()
    print("Better luck next time!")
    print("No balance left!")

if __name__ == "__main__":
    main()
