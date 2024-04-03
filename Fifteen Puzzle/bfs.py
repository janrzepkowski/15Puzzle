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
        queue = deque([(self.puzzle, [])])
        self.visited.add(tuple(map(tuple, self.puzzle.board)))

        while queue:
            current_puzzle, path = queue.popleft()
            self.processed_states += 1

            self.max_recursion_reached = max(self.max_recursion_reached, len(path))

            if current_puzzle.is_solved():
                self.elapsed_time = time.time() - start_time
                return {
                    "path_length": len(path),
                    "visited_states": self.visited_states,
                    "processed_states": self.processed_states,
                    "max_recursion_reached": self.max_recursion_reached,
                    "elapsed_time": self.elapsed_time,
                    "solution": path
                }

            current_puzzle.move()
            for neighbor in current_puzzle.get_neighbors():
                neighbor_tuple = tuple(map(tuple, neighbor.board))
                if neighbor_tuple not in self.visited:
                    self.visited.add(neighbor_tuple)
                    queue.append((neighbor, path + [neighbor.last_move]))
                    self.visited_states += 1

        self.elapsed_time = time.time() - start_time
        return None