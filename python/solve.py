QUEEN = "\u2655"


def print_solution(board):
    n = len(board)
    for row in range(n):
        for i in range(n):
            print("+---", end="")
        print("+")
        for col, p in enumerate(board):
            if p == row:
                print("| " + QUEEN, end=" ")
            else:
                print("|  ", end=" ")
        print("|")
    for i in range(n):
        print("+---", end="")
    print("+")


def is_place_ok(board, row, col):
    slash = row - col
    divide = row + col
    n = len(board)
    for i in range(n):
        for j in range(n):
            if i == col and j == row:
                continue
            if board[i] == j:
                if i == col or j == row:
                    return False
                if j - i == slash or j + i == divide:
                    return False
    return True


def solve(board, col):
    MAX_COL = len(board)
    MAX_ROW = len(board)
    if col >= MAX_COL:
        return board
    else:
        for row in range(MAX_ROW):
            if is_place_ok(board, row, col):
                board[col] = row
                solved = solve(board, col + 1)
                if solved:
                    return solved
                else:
                    board[col] = -1


solution = solve([-1] * 8, 0)
print_solution(solution)
