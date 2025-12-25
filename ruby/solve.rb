QUEEN = "\u2655"

def print_solution(board)
  n = board.size
  n.times do |row|
    n.times { print "+---" }
    puts "+"
    board.map { |cell| print "| " + (cell == row ? QUEEN : " ") + " " }
    puts "|"
  end
  n.times { print "+---" }
  puts "+"
end

def is_place_ok(board, row, col)
  slash = row - col
  divide = row + col
  n = board.size
  n.times do |i|
    n.times do |j|
      if i == col && j == row
        next
      end
      if board[i] == j
        if i == col || j == row
          return false
        end
        if j - i == slash || j + i == divide
          return false
        end
      end
    end
  end
  true
end

def solve(board, col)
  if col >= board.size
    return board
  else
    board.size.times do |row|
      if is_place_ok(board, row, col)
        board[col] = row
        solved = solve(board, col + 1)
        if solved.size > 0
          return solved
        else
          board[col] = -1
        end
      end
    end
    []
  end
end

print_solution(solve([-1,-1,-1,-1,-1,-1,-1,-1], 0))
