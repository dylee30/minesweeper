import random
import re

class Board:
    def __init__(self, boardLen, bombCount):
        # Initialize the board with dimensions and number of bombs
        self.boardLen = boardLen
        self.bombCount = bombCount
        # Create the game board and initialize the set of dug positions
        self.board = self.create_board()
        self.set_board()
        self.dug = set()
        self.flagged = set()

    def create_board(self):
        # Create a new game board with empty cells and randomly place bombs
        board = [[' ' for _ in range(self.boardLen)] for _ in range(self.boardLen)]
        bombs = 0
        while bombs < self.bombCount:
            pos = random.randint(0, self.boardLen**2 - 1)
            r = pos // self.boardLen
            c = pos % self.boardLen
            if board[r][c] == '*':
                continue
            board[r][c] = '*'
            bombs += 1
        return board

    def set_board(self):
         # set values to non-bomb cells based on the number of bomb neighbors
        for r in range(self.boardLen):
            for c in range(self.boardLen):
                if self.board[r][c] == '*':
                    continue
                self.board[r][c] = str(self.neighbor_count(r, c))

    def neighbor_count(self, row, col):
        # Calculate the number of bomb neighbors for each cell unless the cell is a bomb
        count = 0
        lower_row = max(0, row - 1)
        upper_row = min(self.boardLen - 1, row + 1)
        lower_col = max(0, col - 1)
        upper_col = min(self.boardLen - 1, col + 1)
        for r in range(lower_row, upper_row + 1):
            for c in range(lower_col, upper_col + 1):
                if r == row and c == col:
                    continue
                if self.board[r][c] == '*':
                    count += 1
        return count

    def mine(self, row, col):
        # mine the specified cell
        self.dug.add((row, col))
        if self.board[row][col] == '*':
            return False
        elif self.board[row][col] != ' ':
            return True

        # Recursively dig neighboring cells if the current cell is empty
        lower_row = max(0, row - 1)
        upper_row = min(self.boardLen - 1, row + 1)
        lower_col = max(0, col - 1)
        upper_col = min(self.boardLen - 1, col + 1)
        for r in range(lower_row, upper_row + 1):
            for c in range(lower_col, upper_col + 1):
                if (r, c) in self.dug:
                    continue
                self.mine(r, c)
        return True

    def __repr__(self):
            # Provide a string representation of the board (calls __str__)
            return self.__str__()

    def __str__(self):
        # Create a string representation of the game board for display
        printed = [[' ' for _ in range(self.boardLen)] for _ in range(self.boardLen)]
        for row in range(self.boardLen):
            for col in range(self.boardLen):
                if (row, col) in self.dug:
                    printed[row][col] = str(self.board[row][col])
                else:
                    printed[row][col] = '💣' if self.board[row][col] == '*' else ' '

        x = ''
        index = '   '
        c = []

        # Display column indices
        for indices in range(self.boardLen):
            columns = map(lambda x: x[indices], printed)
            max_width = len(max(columns, key=len))
            c.append(str(indices).center(max_width))
        index += '  '.join(c)
        index += '\n'

        for i in range(len(printed)):
            row = printed[i]
            x += f'{i} |'
            c = []
            for indices, col in enumerate(row):
                format_str = f'%-{len(index.split()[indices]) - 1}s'
                c.append(format_str % col)
            x += ' |'.join(c)
            x += ' |\n'

        str_len = len(x.split('\n')[0])
        x = index + '-' * str_len + '\n' + x + '-' * str_len

        return x

    def __getitem__(self, index):
        return self.board[index]

    def flag(self, row, col):
        # Flag the specified cell
        if (row, col) not in self.dug:
            if (row, col) in self.flagged:
                self.flagged.remove((row, col))
            else:
                self.flagged.add((row, col))


def minesweeper(boardLen=10, bombCount=13):
    board = Board(boardLen, bombCount)

    while len(board.dug) < board.boardLen**2 - bombCount:
        print(board)
        user_input = re.split(',\\s*', input("Input [row],[col] for where you want to mine or flag: "))
        row, col = int(user_input[0]), int(user_input[-1])

        if row < 0 or row >= board.boardLen or col < 0 or col >= board.boardLen:
            print("Location Out Of Bounds. Please try another move: ")
            continue

        action = input("Enter 'm' to mine or 'f' to flag: ")
        if action == 'm':
            safe = board.mine(row, col)
            if not safe:
                break  # game over
        elif action == 'f':
            board.flag(row, col)
        else:
            print("Invalid action. Please enter 'm' to mine or 'f' to flag.")

    if safe and len(board.flagged) == bombCount:
        print("You Win!")
    elif len(board.dug) == board.boardLen**2:
        print("All tiles revealed, but not all bombs flagged. You Lose!")
    else:
        print("You Dug A Bomb! You Lose!")

    board.dug = {(r, c) for r in range(board.boardLen) for c in range(board.boardLen)}
    print(board)

