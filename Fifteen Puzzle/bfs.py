from collections import deque
import time

class BFS:
    def __init__(self, puzzle):
        self.puzzle = puzzle

    def solve(self, search_order):
        start_time = time.time()
        queue = deque([(self.puzzle, [])])  # Kolejka przechowująca układanki i ich ścieżki
        visited = set()  # Zbiór odwiedzonych układanek
        max_recursion_depth = 0  # Maksymalna osiągnięta głębokość rekursji

        while queue:
            current_puzzle, path = queue.popleft()  # Pobranie pierwszego elementu z kolejki
            visited.add(tuple(map(tuple, current_puzzle.board)))  # Dodanie układanki do odwiedzonych

            if len(path) > max_recursion_depth:
                max_recursion_depth = len(path)

            if current_puzzle.is_solved():
                end_time = time.time()
                elapsed_time = end_time - start_time
                return {
                    "path_length": len(path),
                    "visited_states": len(visited),
                    "processed_states": len(visited) + len(queue),
                    "max_recursion_depth": max_recursion_depth,
                    "elapsed_time": elapsed_time,
                    "solution": path
                }  # Jeśli układanka jest rozwiązana, zwróć dodatkowe informacje

            for move in search_order:  # Loop through the specified search order
                new_puzzle = current_puzzle.copy()  # Utworzenie kopii układanki
                new_puzzle.move(move)  # Wykonanie ruchu

                # Sprawdzenie czy nowa układanka nie została wcześniej odwiedzona
                if tuple(map(tuple, new_puzzle.board)) not in visited:
                    queue.append((new_puzzle, path + [move]))  # Dodanie układanki i jej ścieżki do kolejki

        end_time = time.time()
        elapsed_time = end_time - start_time
        return {
            "path_length": None,
            "visited_states": len(visited),
            "processed_states": len(visited) + len(queue),
            "max_recursion_depth": max_recursion_depth,
            "elapsed_time": elapsed_time,
            "solution": None
        }  # Jeśli nie udało się znaleźć rozwiązania, zwróć None
