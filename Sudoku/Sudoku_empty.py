# OPTIONAL HELPER FUNCTIONS:

def find_next_empty(puzzle):
    # finds the next row or column on the puzzle that's not filled yet and is represented these with -1
    # returns a row or a column tuple (or None, None when there is a None value)
    pass

def is_valid(puzzle, guess, row, col):
    # figures out whether the guess at the row/column of the puzzle is a valid guess
    # returns a True or False based on the guess
    pass

# SOLVER IMPLEMENTATION:

def solve_sudoku(puzzle):
    # solving sudoku using backtracking
    # our puzzle is a list of lists, where each inner list is a row in
    # our sudoku puzzle and it returns a solution

    # STEPS:
    # step 1: choose a place on the puzzle-board to start making a guess
    # step 1.1: if there's no place left, then we're done because we are only allowed to enter valid inputs
    # step 2: if there is a place to put a number, then make a guess between 1 and 9
    # step 3: checking if this is a valid guess        # step 3.1: if this is a valid guess, then place it at that spot on the puzzle
    # step 4: then we recursively call our solver!
    # step 5: if not valid or if nothing gets returned true, then we need to backtrack and try a new number
    # step 6: if none of the numbers that we try work, then this puzzle is UNSOLVABLE!!
