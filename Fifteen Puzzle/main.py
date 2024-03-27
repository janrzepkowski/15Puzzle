from puzzle import Puzzle
from dfs import Dfs
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

    print("Initial board:")
    print(puzzle)

    print("Number of misplaced tiles:", puzzle.heuristic_hamming())
    print("Manhattan distance:", puzzle.heuristic_manhattan())

    dfs = Dfs()
    solution, max_recursion_reached, visited_states, processed_states, elapsed_time = dfs.dfs_solve(puzzle)

    print("Solution:", solution)
    print("Max recursion depth:", max_recursion_reached)
    print("Visited states:", visited_states)
    print("Processed states:", processed_states)
    print("Elapsed time:", elapsed_time)

    new_puzzle = puzzle
    for move in solution:
        new_puzzle = new_puzzle.swap(move)
    print(new_puzzle)

if __name__ == "__main__":
    main()