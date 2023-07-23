# 2048_python
Overview
This is a simple implementation of the popular 2048 game using Python and Tkinter for the GUI. The objective of the game is to slide numbered tiles on a grid to combine them and create a tile with the number 2048. The game ends when the grid is full, and no more moves can be made, or when the player successfully reaches the 2048 tile.

How to Play
Use the arrow keys (Up, Down, Left, Right) or the corresponding letters (W, S, A, D) to move the tiles in the respective direction.
Tiles with the same number will merge into one when they collide.
After every move, a new tile with the number 2 will appear in an empty cell.
Continue combining tiles until you reach the 2048 tile or until you cannot make any more moves.
Features
Simple and intuitive user interface using Tkinter.
Score tracking: The current score and the high score are displayed during the game.
Game Over and Victory Detection: The game will end and display a popup when you lose or reach the 2048 tile.
High Score Persistence: The high score is stored in the "GameData.txt" file for future sessions.
Customizable GUI: You can change the colors of the tiles and the grid easily by modifying the change_color function in the field.py file.
Requirements
Python 3.x
Tkinter (usually included in the standard library)
