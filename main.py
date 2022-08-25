import os
import time
import sys
from ai import AI
from game import Game

os.system("cls") #for cleaning the console

moves = ['Rock', 'Paper', 'Scissors']

ai = AI()
game = Game()


def make_move():

    selected_move = input("What is your move (Rock, Paper, Scissors): ").title()
    if selected_move not in moves:
        print("Invalid Input")
        time.sleep(.3)
        return make_move()
    return selected_move

def gameloop():

    player_move = make_move()
    print(f"You: {player_move}")
    ai_move = ai.make_move(moves)
    print(f"AI: {ai_move}")

    winner = game.select_winner(player_move=player_move, ai_move=ai_move)

    if winner == 1:
        should_play = input("You won, would you like to play again (yes or no): ")
    elif winner == -1:
        should_play = input("You lost, would you like to play again (yes or no): ")
    else:
        should_play = input("Tie, would you like to play again (yes or no): ")
    
    if should_play != 'yes':
        print("Goodbye ✌️")
        time.sleep(.3)
        sys.exit() #closes the program
    gameloop()

gameloop()


    