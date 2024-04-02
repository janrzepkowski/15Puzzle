import copy

class Puzzle:

    UP = (-1, 0)
    DOWN = (1, 0)
    LEFT = (0, -1)
    RIGHT = (0, 1)

    def __init__(self, board, strategy):
        self.board = board
        self.rows = len(board)
        self.columns = len(board[0])
        self.final_board = self.generate_final_board()
        self.last_move = None
        if strategy == "manh" or strategy == "hamm":  # tylko jesli A*
            self.strategy = "LURD"  # na sztywno daje wybrana permutacje
            self.heuristic = strategy
        else:
            self.strategy = strategy
            self.heuristic = None
        self.neighbors = []
        self.depth = 0
        self.parent = None

    def __str__(self):
        puzzle_string = ''

        for i in range(self.rows):
            for j in range(self.columns):
                puzzle_string += ' {0: >2}'.format(str(self.board[i][j]))
            puzzle_string += '\n'

        return puzzle_string

    def __copy__(self):
        new_puzzle = copy.deepcopy(self.board)
        new_instance = Puzzle(new_puzzle, self.strategy)
        new_instance.last_move = self.last_move
        new_instance.strategy = self.strategy
        new_instance.depth = self.depth + 1
        new_instance.heuristic = self.heuristic
        new_instance.parent = self
        return new_instance

    def __lt__(self, other):
        return True

    def get_neighbors(self):
        return self.neighbors

    def generate_final_board(self):
        final_board = []
        new_row = []

        for i in range(1, self.rows * self.columns + 1):
            new_row.append(i)
            if len(new_row) == self.columns:
                final_board.append(new_row)
                new_row = []

        final_board[-1][-1] = 0

        return final_board

    def move(self):
        i, j = self.get_coords(0)
        for move in self.strategy:
            if move == "U" and self.last_move != "D" and i > 0:
                self.neighbors.append(self.swap(move))
            elif move == "L" and self.last_move != "R" and j > 0:
                self.neighbors.append(self.swap(move))
            elif move == "D" and self.last_move != "U" and i < self.rows - 1:
                self.neighbors.append(self.swap(move))
            elif move == "R" and self.last_move != "L" and j < self.columns - 1:
                self.neighbors.append(self.swap(move))

    def swap(self, move):
        n = self.__copy__() # n wzielo sie od new puzzle zeby bylo krocej xd
        n.last_move = move
        if move == "U":
            direction = n.UP
        elif move == "D":
            direction = n.DOWN
        elif move == "R":
            direction = n.RIGHT
        elif move == "L":
            direction = n.LEFT
        new_blank = (n.get_coords(0)[0] + direction[0], n.get_coords(0)[1] + direction[1])
        n.board[n.get_coords(0)[0]][n.get_coords(0)[1]] = n.board[new_blank[0]][new_blank[1]]
        n.board[new_blank[0]][new_blank[1]] = 0
        return n

    def get_coords(self, value, board=None):
        if not board:
            board = self.board

        for i in range(self.rows):
            for j in range(self.columns):
                if board[i][j] == value:
                    return i, j

        return RuntimeError('Invalid tile value')

    def is_solved(self):
        return self.board == self.final_board

    def heuristic_manhattan(self):
        distance = 0
        for i in range(self.rows):
            for j in range(self.columns):
                if self.board[i][j] != 0:
                    i1, j1 = self.get_coords(self.board[i][j], self.final_board)
                    distance += abs(i - i1) + abs(j - j1)

        return distance

    def heuristic_hamming(self):
        misplaced = 0
        for i in range(self.rows):
            for j in range(self.columns):
                if self.board[i][j] != 0 and self.board[i][j] != self.final_board[i][j]:
                    misplaced += 1

        return misplaced

    def get_heuristic_cost(self):
        if self.heuristic == "hamm":
            return self.heuristic_hamming()
        else:
            return self.heuristic_manhattan()