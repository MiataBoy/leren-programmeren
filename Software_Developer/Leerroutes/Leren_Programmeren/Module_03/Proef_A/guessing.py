import random

anotherRound = ""
score = 0
rounds = 1
# Functie is;
# Controleren of het getal geraden is
# -- Check only the input
def guesser(question: str) -> bool:
    print("number ", number)  # uncomment this for debugging
    global guess # dont use global
    while not (guess := input(question)).isdigit():
        if guess == "stop":
            print("Exiting game with a score of {}, we're sad to see you go.".format(score))
            exit() # dont exit in functions
        print("--- You need to provide us with a number between 1 and 1000 or \"stop\" to stop ---")
    #print(guess)

    if int(guess) == number:
        return True

    else:
        return False

for x in range(20):
    if x != 0: # put at the bottom
        while not (anotherRound == "y" or anotherRound == "n"):
            anotherRound = input("Do you want to play another round? Y/N").lower()

        if anotherRound == "n":
            print("Got it, aborting game.")
            break
        if anotherRound == "y":
            print("You are currently on round {} with score {}.".format(rounds, score))
            pass
    number = random.randint(1, 1000)  # The number that has to be guessed

    if guesser("Guess a number between 1 to 1000") == True:
        score += 1
        rounds += 1
        if x != 20:
            print("You guessed correctly! Moving onto round {} with score {}".format(rounds, score))

    else:
        guesses = 10
        for x in range(10):
            if x == 10:
                print("You have failed to guess correctly, moving onto round {} with score {}".format(rounds, score))
                break
            #if number - guess > 50:
                #print("Guess higher")

            if guesser("Please guess again. You have {} guesses left.".format(guesses)) == True:
                score += 1
                rounds += 1
                print("You guessed correctly! Moving onto round {} with score {}".format(rounds, score))
                break

            else:
                sum = number - int(guess)
                if sum < 0:
                    sum = sum * -1

                if number > int(guess) and number - int(guess) > 50:
                    print("Guess higher.")
                elif int(guess) > number and int(guess) - number > 50:
                    print("Guess lower.")
                elif number > int(guess) and number - int(guess) < 50 and number - int(guess) > 20:
                    print("Getting warm, guess higher..")
                elif int(guess) > number and int(guess) - number < 50 and int(guess) - number >  20:
                    print("Getting warm, guess lower..")
                elif number > int(guess) and number - int(guess) < 20:
                    print("Getting very warm, guess higher.")
                elif int(guess) > number and int(guess) - number < 20:
                    print("Getting very warm, guess lower.")

                guesses -= 1
        rounds += 1

print("Congratulations! You have finished the game with a score of {}".format(score))