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

        self.visited[tuple(map(tuple, puzzle.board))] = puzzle.depth
        puzzle.move()

        for neighbor in puzzle.get_neighbors():
            self.visited_states += 1
            neighbor_tuple = tuple(map(tuple, neighbor.board))
            if (neighbor_tuple in self.visited and neighbor.depth < self.visited[neighbor_tuple]) or neighbor_tuple not in self.visited:
                self.path += neighbor.last_move
                result = self.solve(neighbor)
                if result is not None:
                    return result
                self.path = self.path[:-1]
        return None

    def dfs_solve(self, puzzle):
        start_time = time.time_ns() // 1_000_000
        solution = self.solve(puzzle)
        self.elapsed_time = time.time_ns() // 1_000_000 - start_time
        return {
            "solution": solution,
            "path_length": len(solution),
            "visited_states": self.visited_states,
            "processed_states": self.processed_states,
            "max_recursion_reached": self.max_recursion_depth,
            "elapsed_time": self.elapsed_time
        }