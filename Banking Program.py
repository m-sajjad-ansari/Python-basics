def balance(b):
    print(f"Your balance is {b}")


def deposit(b):
    while True:
        try:
            amount = int(input("Amount you want to deposit : "))
            if amount >= 0:
                print("Deposited successfully!")
                break
            else:
                print("Amount cannot be negative!")
        except ValueError:
            print("Invalid Input!")
    return amount


def withdraw(b):
    while True:
        try:
            amount = int(input("Amount you want to withdraw : "))
            if amount >= 0 and amount <= b:
                print("Withdrawn successfully!")
                break
            elif amount > b:
                print("Not enough amount in your bank account!")
                print("Withdrawn all amount present in your account!")
                amount = b
                break
            else:
                print("Amount cannot be negative!")
        except ValueError:
            print("Invalid Input!")
    return amount


def menu(name):
    print(f"{name}! Welcome to my banking program.")
    print("--------MENU--------")
    print("1.Check Balance")
    print("2.Deposit")
    print("3.Withdraw")
    print("4.Exit")
    print("--------------------")


def optionGetting():
    while True:
        try:
            option = int(input("Option number (1-4) : "))
            if option > 0 and option < 5:
                break
            else:
                print("Invalid option number!")
        except ValueError:
            print("Invalid input!")
    return option


def mainWorking(b):
    while True:
        option = optionGetting()
        if option == 1:
            balance(b)
        elif option == 2:
            b += deposit(b)
        elif option == 3:
            b -= withdraw(b)
        else:
            print("Thank you for using my program!")
            break
    return b

def main():
    b = 0
    name = input("Your name : ")
    menu(name)
    b = mainWorking(b)

if __name__ == "__main__":
    main()
