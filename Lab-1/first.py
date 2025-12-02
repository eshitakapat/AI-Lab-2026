v = int(input("Enter number of vertices: "))
e = int(input("Enter number of edges: "))

matrix = [[0] * v for _ in range(v)]

for i  in range(e):
    u = int(input(f"Enter first vertex for edge {i}: "))
    w = int(input(f"Enter second vertex for edge {i}: "))
    matrix[u][w] = 1
    matrix[w][u] = 1

for row in matrix:
    print(row)