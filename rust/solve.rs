const N: usize = 8;

type Board = [i8; N];

fn print_solution(board: Board) {
    for m in 0..N {
        for _ in 0..N {
            print!("+---");
        }
        println!("+");
        for i in 0..N {
            if board[i] == m as i8 {
                print!("| \u{2655} ")
            } else {
                print!("|   ");
            }
        }
        println!("|");
    }
    for _ in 0..N {
        print!("+---");
    }
    println!("+");
}

fn is_place_ok(board: &Board, row: i8, col: i8) -> bool {
    let slash = row - col;
    let divide = row + col;
    for i in 0..N {
        for j in 0..N {
            if i as i8 == col && j as i8 == row {
                continue;
            }
            if board[i] == j as i8 {
                if i as i8 == col || j as i8 == row {
                    return false;
                }
                if j as i8 - i as i8 == slash || j as i8 + i as i8 == divide {
                    return false;
                }
            }
        }
    }
    return true;
}

fn solve(board: &mut Board, col: i8) -> bool {
    if col >= N as i8 {
        return true;
    } else {
        let mut row = 0;
        while row < N {
            if is_place_ok(&board, row as i8, col as i8) {
                board[col as usize] = row as i8;
                let is_solved = solve(board, col + 1);
                if is_solved {
                    return is_solved;
                } else {
                    board[col as usize] = -1;
                }
            }
            row += 1;
        }
        return false;
    }
}

fn main() {
    let mut solution = [-1, -1, -1, -1, -1, -1, -1, -1];
    let _ = solve(&mut solution, 0);
    print_solution(solution);
}
