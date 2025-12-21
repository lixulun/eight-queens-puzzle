package main

import "fmt"

const N = 8
const QUEEN rune = 0x2655

type Board [N]int

func printSolution(board Board) {
	for r, _ := range board {
		for range N {
			fmt.Printf("+---")
		}
		fmt.Printf("+\n")
		for i := range N {
			if board[i] == r {
				fmt.Printf("| %c ", QUEEN)
			} else {
				fmt.Printf("|   ")
			}

		}
		fmt.Printf("|\n")
	}
	for range N {
		fmt.Printf("+---")
	}
	fmt.Printf("+\n")
}

func isPlaceOk(board Board, row int, col int) bool {
	slash := row - col
	divide := row + col
	for i := range N {
		for j := range N {
			if i == col && j == row {
				continue
			}
			if board[i] == j {
				if i == col || j == row {
					return false
				}
				if j-i == slash || j+i == divide {
					return false
				}
			}
		}
	}
	return true
}

func solve(board Board, col int) (Board, bool) {
	if col >= N {
		return board, true
	} else {
		for row := range board {
			if isPlaceOk(board, row, col) {
				board[col] = row
				solution, isSolved := solve(board, col+1)
				if isSolved {
					return solution, isSolved
				} else {
					board[col] = -1
				}
			}
		}
		return board, false
	}
}

func main() {
	solution, _ := solve(Board{-1, -1, -1, -1, -1, -1, -1, -1}, 0)
	printSolution(solution)
}
