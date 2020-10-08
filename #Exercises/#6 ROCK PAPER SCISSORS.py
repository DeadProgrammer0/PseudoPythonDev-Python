
# Rock, Paper and Scissors Game.

import random

player_score = 0
computer_score = 0

no_of_rounds = 1



print("=================================================================="+
    "\n\t  This is a Rock, Paper, Scissors Game."+
    "\n=================================================================="+
    "\n\nYou'll play against the Computer and the Winner will be decided after 10 rounds."+
    "\n\nEnter r for rock.\nEnter p for paper.\nEnter s for scissors.")


while no_of_rounds <= 10:
    print("----------------------------------------"+
    f"\nRound {no_of_rounds}"+
    "\n----------------------------------------")
    player = input("Enter your move here : ")

    op = ("r","p","s")

    def convert(n):
        if n == "r":
            return "Rock"
        elif n == "p":
            return "Paper"
        elif n == "s":
            return "Scissors"

    comp = random.choice(op)
    print(f"Your move : {convert(player)} | Computer's move : {convert(comp)}")

    if player == comp:
        print("Round Draw!")

    elif player == "s" and comp == "p":
        print("Player wins!")
        player_score += 1
        
    elif player == "s" and comp == "r":
        print("Computer wins!")
        computer_score += 1
    
    elif player == "p" and comp == "r":
        print("Player wins!")
        player_score += 1
    
    elif player == "p" and comp == "s":
        print("Computer wins!")
        computer_score += 1
        
    if player == "r" and comp == "s":
        print("Player wins!")
        player_score += 1

    elif player == "r" and comp == "p":
        print("Computer wins!")
        computer_score += 1



    no_of_rounds += 1


def dec(func):
    def ini(*args,**kwargs):
        print("\n+++++++++++++++++++++++++++++++++++++++++++")
        func(*args,**kwargs)
        print("+++++++++++++++++++++++++++++++++++++++++++")
    return ini 

@dec
def counter(pscore,cscore):
    print(f"Player Score : {player_score} | Computer Score : {computer_score}")
    if pscore > cscore:
        print("Player Won!")
    elif cscore > pscore:
        print("Computer Won!")
    elif pscore == cscore:
        print("Match Drew!")

    
    

counter(player_score,computer_score)

