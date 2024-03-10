from puzzle import Puzzle

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
    print(puzzle)

    # Print the end position
    print("End position:")
    print(puzzle.final_board)

    # Check if the puzzle is solvable
    print("Is solvable:", puzzle.is_solvable())

    # Get the number of possible moves
    print("Number of possible moves:", len(puzzle.get_moves()))

    # Get the number of misplaced tiles
    print("Number of misplaced tiles:", puzzle.heuristic_misplaced())

    # Get the Manhattan distance
    print("Manhattan distance:", puzzle.heuristic_manhattan_distance())
    print(puzzle.get_coordinates(0))


if __name__ == "__main__":
    main()
