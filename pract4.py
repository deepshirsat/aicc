def is_safe(board, row, col, n):
    # Check column
    for i in range(row):
        if board[i] == col:
            return False
    # Check diagonal
    for i in range(row):
        if abs(board[i] - col) == abs(i - row):
            return False
    return True
def solve_nqueens_bt(board, row, n):
    if row == n:
        print(board)
        return True
    for col in range(n):
        if is_safe(board, row, col, n):
            board[row] = col
            solve_nqueens_bt(board, row + 1, n)
    return False
# Run
n = 4
board = [-1] * n
solve_nqueens_bt(board, 0, n)

# Output
#PS C:\Users\user> & C:/Users/user/anaconda3/python.exe e:/AI/P4.py
#[2, 0, 3, 1]
