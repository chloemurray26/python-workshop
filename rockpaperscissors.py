
playerone = input("Player One: Rock, paper, or scissors?")

playertwo = input("Player Two: Rock, paper, or scissors?")

if playerone == "paper"  and playertwo == "rock":
    print("Player one wins.")
elif playerone == "rock" and playertwo == "scissors":
    print("Player one wins.")
elif playerone == "scissors" and playertwo == "rock":
    print("Player two wins.")
elif playerone == playertwo:
    print("There is a tie.")