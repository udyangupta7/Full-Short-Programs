# importing important libraries
import random # used for generating random numbers
import sys # library for system-specific parameters and functions
try:
    # creating a logging file
    import logging as lg
    lg.basicConfig(filename="logging.txt", filemode='a', format='%(asctime)s %(levelname)s -%(message)s', datefmt='%Y-%m-%d %H:%M:%S')
    lg.warning("User started playing the game.") # creates a log everytime the user will run the code.
    # general information to the user:
    print("LET'S PLAY ROCK PAPER SCISSORS. FOLLOWING ARE THE INSTRUCTIONS FOR YOUR INPUT AGAINST THE SYSTEM.\n\t1. 'r' - When you want to use rock as your move.\n\t1. 'p' - When you want to use paper as your move.\n\t1. 's' - When you want to use scissor as your move.\n")
    # user will decide the number of times he will play the game for:
    turns = int(input("Enter the number of times you want to play the game for: "))
    # creating three variables to count total wins, losses and ties:
    win, loss, tie = 0, 0, 0
    for i in range(turns):
        # the randomly generated move by the system:
        number = random.randint(1,3)
        if number == 1: computer_move = 'r'      # r stands for 'rock'.
        elif number == 2: computer_move = 'p'    # 'p' stands for 'paper'.
        else: computer_move = 's'                # 's' stands for 'scissor'.
        while True:
            # user input when it's his chance to play the game.
            user_input = str(input("\nEnter your move: (r)ock (p)aper (s)cissors or (q)uit : ")).lower()
            # executes when user will enter one of the three possible moves for the game:
            if user_input == 'r' or user_input == 'p' or user_input == 's':
                break
            # executes when user decides to quit the game:
            elif  user_input == 'q':
                print("Thank you for playing. See you soon!")
                sys.exit()
            # executes when user input is not one of the three moves possible in the game:
            else:
                print("Wrong Entry. Please try again.")
        print("You entered:",user_input ,"and the computer entered:",computer_move,)
        if computer_move == user_input:
            print("its a Tie")
            tie+=1
        elif computer_move != user_input:
            # All the conditions when the user will win:
            if user_input == 's' and computer_move == 'p':
                print("You Win!")
                win+=1
            elif user_input == 'r' and computer_move == 's':
                print("You Win!")
                win+=1
            elif user_input == 'p' and computer_move == 'r':
                print("You Win!")
                win+=1
            # All the conditions when the user will loose:
            elif user_input == 'p' and computer_move == 's':
                print("You Loose!")
                loss+=1
            elif user_input == 's' and computer_move == 'r':
                print("You Loose!")
                loss+=1
            elif user_input == 'r' and computer_move == 'p':
                print("You Loose!")
                loss+=1
    print("\nFINAL RESULT:", win, "wins", tie,"ties and", loss, "losses" )
except (AttributeError, TypeError, ValueError, AssertionError, Exception, ArithmeticError) as e:
    print("Error is: \n", e)
    lg.error("Error found in the code. Pl rectify and try again.")