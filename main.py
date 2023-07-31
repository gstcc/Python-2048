import random
import os

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def initialize_board():
    board = [[0 for _ in range(4)] for _ in range(4)]
    add_random_tile(board)
    add_random_tile(board)
    return board

def add_random_tile(board):
    empty_tiles = [(i, j) for i in range(4) for j in range(4) if board[i][j] == 0]
    if empty_tiles:
        i, j = random.choice(empty_tiles)
        board[i][j] = 2 if random.random() < 0.9 else 4

def transpose(board):
    return [list(row) for row in zip(*board)]

def reverse(board):
    return [row[::-1] for row in board]

def merge(row):
    #fix error when moving to left
    new_row = [num for num in row if num != 0]
    for i in range(len(new_row) - 1):
        if new_row[i] == new_row[i + 1]:
            new_row[i] *= 2
            new_row[i + 1] = 0
    new_row = new_row + [0] * (len(row) - len(new_row))
    return new_row

def move_left(board):
    return [merge(row) for row in board]

def move_right(board):
    return reverse(move_left(reverse(board)))

def move_up(board):
    return transpose(move_left(transpose(board)))

def move_down(board):
    return transpose(move_right(transpose(board)))

def is_game_over(board):
    for row in board:
        if 2048 in row:
            return True
    for row in transpose(board):
        if 2048 in row:
            return True
    return not any(0 in row for row in board)

def display_board(board):
    clear_screen()
    print("\n2048 GAME\n")
    for row in board:
        print(" ".join(f"{num:4}" if num != 0 else "    " for num in row))

def main():
    board = initialize_board()
    moves = {'w': move_up, 'a': move_left, 's': move_down, 'd': move_right}

    while not is_game_over(board):
        display_board(board)
        move = input("Enter move (W/A/S/D): ").lower()
        if move in moves:
            board = moves[move](board)
            add_random_tile(board)
    
    display_board(board)
    print("Game Over! You win!" if 2048 in [num for row in board for num in row] else "Game Over! You lose!")

if __name__ == "__main__":
    main()
