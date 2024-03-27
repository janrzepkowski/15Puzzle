import time


class Dfs:

    def __init__(self):
        self.visited_states = 1
        self.processed_states = 0
        self.elapsed_time = 0
        self.max_recursion_depth = 20
        self.visited = {}
        self.path = ""

    def solve(self, puzzle):
        self.processed_states += 1

        if puzzle.depth > self.max_recursion_depth:
            return None

        if puzzle.is_solved():
            return self.path

        self.visited[tuple(map(tuple, puzzle.board))] = puzzle.depth # krotka to klucz a wartoscia jest dlugosc sciezki
        puzzle.move()

        for neighbor in puzzle.get_neighbors():
            self.visited_states += 1
            # Sprawdzenie czy nowa układanka nie została wcześniej odwiedzona
            neighbor_tuple = tuple(map(tuple, neighbor.board))
            # bez warunku w nawiasie dziala szybciej ale rozwiazanie jest niezgodne z zadana strategia. Do przemyslenia.
            if (neighbor_tuple in self.visited and neighbor.depth < self.visited[neighbor_tuple]) or neighbor_tuple not in self.visited:
                self.path += neighbor.last_move
                result = self.solve(neighbor)
                if result is not None:
                    return result
                self.path = self.path[:-1]
        return None

    def dfs_solve(self, puzzle):
        star_time = time.time()
        self.solve(puzzle)
        self.elapsed_time = time.time() - star_time
        return self.path, len(self.path), self.visited_states, self.processed_states, self.elapsed_time
