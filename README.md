# Fifteen Puzzle

The repository contains a console application that searches the graph using three algorithms:
Breadth-First Search (BFS), Depth-First Search (DFS), and A* to solve an initial puzzle loaded from a file. In addition, it also provides 
statistical data on the performance of each algorithm in the research section

## Project Description
Fifteen is a sliding puzzle game played on a board filled with tiles arranged in a 4×4 square and numbered from 1 to 15. 
One square is empty and allows neighbouring tiles to be moved relative to each other. The goal of the puzzle is to place the tiles in numerical order,
left to right, top to bottom, with the empty square in the lower right corner. 

The programme uses graph search algorithms in which the root is the initial state of the puzzle, 
while the subsequent vertices are the child states of the puzzle, which are created by moving tiles according to the rules of the game.

## Built With
Tools used in the project:
* Python
* Matplotlib
* Numpy

## Getting Started
1. Clone the repository to your local machine:
```sh
git clone https://github.com/janrzepkowski/15Puzzle.git
```

2. Open IDE and select "Open an existing project." Navigate to the cloned repository and select the "Fifteen Puzzle" directory.

3. Configure Python interpreter.

4. To install the required packages, execute the following command in the terminal:
```sh
pip install -r requirements.txt
```

5. To run application, execute the following command in the terminal:
```sh
python main.py bfs RDUL tested_puzzles\4x4_01_00001.txt 4x4_01_00001_bfs_rdul_sol.txt 4x4_01_00001_bfs_rdul_stats.txt
```
where:

first parameter is algorithm name (bfs, dfs, astr)

the second parameter is the permutation of searches or heuristic (RDUL, DRUL, etc. for bfs and dfs, or manh, hamm for astr)

third is a file name with initial board state (file should be in the "tested_puzzles" directory)

fourth is a file name where application saves the solution

fifth is a file name where application saves the statistics


## Research section
All initial puzzle were tested at distances 1-7 from the final puzzle (a total of 413 puzzles) using each algorithm.
The following 8 search orders were used for the bfs and dfs strategies:
* right-down-up-left
* right-down-left-up
* down-right-up-left
* down-right-left-up
* left-up-down-right
* left-up-right-down
* up-left-down-right
* up-left-right-down

For the A* strategy, the Manhatan and Hamming heuristics were used. The results of the research are presented in the "Data.csv" file.

#### Data.csv columns explained

Example: 7 210 bfs drlu 7 924 444 7 13.000

1. Distance - 7
2. ID - 210
3. Algorithm - bfs
4. Processing order - drlu
5. Length - 7
6. Visited states - 924
7. Processed states - 444
8. Max recursion depth - 7
9. Elapsed time - 13.000 ms

Data on the various aspects considered in the comparisons are illustrated in charts and provided in the report (in Polish) or in "charts" directory.