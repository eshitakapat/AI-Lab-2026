#represent a 2-D grid using a list of lists.
#print all valid neighbours (up, down, left, right) of a given cell in the grid.
#check if a cell is inside grid boundaries
#count obstacles(0s) in a grid

def get_valid_neighbors(grid, row, col):
    neighbors = []
    if row > 0:
        neighbors.append(grid[row-1][col])
    if row < len(grid)-1:
        neighbors.append(grid[row+1][col])
    if col > 0:
        neighbors.append(grid[row][col-1])
    if col < len(grid[0])-1:
        neighbors.append(grid[row][col+1])
    return neighbors
grid = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
row = 1
col = 1
valid_neighbors = get_valid_neighbors(grid, row, col)
print(valid_neighbors)

def count_obstacles(grid):
    count = 0
    for row in grid:
        for cell in row:
            if cell == 0:
                count += 1
    return count