# Put your code here
import random
rand_num = random.randint(1,2)

user = raw_input("Hey, What's your name? ")
play = 'Y'
while play.upper() == 'Y':
    guesses = 1
    print "Hey %s, let's play a game! Try to guess what number I'm thinking of" % user
    num = int(raw_input("Hint, it's between 1 and 100: "))
    try:
        while num != rand_num:
            if num > rand_num and num < 101:
                print "Too High, guess again"    
            elif num < rand_num and num > 0:
                print "Too Low, guess again"
            else:
                print "Silly goose, read the directions and guess between 1 and 100"
            

            guesses += 1
            num = int(raw_input("Guess again a number between 1 and 100: "))
                
        print "Great job, you guessed it in %d guesses" % guesses
    except ValueError:
        print "Silly goose, I asked for a number, guess a number between 1 and 100"
    play = raw_input("Would you like to play again (Y/N): ")

print "Thanks for playing!"    