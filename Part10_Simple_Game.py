###########################
## PART 10: Simple Game ###
### --- CODEBREAKER --- ###
## --Nope--Close--Match--  ##
###########################

# It's time to actually make a simple command line game so put together everything
# you've learned so far about Python. The game goes like this:

# 1. The computer will think of 3 digit number that has no repeating digits.
# 2. You will then guess a 3 digit number
# 3. The computer will then give back clues, the possible clues are:
#
#     Close: You've guessed a correct number but in the wrong position
#     Match: You've guessed a correct number in the correct position
#     Nope: You haven't guess any of the numbers correctly
#
# 4. Based on these clues you will guess again until you break the code with a
#    perfect match!

# There are a few things you will have to discover for yourself for this game!
# Here are some useful hints:

# Try to figure out what this code is doing and how it might be useful to you
import random
digits = list(range(10))
random.shuffle(digits)
code=digits[:3]
print(code)

# Another hint:
# guess = int(input("What is your guess? "))

def close(n):
    if n%10 in code[:2] or ((n-(n%10))%100)/10 in code[::1] or (n-((n%10)+(n-(n%10))%100))/100 in code[1:]:
        return True

def match(n):
    if n%10==code[2] or ((n-(n%10))%100)/10 == code[1] or (n-((n%10)+(n-(n%10))%100))/100 == code[0]:
        return True

def nope(n):
    if n%10 not in code and ((n-(n%10))%100)/10 not in code and (n-((n%10)+(n-(n%10))%100))/100 not in code:
        return True

def perfect(n):
    if n%10 == code[2] and ((n-(n%10))%100)/10 == code[1] and (n-((n%10)+(n-(n%10))%100))/100 == code[0]:
        return True
    else:
        return False


def game():
    i='n'
    while i=='n':
        guess = int(input("What is your guess? "))
        if perfect(guess):
            print("Bingo You've found a match")
            return True
        elif close(guess):
            print("Close guess")
        elif match(guess):
            print("Match found")
        elif nope(guess):
            print("Oops no correct value")

        i=input("do you want to quit (y/n)")
    return False


game()






# Think about how you will compare the input to the random number, what format
# should they be in? Maybe some sort of sequence? Watch the Lecture video for more hints!
