import argparse
from puzzle import Puzzle
from dfs import Dfs
from bfs import Bfs
from astar import Astar

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("strategy", choices=["bfs", "dfs", "astr"])
    parser.add_argument("param")
    parser.add_argument("input_file")
    parser.add_argument("solution_file")
    parser.add_argument("stats_file")
    args = parser.parse_args()

    with open(args.input_file, 'r') as file:
        lines = file.readlines()

    puzzle_rows = int(lines[0].split()[0])
    puzzle_columns = int(lines[0].split()[1])
    puzzle_matrix = []
    for line in lines[1:]:
        puzzle_matrix.append(list(map(int, line.strip().split())))

    puzzle = Puzzle(puzzle_matrix, args.param)

    result = None
    if args.strategy == "bfs":
        bfs = Bfs(puzzle)
        result = bfs.solve()
    elif args.strategy == "dfs":
        dfs = Dfs()
        result = dfs.dfs_solve(puzzle)
    elif args.strategy == "astr":
        astr = Astar(puzzle)
        result = astr.solve()

    with open(args.solution_file, 'w') as file:
        if result is None:
            file.write("-1\n")
        else:
            file.write(f"{len(result['solution'])}\n")
            file.write(' '.join(result['solution']))

    with open(args.stats_file, 'w') as file:
        if result is None:
            file.write("-1\n")
        else:
            file.write(f"{len(result['solution'])}\n")
        file.write(f"{result['visited_states']}\n")
        file.write(f"{result['processed_states']}\n")
        file.write(f"{result['max_recursion_reached']}\n")
        file.write(f"{result['elapsed_time']:.3f}\n")

if __name__ == "__main__":
    main()