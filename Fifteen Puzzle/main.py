from puzzle import Puzzle
from bfs import Bfs

def main():
    # Read the puzzle from a file
    with open('4x4_01_00002.txt', 'r') as file:
        lines = file.readlines()

    # Parse the puzzle matrix from the file
    puzzle_rows = int(lines[0].split()[0])
    puzzle_columns = int(lines[0].split()[1])
    puzzle_matrix = []
    for line in lines[1:]:
        puzzle_matrix.append(list(map(int, line.strip().split())))

    # Create a Puzzle object with the parsed puzzle matrix
    strategy = "LURD"
    puzzle = Puzzle(puzzle_matrix, strategy)

    # Print the initial puzzle matrix
    print("Initial board:")
    print(puzzle)

    # Get the number of misplaced tiles
    print("Number of misplaced tiles:", puzzle.heuristic_hamming())

    # Get the Manhattan distance
    print("Manhattan distance:", puzzle.heuristic_manhattan())

    # Solve the puzzle using BFS
    bfs_solver = Bfs(puzzle)
    result = bfs_solver.solve()

    # Print the solution
    if result:
        print("Solution:", result["solution"])
        print("Path length:", result["path_length"])
        print("Visited states:", result["visited_states"])
        print("Processed states:", result["processed_states"])
        print("Max recursion depth:", result["max_recursion_depth"])
        print("Elapsed time:", result["elapsed_time"])
    else:
        print("Puzzle could not be solved.")

if __name__ == "__main__":
    main()
