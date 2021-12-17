import random
import sys
try:
    import logging as lg
    lg.basicConfig(filename="logging.txt", filemode='a', format='%(asctime)s %(levelname)s -%(message)s', datefmt='%Y-%m-%d %H:%M:%S')
    lg.warning("User started playing the game.")
    turns = int(input("Enter the number of times you want to play the game for: "))
    win, loss, tie = 0, 0, 0
    for i in range(turns):
        number = random.randint(1,3)
        if number == 1: computer_move = 'r'
        elif number == 2: computer_move = 'p'
        else: computer_move = 's'
        while True:
            user_input = str(input("\nEnter your move: (r)ock (p)aper (s)cissors or (q)uit : ")).lower()
            if user_input == 'r' or user_input == 'p' or user_input == 's':
                break
            elif  user_input == 'q':
                print("Thank you for playing. See you soon!")
                sys.exit()
            else:
                print("Wrong Entry. Please try again.")
        print("The computer entered:",computer_move,"\nand you entered:",user_input)
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