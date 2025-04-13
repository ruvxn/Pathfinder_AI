# Pathfinder_AI

Pathfinder_AI is a part of Assignment 2A for the COS30019 - Introduction to Artificial Intelligence. This project implements search algorithms such as DFS, BFS, GBFS, ASTAR and 2 custom methods.

---

## Project Structure

```
Pathfinder_AI/
│
├── Assets/              # Visuals, structure diagrams
├── methods/             # DFS, BFS, GBFS, ASTAR, CUS1, CUS2
├── pseudocode/          # Pseudocode references
├── tests/               # Input graph test files
├── utils/               # Graph + Heuristic utility functions
│
├── GUI.py               # Graphical search visualizer
├── search.py            # Command-line search executor
├── requirements.txt     # Required dependencies
├── create_test.py       # Path testing helper
├── TreeBasedSearch.ipynb# Jupyter testing notebook
├── README.md            # Project information
```


---

## How It Works

Search methods are implemented as a class with a `search(self, graph, origin, destination)` method.  
The input graph is taken from the input text file stored in `tests/test*.txt` by using `utils/graph.py`.

We use Euclidean distance in `utils/heuristics.py` for GBFS and A* (suited to 2D graphs).  
Manhattan distance can be added in the future for other environments.

---

## How to Run (Command Line)

Use the command line to run the script with your input graph file and method:

```bash
python3 search.py <path_to_input_text_file> <search_method>
```

Example:

```bash
python3 search.py tests/test2.txt DFS
```

---

## How to Run (Graphical GUI)

1. Install requirements:

```bash
pip install -r requirements.txt
```

Or manually:

```bash
pip install pygame
```

2. Run the GUI version:

```bash
python GUI.py tests/test2.txt DFS
```

3. Press Enter when prompted to start the visual traversal.

---

## Output Format

The execution output required by the assignment looks like this:

```
<input_text_filename> <search_method>  
<destination_goal> <number_of_nodes_in_path>  
<full_path>
```

Example:

```
tests/test2.txt GBFS  
11 8  
1 3 5 6 7 9 10 11
```

---

## Test Files

- `test1.txt` – Basic pathfinding test  
- `test3.txt` – Larger graph with multiple branches  
- `test4.txt` – Multi-destination test with forked paths  
- `test5.txt` – Edge case with multiple potential goal paths  
- `DFS_test.txt` – Specifically designed for DFS validation  
- `BFS_test.txt` – BFS-focused graph structure  
- `GBFS_test.txt` – Heuristic-based graph to test GBFS  
- `ASTARTest.txt` – Test case targeting A* algorithm  
- `CUS1_test.txt` – Designed for Uniform Cost Search (CUS1)  
- `CUS2test.txt` – Tailored for the custom CUS2 algorithm  
- `PathFinder-test.txt` – Overall integrated scenario testing

---

## Notes

- Follows assignment rule: stops at first reachable goal  
- Expands nodes in ascending order using `sorted()`  
- All methods return both the path and cost  
- Modular codebase built for easy extension


---

## Group Members

- Ananda Pathiranage Ruveen Thathsilu Jayasinghe - 104317649  
- Denver Cope - 104738758  
- Rahat Alam - 103810105  
- Fayiz Kallupalathingal - 104658733

---

## Course Info

- Course: COS30019 - Introduction to Artificial Intelligence  
- Semester: 2025 HS1

---

## Repository

[GitHub Repo – Pathfinder_AI](https://github.com/ruvxn/Pathfinder_AI)
