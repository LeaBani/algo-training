def sudoku(puzzle):
    
    def is_valid(num, row, col):

        for x in range(9):
            if puzzle[row][x] == num:
                return False

        for y in range(9):
            if puzzle[y][col] == num:
                return False

        start_row, start_col = 3 * (row // 3), 3 * (col // 3)
        for x in range(start_row, start_row + 3):
            for y in range(start_col, start_col + 3):
                if puzzle[x][y] == num:
                    return False
        return True

    def solve():
        for row in range(9):
            for col in range(9):
                if puzzle[row][col] == 0:
                    for num in range(1, 10):
                        if is_valid(num, row, col):
                            puzzle[row][col] = num
                            if solve():
                                return True
                            puzzle[row][col] = 0  
                    return False
        return True

    solve()
    return puzzle

# Test case
puzzle = [[5,3,0,0,7,0,0,0,0],
          [6,0,0,1,9,5,0,0,0],
          [0,9,8,0,0,0,0,6,0],
          [8,0,0,0,6,0,0,0,3],
          [4,0,0,8,0,3,0,0,1],
          [7,0,0,0,2,0,0,0,6],
          [0,6,0,0,0,0,2,8,0],
          [0,0,0,4,1,9,0,0,5],
          [0,0,0,0,8,0,0,7,9]]

print(sudoku(puzzle))
