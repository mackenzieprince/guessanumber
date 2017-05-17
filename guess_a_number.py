import random

# 1. Ask if they want to play the game : play()
#     a/ yes....guess()
#         pick a number
#     b. no....exit()



# 2. Ask them to guess a number : guess()
# guessed_number_list.append(guess)
# check()

# 3. Check the number : check(number, guessed_number_list)
#     a. if match print result play()
#     b. if not match give input guess()
#         if abs(number - guess) < abs(number - guess_before)...then, say getting warmer
#         guessed_numbr = guessed_number_list[-1]
#         guessed_before = guessed_number_list[-2]



def play():
    guessed_number_list = []
    num_games_played = 0
    while True:
        if num_games_played > 0:
            print "Hello! Would you like to play Guess a Number?"

            # ask a different question...raw_input()
        else:
            answer = raw_input("Would you like to play Guess a Number? (Y/N) ")

        if answer.lower() == "y" or answer.lower() == "yes":
            secret_number = random.randint(1,100)
            print secret_number
            directions()
            guess_a_num(secret_number,guessed_number_list)

        elif answer.lower() == "n" or answer.lower() == "no":
            print "Goodbye!"
            break
        else:
            print "Please enter Y or N"
            # play()


def guess_a_num(secret_number,guessed_number_list):
    guess = raw_input("I'm thinking of a number between 1 and 100. Care to take a guess? ")
    guess = int(guess)
    guessed_number_list.append(guess)
    if guess == secret_number:
        print "You got it! The number was (secret_number)"
        # play()
    elif guess <= secret_number:
        print "Higher..."
        guess_a_num(secret_number,guessed_number_list)
    elif guess >= secret_number:
        print "Lower..."
        guess_a_num(secret_number,guessed_number_list)
    print "It only took you _ tries! You guessed guessed_number_list"




def directions():
    print "Great! You will have 5 chances to guess the number."



play()
