# Pathfinder_AI


Pathfinder_AI is a part of Assignment 2A for the COS30019 - Introduction to Artificial Intelligence. This project implements search algorithms such as DFS, BFS, GBFS, ASTAR and 2 custom methods.

## Project Structure

[Project Structure](Assets/structure.png)


##  How It Works

Search methods are implemented as a class with a `.search(graph, origin, destination)` method. The input graph is taken from the input text file stored in `tests/test*.py` by using `utils/graph.py`.

For heuristics we have used the Euclidean distance  implemented in `utils/heuristics.py` because this is based on a 2D graph environment. This is used by GBFS and A* methods.

-> Manhattan distance could be used in future updates with the introduction of more dimensions.

## How to run the python program

Use the command line to run the script with your input graph file and method:

python3 search.py <path_to_input_text_file> <method>

**Example:**

python3 search.py tests/test2.txt DFS

##  Output Format

The execution output required by te assignment looks like this,

<filename> <method>  
<goal> <number_of_nodes_in_path>  
<full_path>

**Example:**

tests/test2.txt GBFS  
11 8  
1 3 5 6 7 9 10 11

## Test Files

- `test2.txt` – Basic multiple-destination test  
- `test3.txt` – Larger graph with branching  
- `test4.txt` – Multi-destination graph with fork paths  

## ✍️ Notes

- Follows assignment requirement: stop at **first reachable goal**  
- Expands nodes **in ascending order**, using the `sorted()` fucntion
- All methods return path and cost which is an additional feature  
- The structure of this code is implemented with further expandibility in mind.

## 👨‍💻 Author

- Student names: 
    *Ananda Pathiranage Ruveen Thathsilu Jayasinghe - 104317649*  
    *Denver Cope*
    *Rahat Alam*
    *Fayiz Kallupalathingal*

- Course: COS30019 - Introduction to Artificial Intelligence  
- Semester: 2025 HS1
