import pygame

# Define colors (RGB format)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (128, 128, 128)
SCORE_BAR_COLOR = (120, 140, 200)
TILE_COLORS = {
    0: GRAY,
    2: (238, 228, 218),
    4: (237, 224, 200),
    8: (242, 177, 121),
    16: (245, 149, 99),
    32: (246, 124, 95),
    64: (246, 94, 59),
    128: (237, 207, 114),
    256: (237, 204, 97),
    512: (237, 200, 80),
    1024: (237, 197, 63),
    2048: (237, 194, 46)
}

# Function to draw the game board and tiles
def draw_board(screen, board, tile_size, font):
    screen.fill(BLACK)  # Clear the screen

    score_bar_rect = pygame.Rect(0, 400, screen.get_width(), 50)
    pygame.draw.rect(screen, SCORE_BAR_COLOR, score_bar_rect)

    score_text = font.render(f"Score: {0}  Highest: {100}", True, BLACK)
    score_text_rect = score_text.get_rect(center=(screen.get_width() // 2, tile_size * 4 + 25))
    screen.blit(score_text, score_text_rect)

    # Draw the tiles on the board
    for y in range(4):
        for x in range(4):
            tile_value = board[y][x]
            tile_color = TILE_COLORS.get(tile_value, WHITE)
            pygame.draw.rect(screen, tile_color, (x * tile_size, y * tile_size, tile_size, tile_size))
            if tile_value != 0:
                draw_text(screen, str(tile_value), (x * tile_size + tile_size // 2, y * tile_size + tile_size // 2), font, BLACK)

    

    pygame.display.flip()  # Update the screen

# Function to draw text on the screen
def draw_text(screen, text, pos, font, color):
    text_surface = font.render(text, True, color)
    text_rect = text_surface.get_rect(center=pos)
    screen.blit(text_surface, text_rect)
