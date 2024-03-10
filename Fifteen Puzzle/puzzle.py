class Puzzle:
    def __init__(self, board):
        self.board = board
        self.rows = len(board)
        self.columns = len(board[0])
        self.final_board = self.generate_final_board()

    def __str__(self):
        puzzle_string = ''

        for i in range(self.rows):
            for j in range(self.columns):
                puzzle_string += ' {0: >2}'.format(str(self.board[i][j]))
            puzzle_string += '\n'

        return puzzle_string

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

    def swap(self, x1, y1, x2, y2):
        puzzle_copy = [list(row) for row in self.board]
        puzzle_copy[x1][y1], puzzle_copy[x2][y2] = puzzle_copy[x2][y2], puzzle_copy[x1][y1]

        return puzzle_copy

    @staticmethod
    def is_odd(num):
        return num % 2 != 0

    @staticmethod
    def is_even(num):
        return num % 2 == 0

    def get_blank_space_row_counting_from_bottom(self):
        zero_row, _ = self.get_coordinates(0)
        return self.rows - zero_row

    def get_coordinates(self, cell, board=None):
        if not board:
            board = self.board

        for i in range(self.rows):
            for j in range(self.columns):
                if board[i][j] == cell:
                    return i, j

        return RuntimeError('Invalid tile value')

    '''
    Inwersja to para dwóch liczb i i j takich, że i występuje później niż j w kolejności,
    w której powinny się pojawić, ale i jest mniejsze od j. Na przykład:
    5 6 7
    1 2 3
    4 0 8
    Mamy 3 inwersje: (1, 5), (2, 5), i (3, 5),
    gdyż 1, 2, i 3 powinny wystąpić przed 5, ale nie są.
    '''
    def get_inversions(self):
        inversions = 0
        puzzle_list = [number for row in self.board for number in row if number != 0]

        for i in range(len(puzzle_list)):
            for j in range(i + 1, len(puzzle_list)):
                if puzzle_list[i] > puzzle_list[j]:
                    inversions += 1

        return inversions

    def get_moves(self):
        moves = []
        i, j = self.get_coordinates(0)  # blank space

        if i > 0:
            moves.append(Puzzle(self.swap(i, j, i - 1, j)))  # move up

        if j < self.columns - 1:
            moves.append(Puzzle(self.swap(i, j, i, j + 1)))  # move right

        if j > 0:
            moves.append(Puzzle(self.swap(i, j, i, j - 1)))  # move left

        if i < self.rows - 1:
            moves.append(Puzzle(self.swap(i, j, i + 1, j)))  # move down

        return moves

    def heuristic_misplaced(self):
        misplaced = 0

        for i in range(self.rows):
            for j in range(self.columns):
                if self.board[i][j] != self.final_board[i][j]:
                    misplaced += 1

        return misplaced

    def heuristic_manhattan_distance(self):
        distance = 0

        for i in range(self.rows):
            for j in range(self.columns):
                i1, j1 = self.get_coordinates(self.board[i][j], self.final_board)
                distance += abs(i - i1) + abs(j - j1)

        return distance

    def is_solvable(self):
        """
         1. If N is odd, then puzzle instance is solvable if number of inversions is even in the input state.
         2. If N is even, puzzle instance is solvable if
            - the blank is on an even row counting from the bottom (second-last, fourth-last, etc.)
              and number of inversions is odd.
            - the blank is on an odd row counting from the bottom (last, third-last, fifth-last, etc.)
            and number of inversions is even.
         3. For all other cases, the puzzle instance is not solvable.
        """

        inversions_count = self.get_inversions()
        blank_position = self.get_blank_space_row_counting_from_bottom()

        if self.is_odd(self.rows) and self.is_even(inversions_count):
            return True
        elif self.is_even(self.rows) and self.is_even(blank_position) and self.is_odd(inversions_count):
            return True
        elif self.is_even(self.rows) and self.is_odd(blank_position) and self.is_even(inversions_count):
            return True
        else:
            return False