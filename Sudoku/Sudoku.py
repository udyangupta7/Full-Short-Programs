from pprint import pprint
def find_next_empty(puzzle):
    # this function finds the next row and col on the puzzle
    # the spaces that aren't filled yet are represented with -1
    # return row, col tuple (or (None, None) if there is none)
    # we are using 0-8 for our indices
    for r in range(9):
        for c in range(9): # range(9) is 0, 1, 2, ... 8
            if puzzle[r][c] == -1:
                return r, c

    return None, None  # when no spaces in the puzzle are empty (aka equal to -1)

def is_valid(puzzle, guess, row, col):
    # this function figures out whether the guess at the row/col of the puzzle is a valid guess or not
    # it returns either a True or a False

    # starting with the row first
    row_vals = puzzle[row]
    if guess in row_vals:
        return False # if we've repeated, then our guess is not valid!

    # now looking at the columns:
    # col_vals = [] is an empty list
    # for i in range(9):
    #     col_vals.append(puzzle[i][col])
    # col_vals uses list comprehension to perform the above lines of code in one line
    col_vals = [puzzle[i][col] for i in range(9)]
    if guess in col_vals:
        return False

    # and then checking the entire square
    row_start = (row // 3) * 3
    col_start = (col // 3) * 3

    for r in range(row_start, row_start + 3):
        for c in range(col_start, col_start + 3):
            if puzzle[r][c] == guess:
                return False

    return True

def solve_sudoku(puzzle):
    # solving the sudoku using backtracking
    # our puzzle is a list of lists, where each inner list is a row in
    # our sudoku puzzle return whether a solution exists or not
    # mutates puzzle to be the solution if the solution exists
    
    # step 1: choose a place on the puzzle-board to start making a guess
    row, col = find_next_empty(puzzle)

    # step 1.1: if there's no place left, then we're done because we are only allowed to enter valid inputs
    if row is None:  # this condition is true if our find_next_empty function returns None, None for the condition
        return True 
    
    # step 2: if there is a place to put a number, then make a guess between 1 and 9
    for guess in range(1, 10): # range(1, 10) is 1, 2, 3 upto 9
        # step 3: checking if this is a valid guess
        if is_valid(puzzle, guess, row, col):
            # step 3.1: if this is a valid guess, then place it at that spot on the puzzle
            puzzle[row][col] = guess
            # step 4: then we recursively call our solver!
            if solve_sudoku(puzzle):
                return True
        
        # step 5: if not valid or if nothing gets returned true, then we need to backtrack and try a new number
        puzzle[row][col] = -1

    # step 6: if none of the numbers that we try work, then this puzzle is UNSOLVABLE!!
    return False

if __name__ == '__main__':
    # sample board
    example_board = [
        [3, 9, -1,   -1, 5, -1,   -1, -1, -1],
        [-1, -1, -1,   2, -1, -1,   -1, -1, 5],
        [-1, -1, -1,   7, 1, 9,   -1, 8, -1],

        [-1, 5, -1,   -1, 6, 8,   -1, -1, -1],
        [2, -1, 6,   -1, -1, 3,   -1, -1, -1],
        [-1, -1, -1,   -1, -1, -1,   -1, -1, 4],

        [5, -1, -1,   -1, -1, -1,   -1, -1, -1],
        [6, 7, -1,   1, -1, 5,   -1, 4, -1],
        [1, -1, 9,   -1, -1, -1,   2, -1, -1]
    ]
    print(solve_sudoku(example_board))
    pprint(example_board)
