# Minesweeper Game
#### Video Demo: https://youtu.be/EGiLOxIXOl0
#### Description:
# Minesweeper Web Application

## Overview

This Minesweeper web application is a classic implementation of the popular Minesweeper game. The game is built using Python for the server-side logic, Flask as the web framework, and HTML with Jinja templating for the frontend. The Minesweeper game allows users to explore a grid of cells, avoiding hidden bombs while revealing the number of neighboring bombs in each uncovered cell.

## Features
Classic Minesweeper Gameplay: Experience the timeless challenge of Minesweeper with a clean and intuitive web interface.

Dynamic Board Rendering: The game dynamically renders the Minesweeper board using HTML and Jinja templating, allowing for a seamless and responsive user experience.

User Interaction: Users can interact with the game by clicking on cells to reveal them or right-clicking to flag potential bombs. The design focuses on simplicity and ease of use.

## Files and Their Purposes

### `app.py`

This Python file serves as the main server-side script using the Flask web framework. It handles routing, communicates with the Minesweeper game logic, and renders HTML templates to the user's browser. The key functionalities include starting a new game, making moves (revealing or flagging cells), and restarting the game.

Key Functionalities:
1. Starting a New Game: Initializes a new instance of the Minesweeper game.
2. Making Moves: Handles user inputs for revealing or flagging cells on the game board.
3. Restarting the Game: Provides the functionality to restart the game.

### `game.py`

The `game.py` file contains the logic for the Minesweeper game. It defines the `Board` class, responsible for creating and managing the game board. The class includes methods for initializing the board, revealing cells, flagging cells, and handling game state.

Key Functionalities:
1. Board Initialization: Creates the Minesweeper board with random bomb placement.
2. Cell Actions: Implements methods for revealing cells, flagging potential bombs, and handling the consequences of each action.
3. Game State Handling: Checks and updates the game state based on user actions.

### `templates/index.html`

This HTML file is a Jinja template used to render the Minesweeper game interface. It includes the game board, a "Play Again" button, and the necessary JavaScript code for user interactions. The template dynamically displays the state of the game board and handles user inputs for revealing or flagging cells.

Key Components:
1. Game Board Display: Dynamically renders the Minesweeper board based on the state of the Python Board object.
2. User Interaction Handling: Uses JavaScript to respond to user clicks on cells for revealing or flagging.

## Design and User Interaction

The Minesweeper board is represented as a two-dimensional list in Python. Each cell in the list corresponds to a cell on the game board, and the contents of the cell determine whether it contains a bomb, a number indicating neighboring bombs, or is empty. User interaction is facilitated through a simple web interface. The use of HTML with Jinja templating allows for dynamic rendering of the game board based on the state of the Python `Board` object. JavaScript is employed to handle user clicks, updating the frontend without requiring a full page reload. Users can click on cells to reveal them or right-click to flag a potential bomb.
