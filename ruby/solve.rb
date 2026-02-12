# frozen_string_literal: true

QUEEN = "\u2655"

def print_solution(board)
  n = board.size
  n.times do |row|
    n.times { print '+---' }
    puts '+'
    board.map { |cell| print "| #{cell == row ? QUEEN : ' '} " }
    puts '|'
  end
  n.times { print '+---' }
  puts '+'
end

def place_ok?(board, row, col)
  slash = row - col
  divide = row + col
  n = board.size
  n.times do |i|
    n.times do |j|
      next if i == col && j == row

      return false if board[i] == j && (i == col || j == row)
      return false if board[i] == j && (j - i == slash || j + i == divide)

    end
  end
  true
end

def solve(board, col)
  return board if col >= board.size

  board.size.times do |row|
    next unless place_ok?(board, row, col)

    board[col] = row
    solved = solve(board, col + 1)
    return solved unless solved.empty?

    board[col] = -1
  end
  []
end

print_solution(solve([-1, -1, -1, -1, -1, -1, -1, -1], 0))
