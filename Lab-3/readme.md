# Lab-3: Python Data Structures and Algorithms

This lab contains a collection of Python scripts that implement various fundamental data structure operations and simple algorithms. The scripts cover operations on lists, dictionaries, and basic stack implementation.

## Scripts

### List Operations

#### `first.py`
**Purpose:** Provides a menu-driven interface for basic list operations.
**Functionality:**
- **Insert:** Adds an element to the list.
- **Delete:** Removes a specified element from the list.
- **Search:** Checks for the presence of an element in the list.

#### `second.py`
**Purpose:** Removes duplicate elements from a list.
**Functionality:**
- Defines a function `remove_duplicates(list1)` that iterates through a list and creates a new list containing only unique elements.

#### `third.py`
**Purpose:** Calculates the sum and average of numbers in a list.
**Functionality:**
- The `sum_and_average(numbers)` function computes the sum of all elements and then calculates their average.

#### `fourth.py`
**Purpose:** Finds the index of a specific element within a list.
**Functionality:**
- The `find_index(lst, element)` function returns the index of the first occurrence of the `element` or `-1` if it is not found.

#### `fifth.py`
**Purpose:** Swaps two elements in a list based on their indices.
**Functionality:**
- The `swap(lst, i, j)` function swaps the elements at index `i` and `j` in place.

### Dictionary Operations

#### `six.py`
**Purpose:** Demonstrates how to iterate through and print all keys and values in a dictionary.
**Functionality:**
- The `display(d)` function prints each key-value pair from the input dictionary `d`.

#### `seven.py`
**Purpose:** Counts the frequency of each element in a list using a dictionary.
**Functionality:**
- The `count_frequency(lst)` function returns a dictionary where keys are the elements from the list and values are their frequencies.

#### `eight.py`
**Purpose:** Checks for the existence of a key in a dictionary.
**Functionality:**
- Uses the `in` keyword to determine if a specified key is present in the dictionary and prints the result.

### Stack and 2D Grid

#### `ninth.py`
**Purpose:** Implements a basic stack data structure using a Python list.
**Functionality:**
- Provides a `stack()` function that can perform:
  - `push`: Appends an element to the list.
  - `pop`: Removes and returns the last element from the list.

#### `tenth.py`
**Purpose:** A collection of utility functions for working with a 2D grid represented by a list of lists.
**Functionality:**
- `get_valid_neighbors(grid, row, col)`: Returns a list of valid neighbors (up, down, left, right) for a given cell.
- `is_inside_grid(grid, row, col)`: Checks if a given cell's coordinates are within the grid's boundaries.
- `count_obstacles(grid)`: Counts the number of cells with a specific value (e.g., `0` for obstacles).

## How to Run
Each script is self-contained and can be executed from the command line:
```bash
python <script_name>.py
```
For example, to run the list operations menu:
```bash
python first.py
```
