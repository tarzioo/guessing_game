# Put your code here
import random
rand_num = random.randint(1,100)

guesses = 1
user = raw_input("Hey, What's your name? ")
print "Hey %s, let's play a game! Try to guess what number I'm thinking of" % user
num = int(raw_input("Hint, it's between 1 and 100: "))

while num != rand_num:
    if num > rand_num:
        print "Too High, guess again"    
    else:
        print "Too Low, guess again"

    guesses += 1
    num = int(raw_input("Guess again a number between 1 and 100: "))
        
print "Great job, you guessed it in %d guesses" % guesses