from collections import deque
import time


class Bfs:
    def __init__(self, puzzle):
        self.puzzle = puzzle
        self.visited_states = 1
        self.processed_states = 0
        self.elapsed_time = 0
        self.max_recursion_reached = 0
        self.visited = set()

    def solve(self):
        start_time = time.time()
        queue = deque([(self.puzzle, [])])  # Kolejka przechowująca układanki i ich ścieżki
        self.visited.add(tuple(map(tuple, self.puzzle.board)))
        # map(tuple, self.puzzle.board) mapujemy kazdy wiersz planszy na krotke - tuple
        # tuple(map(tuple, self.puzzle.board)) zamieniamy na krotke krotek, a kazda krotka to jeden wiersz ukladanki

        while queue:
            current_puzzle, path = queue.popleft()  # Pobranie pierwszego elementu z kolejki
            self.processed_states += 1

            if len(path) > self.max_recursion_reached:
                self.max_recursion_reached = len(path)

            if current_puzzle.is_solved():
                end_time = time.time()
                self.elapsed_time = end_time - start_time
                return {
                    "path_length": len(path),
                    "visited_states": self.visited_states,
                    "processed_states": self.processed_states,
                    "max_recursion_reached": self.max_recursion_reached,
                    "elapsed_time": self.elapsed_time,
                    "solution": path
                }  # Jeśli układanka jest rozwiązana, zwróć dodatkowe informacje
            current_puzzle.move()
            for neighbor in current_puzzle.get_neighbors():  # Loop through the specified search order
                # Sprawdzenie czy nowa układanka nie została wcześniej odwiedzona
                neighbor_tuple = tuple(map(tuple, neighbor.board))
                if neighbor_tuple not in self.visited:
                    self.visited.add(neighbor_tuple)
                    queue.append((neighbor, path + [neighbor.last_move]))  # Dodanie układanki i jej ścieżki do kolejki
                    self.visited_states += 1

        end_time = time.time()
        self.elapsed_time = end_time - start_time
        return None