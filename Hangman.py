import random
import time
fruits = (
    "apple", "banana", "mango", "orange", "grape", "watermelon",
    "strawberry", "blueberry", "pineapple", "pear", "cherry",
    "peach", "kiwi", "pomegranate", "papaya", "fig", "plum",
    "apricot", "blackberry", "raspberry", "coconut", "guava",
    "melon", "dragonfruit", "lychee", "passionfruit"
)

vegetables = (
    "carrot", "potato", "tomato", "onion", "broccoli", "cucumber",
    "spinach", "lettuce", "cauliflower", "cabbage", "bell pepper",
    "peas", "garlic", "ginger", "pumpkin", "radish", "zucchini",
    "eggplant", "beetroot", "chili", "celery", "asparagus",
    "corn", "mushroom", "sweetpotato"
)

words = fruits + vegetables

hangman_art = {
    0: ("     ",
        "     ",
        "     "),
    1: ("  o  ",
        "     ",
        "     "),
    2: ("  o  ",
        "  |  ",
        "     "),
    3: ("  o  ",
        " /|  ",
        "     "),
    4: ("  o  ",
        " /|\\",
        "     "),
    5: ("  o  ",
        " /|\\",
        " /   "),
    6: ("  o  ",
        " /|\\",
        " / \\"),
}


def display_hangman(wrong_guesses):
    print("--------------")
    for line in hangman_art[wrong_guesses]:
        print("\t", end="")
        print(line)
    print("--------------")


def display_answer(answer):
    print(" ".join(answer))


def display_hint(hint):
    print(" ".join(hint))


def main():
    print("Welcome to fruits and vegetables guessing game!")
    time.sleep(2)
    answer = random.choice(words)
    hint = ["_"] * len(answer)
    is_running = True
    wrong_guesses = 0
    guessed_letters = set()

    while is_running:
        display_hangman(wrong_guesses)
        display_hint(hint)
        guess = input("Guess an alphabet : ").lower()
        while True:
            if len(guess) != 1 or not guess.isalpha():
                guess = input("Enter a valid single alphabet : ")
            else:
                break

        if guess in guessed_letters:
            print("Already guessed!")
        else:
            if guess in answer:
                guessed_letters.add(guess)
                for i in range(len(answer)):
                    if answer[i] == guess:
                        hint[i] = guess
            else:
                print("Not found in answer!")
                wrong_guesses += 1

            if wrong_guesses == 6:
                display_hangman(wrong_guesses)
                print("Better luck next time!")
                is_running = False

            if not "_" in hint:
                display_answer(answer)
                print("You won")
                is_running = False


if __name__ == "__main__":
    main()
