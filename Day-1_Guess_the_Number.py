#Guessing the number
def guess_the_number(num,n):
    if n>num: return 1
    elif n<num: return -1
    else: return 0
import random
num=random.randint(1,100) #taking a random number for user to guess
num_guessed= int(input("Guess the number between 1 to 100: "))

tries = 0 #counts the number of times the user plays to guess correctly
while True:
    status = guess_the_number(num, num_guessed)
    if status>0:
        num_guessed=int(input("The number is lesser than your guess, try again: "))
        tries+=1
    elif status<0:
        num_guessed=int(input("The number is greater than your guess, try again: "))
        tries+=1
    else:
        print(f"Success, the correct number is {num_guessed} in {tries} tries")
        break
