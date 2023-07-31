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
    merged_row = [0] * len(row)
    merge_index = 0

    for num in row:
        if num != 0:
            if merged_row[merge_index] == 0:
                merged_row[merge_index] = num
            elif merged_row[merge_index] == num:
                merged_row[merge_index] *= 2
                merge_index += 1
            else:
                merge_index += 1
                merged_row[merge_index] = num
    
    return merged_row

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
    
    moves = [move_left, move_right, move_down, move_up]
    
    return not any(0 in row for row in board) and not any([move(board) for move in moves])

def display_board(board):
    clear_screen()
    print("\n2048 GAME\n")
    for row in board:
        print(" ".join(f"{num:4}" if num != 0 else "    " for num in row))

def can_move(board, move_func):
    # Create a copy of the current board to simulate the move
    new_board = [list(row) for row in board]
    
    # Perform the move on the copy
    new_board = move_func(new_board)
    
    # Check if the original board is different from the new_board
    return new_board != board

def read_high_score():
    try:
        with open("high_score.txt", "r") as file:
            high_score = int(file.read())
            return high_score
    except FileNotFoundError:
        # Return a default high score if the file doesn't exist yet
        return 0
    except ValueError:
        # Handle the case when the file contains invalid data
        # (e.g., not an integer)
        return 0

def write_high_score(high_score):
    with open("high_score.txt", "w") as file:
        file.write(str(high_score))

def check_high_score(board):
    total_score = 0;
    for row in board:
        total_score += sum(row)
    if (total_score > read_high_score()):
        write_high_score(total_score)
    return total_score
    
