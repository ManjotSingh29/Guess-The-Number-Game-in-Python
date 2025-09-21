#Guess the Number Game
import random

def start_Game():

    """    
    Checking if the player is ready to start the game.
    Using if,elif and else to check for yes or no.
    Using 2nd if statement for error handling.
    """
    
    print("Ready to play? y/n")
    player_Status = input(str()).strip().lower()
    global player_Ready
    player_Ready = bool()
    if player_Status == "y":
        print("Lets get started.")
        player_Ready = True
        player_Instructions()
        answer_Generation()
        while True:
            player_Input()
            if answer_checking():
                break 
    elif player_Status == "n":
        print("Ok... rude")
        player_Ready = False
    else:
         print("Invalid input. Please try answering in y/n.")
         pass   



def player_Instructions():
    """
    Giving instructions to player
    """
    print("I have generated a number between 0 and 100. \nYou have to guess what the number is and don`t worry, you dont have to guess in 1 go. \nThis isnt a SAW situation. I`ll give you hints if you can`t give the right answer on the first")



def answer_Generation():
    """
    Generating the answer to the game using the random function
    """
    global answer
    answer = random.randint[0,100]



def player_Input():
    """
    Taking player input and checking it against answer
    """
    print("Enter your guess.")
    global player_Answer
    try:
        player_Answer = int(input("Enter a number: "))
    except ValueError:
        print("Hey! That wasn`t a number.")
        player_Input()


    
def answer_checking():
    """
    Checking all posibilities for player answer and error handling.
    """
    while True:
        if player_Answer > 100:
            print("Too high. Answer is between 0 and 100 inclusive.")
            player_Input()
        if player_Answer < 0:
            print("Too low. Answer is between 0 and 100 inclusive.")
            player_Input()
            exit()
        if player_Answer > answer:
            print(f"The answer is a number smaller than {player_Answer}")
            player_Input()
        if player_Answer < answer:
            print(f"The answer is a number larger than {player_Answer}")
            player_Input()
        if player_Answer == answer:
            print("Congratulations, you won.")
            break

start_Game()

