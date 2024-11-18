import os, time

def displayword(word, guesses):
    for letter in word:
        if letter in guesses:
            print(letter, end=" ")
        else:
            print("_", end=" ")
    print("\n")

def display_wrong_guess(wrong_guesses):
    wrong_guesses = " ".join(wrong_guesses)
    print(wrong_guesses+"\n")

def clean(word):
    while 1:                                 # cleaning the word
        if word[:1] == " ":
            word = word[1:]
        elif word[-1] == " ":
            word = word[:-1]
        else:
            break
    return word

# --------------------------------------------------

def displayhangman(wrong_count):
    hangman = [(" _____",
            "|    ",
            "| ",
            "| "),

            (" _____",
            "|  O  ",
            "| ",
            "| "),

            (" _____",
            "|  O  ",
            "|  |",
            "| "),

            (" _____",
            "|  O  ",
            "|  |",
            "| / "),

            (" _____",
            "|  O  ",
            "|  |",
            "| / \\"),

                (" _____",
                "|  O  ",
                "| /|",
                "| / \\"),

                (" _____",
            "|  O  ",
            "| /|\\",
            "| / \\")
            ]
    
    for line in hangman[wrong_count]:
        print(line)

# ---------------------------------------------

word = input("Enter the word: ")
word = clean(word)

guesses = [" "]                    # aa extra " " for printing space in displayword()
wrong_guesses = []
wrong_count = 0

is_running = 1
while(is_running):
    os.system('cls')
    displayhangman(wrong_count)                          # displaying the hangman

    print("Your wrong guesses:", end=" ")
    display_wrong_guess(wrong_guesses)

    displayword(word, guesses)                      # displaying _ and letters

    guess = input("Enter your guess: ").lower()
    if guess == " ":
        print("Enter something bruh")
        time.sleep(1.2)         
        continue
    guess = clean(guess)
    if guess == "exit":
        print("Bruh you gave up (。_。)")                            # handling input
        is_running = 0
        break
    elif len(guess) != 1:                                # word guessing
        if guess == word:
            print("Dayuuuummm YOU WON!!!")
            is_running = 0
            break
        else:
            print("Arinjudengi enthina verthe ( ´_ゝ` )")
            wrong_count += 1
    elif guess in word:                                   # checking if guessed
        if guess in guesses:
            print("!!You already guessed it!!")
        else:
            guesses.append(guess)
            print("Nice :)")
    else:
        if guess not in wrong_guesses:
            wrong_guesses.append(guess)
        wrong_count += 1
        print("You Guessed Wrong :(")


    if len(set(word)) - 1 == len(guesses):                   # checking exit condition ( -1 for " " in word )
        print("You WON!!!")
        is_running = 0
        break
    if wrong_count == 7:
        print("You LOST :( ")
        print(f"The correct answer was {"".join(word)}")
        is_running = 0
        break

    time.sleep(0.75)            # waiting