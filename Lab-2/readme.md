# Lab-2: Graph Fundamentals in Python

This lab focuses on fundamental graph operations using Python. The scripts demonstrate how to work with graphs represented by both adjacency lists and adjacency matrices.

## Scripts

### `first.py`
**Purpose:** Counts the total number of edges in an undirected graph.
**Functionality:**
- Takes user input to build a graph as either an adjacency list or an adjacency matrix.
- `count_edges_list(adj_list)`: Calculates the number of edges from an adjacency list.
- `count_edges_matrix(matrix)`: Calculates the number of edges from an adjacency matrix.

### `second.py`
**Purpose:** Checks if two specified nodes are directly connected by an edge.
**Functionality:**
- Takes user input to build a graph (adjacency list or matrix) and to specify the two nodes to check.
- `is_connected_list(adj_list, u, v)`: Returns `True` if nodes `u` and `v` are connected in the adjacency list.
- `is_connected_matrix(matrix, u, v)`: Returns `True` if there is an edge between nodes `u` and `v` in the adjacency matrix.

### `third.py`
**Purpose:** Calculates the degree of every vertex in the graph.
**Functionality:**
- Takes user input to create a graph as an adjacency list or matrix.
- `degree_list(adj_list)`: Prints the degree of each vertex from the adjacency list.
- `degree_matrix(matrix)`: Prints the degree of each vertex from the adjacency matrix.

### `fourth.py`
**Purpose:** Verifies if a given sequence of nodes constitutes a valid path in the graph and determines its length.
**Functionality:**
- Takes user input for a graph (adjacency list or matrix) and a sequence of nodes.
- `check_path_list(adj_list, path)`: Checks for the path's existence in an adjacency list representation and returns a boolean and the path length.
- `check_path_matrix(matrix, path)`: Checks for the path's existence in an adjacency matrix representation and returns a boolean and the path length.

### `examples.py`
**Purpose:** Provides sample input and expected output for each of the scripts in this lab (`first.py`, `second.py`, `third.py`, `fourth.py`). This is useful for testing and understanding the programs' behavior.

## How to Run
Each Python script can be run directly from the command line. The programs will prompt the user for input to define the graph structure and other required parameters.

```bash
python <script_name>.py
```
For example:
```bash
python first.py
```
