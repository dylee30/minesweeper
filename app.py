from flask import Flask, render_template, request, redirect, url_for
import re
from game import Board

app = Flask(__name__)

# Default values for the Minesweeper game
DEFAULT_BOARD_LEN = 10
DEFAULT_BOMB_COUNT = 13

# Global variable to store the Minesweeper board
minesweeper_board = None


@app.route('/')
def index():
    global minesweeper_board
    if minesweeper_board is None:
        minesweeper_board = Board(DEFAULT_BOARD_LEN, DEFAULT_BOMB_COUNT)
    return render_template('index.html', board=minesweeper_board)


@app.route('/play', methods=['GET'])
def play():
    global minesweeper_board

    row = int(request.args.get('row'))
    col = int(request.args.get('col'))

    if row < 0 or row >= minesweeper_board.boardLen or col < 0 or col >= minesweeper_board.boardLen:
        return redirect(url_for('index'))

    safe = minesweeper_board.mine(row, col)

    if not safe:
        message = "AHH THE PAIN, YOU CLICKED ON A BOMB WHICH MEANS YOU LOST AND EXPLODED!"
    elif len(minesweeper_board.dug) == minesweeper_board.boardLen ** 2 - minesweeper_board.bombCount:
        message = "You Win!"
    else:
        return redirect(url_for('index'))

    minesweeper_board.dug = {(r, c) for r in range(minesweeper_board.boardLen) for c in range(minesweeper_board.boardLen)}
    return render_template('index.html', board=minesweeper_board, message=message)


@app.route('/flag', methods=['GET'])
def flag():
    global minesweeper_board

    row = int(request.args.get('row'))
    col = int(request.args.get('col'))

    if row < 0 or row >= minesweeper_board.boardLen or col < 0 or col >= minesweeper_board.boardLen:
        return redirect(url_for('index'))

    minesweeper_board.flag(row, col)

    return redirect(url_for('index'))


@app.route('/reset', methods=['GET'])
def reset():
    global minesweeper_board
    minesweeper_board = None
    return redirect(url_for('index'))


if __name__ == '__main__':
    app.run(debug=True)
