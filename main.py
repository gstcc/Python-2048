import pygame
import sys
from pygame.locals import *
from game_logic import *
from board_render import draw_board

# Constants
WINDOW_WIDTH = 400
WINDOW_HEIGHT = 450
TILE_SIZE = WINDOW_WIDTH // 4
FPS = 60

# Initialize Pygame
pygame.init()
pygame.display.set_caption('2048 Game')
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
clock = pygame.time.Clock()
font = pygame.font.Font(None, 36)

def main():
    board = initialize_board()

    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

            # Handle key presses for tile movement
            if event.type == KEYDOWN:
                if event.key == K_LEFT:
                    if can_move(board, move_left):
                        board = move_left(board)
                        add_random_tile(board)
                elif event.key == K_RIGHT:
                    if can_move(board, move_right):
                        board = move_right(board)
                        add_random_tile(board)
                elif event.key == K_UP:
                    if can_move(board, move_up):
                        board = move_up(board)
                        add_random_tile(board)
                elif event.key == K_DOWN:
                    if can_move(board, move_down):
                        board = move_down(board)
                        add_random_tile(board)

        draw_board(screen, board, TILE_SIZE, font)

        if is_game_over(board):
            print("Game Over!")  # Or show a game over screen
            check_high_score(board)
            pygame.quit()
            sys.exit()

        pygame.display.update()
        clock.tick(FPS)

if __name__ == "__main__":
    main()
