def play():
    guessed_number_list = []
    num_games_played = 0
    while True:
        if num_games_played > 0:
            print "H? (Y/N) ?"
            # ask a different question...raw_input()
        else:
            answer = raw_input("Hello! Would you like to play Guess a Number? (Y/N) ")

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
    guess = raw_input("Please guess a number.  ")
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
    print "Would you like to play Beginner level (B) or Advanced level (A)? n/Beginnger Level: I'm thinking of a number between 1 and 50. You have an unlimited number of guesses! /n Advanced level: I'm thinking of a number between 1 and 100. You will have 5 chances to guess the number. "
        if raw_input("B"):
            upper_range = 50
            number_of_guesses_allowed = None
            play(upper_range,number_of_guesses_allowed)
    elif raw_input("A"):
            upper_range = 100
            number_of_guesses_allowed = 5
            play(upper_range,number_of_guesses_allowed)

        



directions()
