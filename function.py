import random

    
roll1 = random.randint(1,6)
guess = int(input("Guess a dice roll: \n"))
if guess == roll1:
    print("Correct! They rolled a " + str(roll1))
else:
    print("Wrong! They rolled a " + str(roll1))


def rollresult1(roll1):
    print("Your roll is ", roll1)

roll2 = random.randint(1,6)
guess = int(input("Guess a dice roll: \n"))
if guess == roll2:
    print("Correct! They rolled a " + str(roll2))
else:
    print("Wrong! They rolled a " + str(roll2))
