#The brute force solution that came to mind is to have a dictionary with the key as either row_[x] or col_y[] and have a set as the value of all the numbers 
from collections import defaultdict
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        #First initialze the dictionary that will be used for cross-checking the sudoku board
        sudoku_dict = defaultdict(set)
        #next, we go through the sudoku board, adding every point to both its corresponding row and column key

        for i in range(len(board)):
            row_key = "row_" + str(i)
            for j in range(len(board[0])):
                #Add the sudoku point
                board_point = board[i][j]
                col_key = "col_" + str(j)
                row_square = i // 3
                col_square = j // 3
                square_key = "square_"+ str(row_square) + "" + str(col_square)
                if board_point in sudoku_dict[row_key] or board_point in sudoku_dict[col_key] or board_point in sudoku_dict[square_key]:
                    return False
                if board_point != '.':
                    sudoku_dict[row_key].add(board_point)
                    sudoku_dict[col_key].add(board_point)
                    sudoku_dict[square_key].add(board_point)
        return True    
