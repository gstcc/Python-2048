# 2048 Game - Python Project

![2048 Game](https://i.imgur.com/UDpB33R.png)

This project is an implementation of the popular 2048 game in Python using the Pygame library for graphical user interface (GUI) rendering. The game's objective is to slide numbered tiles on a grid to combine them and create a tile with the number 2048.


## How to Play

1. Use the arrow keys (Up, Down, Left, Right) to move the tiles in the corresponding directions.
2. When two tiles with the same number collide while moving, they merge into a new tile with the sum of their values.
3. The goal is to create a tile with the number 2048 by merging tiles. Once a tile with 2048 is created, you win the game.
4. The game ends when there are no possible moves left, and the board is full.

## Project Structure

The project consists of three Python files:

- `game_logic.py`: Contains the core game logic, including functions for board initialization, moving tiles, checking for game over, and handling the high score.
- `main.py`: The main script that runs the game loop, captures player inputs, and updates the display.
- `board_renderer.py`: Handles the graphical rendering of the game board, tiles, and the score bar.

## Dependencies

This project requires the following libraries:

- Python 3.x
- Pygame

## Installation

1. Clone or download the project from the GitHub repository.
2. Ensure you have Python 3.x installed on your system.
3. Install the required dependency, Pygame, using the following command:
   ```
   pip install pygame
   ```

## Usage

To start the game, run the `main.py` script using Python. This will launch the 2048 game window. Follow the instructions in the "How to Play" section to move the tiles and reach the target number of 2048.

## High Score

The game keeps track of the highest score achieved during a session. If you beat your highest score, it will be updated and saved. The high score is stored in a text file named `high_score.txt`.