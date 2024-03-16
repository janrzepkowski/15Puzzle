from puzzle import Puzzle
from bfs import BFS

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
    puzzle = Puzzle(puzzle_matrix)

    # Print the puzzle matrix
    print("Initial board:")
    print(puzzle)

    # Check if the puzzle is solvable
    print("Is solvable:", puzzle.is_solvable())

    # Get the number of misplaced tiles
    print("Number of misplaced tiles:", puzzle.heuristic_hamming())

    # Get the Manhattan distance
    print("Manhattan distance:", puzzle.heuristic_manhattan())

    solver = BFS(puzzle)
    search_order = ["D", "U", "L", "R"]  # permutacje kolejnosci przeszukiwania naerazie na sztywno nie wiem czy tak jest ok ale moze lepiej bedzie dodac w init w Puzzle class
    result = solver.solve(search_order) # patrz kom wyzej!!!!!!!!!!

    if result["solution"]:
        print("Solution found:")
        for move in result["solution"]:
            print(move, end=' ')  # Wydrukuj ruchy obok siebie
        print()  #linia dla czytelności
        print("Path length:", result["path_length"])
        print("Visited states:", result["visited_states"])
        print("Processed states:", result["processed_states"])
        print("Max recursion depth:", result["max_recursion_depth"])
        print("Elapsed time:", result["elapsed_time"])


        for move in result["solution"]:
            puzzle.move(move)
            print("Move:", move)
            print(puzzle)

    else:
        print("No solution found.")

if __name__ == "__main__":
    main()
