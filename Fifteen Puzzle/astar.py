import time
import heapq

class Astar:
    def __init__(self, puzzle):
        self.puzzle = puzzle
        self.visited_states = 0
        self.processed_states = 0
        self.start_time = 0

    def solve(self):
        self.start_time = time.time()
        heap = [(0, self.puzzle)]
        visited = set()

        while heap:
            _, current_puzzle = heapq.heappop(heap)
            self.processed_states += 1
            visited.add(tuple(map(tuple, current_puzzle.board)))

            if current_puzzle.is_solved():
                path = self.trace_path(current_puzzle)
                return self.get_result(path)

            current_puzzle.move()
            for neighbor in current_puzzle.get_neighbors():
                self.visited_states += 1
                neighbor_tuple = tuple(map(tuple, neighbor.board))
                if neighbor_tuple not in visited:
                    cost = neighbor.depth + neighbor.get_heuristic_cost()
                    heapq.heappush(heap, (cost, neighbor))

        return None

    def trace_path(self, puzzle):
        path = ""
        while puzzle and puzzle.last_move:
            path += puzzle.last_move
            puzzle = puzzle.parent
        return path[::-1]

    def get_result(self, path):
        self.elapsed_time = time.time() - self.start_time
        return {
            "solution": path,
            "visited_states": self.visited_states,
            "processed_states": self.processed_states,
            "elapsed_time": self.elapsed_time
        }