try:
    import logging as lg
    lg.basicConfig(filename="logging.txt",
                   filemode='a',
                   format='%(asctime)s %(levelname)s -%(message)s',
                   datefmt='%Y-%m-%d %H:%M:%S')
    theBoard = {'top-L': ' ', 'top-M': ' ', 'top-R': ' ', 'mid-L': ' ', 'mid-M': ' ',
                'mid-R': ' ', 'low-L': ' ', 'low-M': ' ', 'low-R': ' '}
    def printBoard(board):
        print(board['top-L'] + '|' + board['top-M'] + '|' + board['top-R'])
        print('-+-+-')
        print(board['mid-L'] + '|' + board['mid-M'] + '|' + board['mid-R'])
        print('-+-+-')
        print(board['low-L'] + '|' + board['low-M'] + '|' + board['low-R'])
    turn = 'X'
    for i in range(9):
        printBoard(theBoard)
        print("""\nPlease enter one of the following to play when it's your turn:
                  top-L, top-M, top-R,
                  mid-L, mid-M, mid-R, 
                  low-L, low-M, low-R
            where L is left, M is middle and R is the right position.""")
        while True:
            print('\nTurn for ' + turn + '. Move on which space?')
            move = input("Make your choice - ")
            if theBoard[move] != " ":
                print("That space already been filled. Please try again.")
                move = input("Make your choice - ")
            if move not in theBoard: print("Wrong Input. Try Again.!\n")
            else: break
        theBoard[move] = turn
        if turn == 'X': turn = 'O'
        else: turn = 'X'
    printBoard(theBoard)
except (AttributeError, TypeError, ValueError, AssertionError, Exception, ArithmeticError) as e:
    print("Error is: \n", e)
    lg.error("Error found in the code. Pl rectify and try again.")