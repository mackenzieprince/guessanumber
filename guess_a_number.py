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
    play = "playing"
   
    num_games_played = 0
    while play == "playing":
        if num_games_played == 0:
            answer = raw_input("Would you like to play Guess a Number? (Y/N) ")
            
            # ask a different question...raw_input()
        else:
            answer = raw_input("would you like to play again? (Y/N) ")
        level = raw_input("Would you like the play Beginner or Advanced? (B or A) ")
        if level.upper() == "B":
            number_allowed_guesses = 10
        else:
            number_allowed_guesses = 5
        if answer.lower() == "y" or answer.lower() == "yes":
            secret_number = random.randint(1,100)
            if num_games_played == 0: 
                directions(number_allowed_guesses)
                num_games_played = num_games_played +1
            print secret_number
            guess_a_num(secret_number, number_allowed_guesses)

        elif answer.lower() == "n" or answer.lower() == "no":
            print "Goodbye!"
            break
        else:
            print "Please enter Y or N"
            # play()


def guess_a_num(secret_number, number_allowed_guesses):
    guessed_number_list = []
    guessing = "not guessed"
    while guessing == "not guessed":

        guess = raw_input("Guess a number ")
        guess = int(guess)
        guessed_number_list.append(guess)
        if guess == secret_number:
            print "You got it! The number was",str(secret_number), "and it only took you",str(len(guessed_number_list)),"tries!"
            break
        # play()
        elif guess < secret_number:
            print "Guess higher..."
        elif guess > secret_number:
            print "Guess lower..."
        if len(guessed_number_list) > number_allowed_guesses:
            print "You failed! The number was",str(secret_number)
            guessing = "failed attempt"
        print "So far you've guessed ", str(guessed_number_list)  


# closeness = 100
# if abs(secret_number - guess) < closeness:
#     print "You're getting closer"
#     closeness = abs(secret_number - guess)


def display():
    print "******   *"
    print "*        *"


def directions(number_allowed_guesses):
    print "I'm thinking of a number between 1 and 100. Guess within",str(number_allowed_guesses),"tries and you win! "


display()
play()
