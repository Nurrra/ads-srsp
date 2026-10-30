def is_safe(board, row, col):
    for r in range(row):
        c = board[r]
        if c == col or abs(c - col) == abs(r - row):
            return False
    return True

def solve_queens(board, row, n, solutions):
    if row == n:
        solutions.append(board[:])
        return
    for col in range(n):
        if is_safe(board, row, col):
            board[row] = col
            solve_queens(board, row + 1, n, solutions)
            board[row] = -1
n = 4
solutions = []
solve_queens([-1] * n, 0, n, solutions)

for number, sol in enumerate(solutions, 1):
    print(f"Решение {number}:")
    for row in range(n):
        print(" ".join("Q" if sol[row] == col else "." for col in range(n)))
    print()
