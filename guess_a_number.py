import random

def play():
    num_games_played = 0
    while True:
        guessed_number_list = []

        if num_games_played > 0:
            answer = raw_input("That was fun! Would you like to play Guess a Number again? (Y/N) ")
            # ask a different question...raw_input()
        else:
            answer = raw_input("Hello! Would you like to play Guess a Number? (Y/N) ")

        if answer.lower() == "y" or answer.lower() == "yes":
            
           
            upper_limit = directions_and_level()
            secret_number = random.randint(1,upper_limit)
            print secret_number
            num_games_played += 1
            guess_a_num(secret_number,guessed_number_list, upper_limit)

        elif answer.lower() == "n" or answer.lower() == "no":
            print "Goodbye!"
            break
        else:
            print "Please enter Y or N"
            # play()

def guess_a_num(secret_number,guessed_number_list, upper_limit):

    #if the upper_limit is 100, then the max length of guessed_number_list is 5.....
    
    max_length = 51
    while True:
        guess = raw_input("Please guess a number.  ")
        guess = int(guess)
        guessed_number_list.append(guess)
        if len(guessed_number_list) == 1:
            time = "time."
        else:
            time = "times."
        if guess == secret_number:

            print "You got it! The number was", secret_number, "and you guessed in", str(len(guessed_number_list)), time
            break
        elif len(guessed_number_list) == max_length:
            print "LOSER"
            break
        # play()
        elif guess <= secret_number:
            print "You guessed too low, please guess higher. You've guessed",str(len(guessed_number_list)),time
            
        elif guess >= secret_number:
            print "You guessed too high. Please guess lower. You've guessed",str(len(guessed_number_list)),time
   
        if upper_limit == 100 and len(guessed_number_list) == 5:
            print "Oh no! You didn't guess the number in 5 times. The number I was thinking of was "+ str(secret_number) + "."
            break



def directions_and_level():  
    print "Guess a number is a game where......."   
    level = raw_input("Would you like to play (B)eginner or (A)dvanced? ")   

    if level.upper() == "A":
        upper_limit = 100
        print "I'm thinking of a number between 1 and 100. You will have 5 chances to guess the number! "
        
    else:
        upper_limit = 50
        print "I'm thinking of a number between 1 and 50. You have an unlimited number of guesses!"
    return upper_limit

       



play()
