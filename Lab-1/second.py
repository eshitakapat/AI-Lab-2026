m = int(input("Enter the number of rows: "))
n = int(input("Enter the number of columns: "))

matrix1 = [[0] * n for _ in range (m)]
matrix2 = [[0] * n for _ in range (m)]

missing  = []

for i in range(m):
    for j in range(n):
        matrix1[i][j] = int(input(f"Enter element at position ({i}, {j}): for matrix 1: "))


for i in range(m):
    for j in range(n):
        matrix2[i][j] = int(input(f"Enter element at position ({i}, {j}): for matrix 2: "))


for i in range(m):
    for j in range(n):
        if((matrix1[i][j] != matrix2[i][j]) or (matrix1[i][j]*matrix2[i][j]==0)):
            missing.append((matrix1[i][j]))

print(f"Number of misplaced elements: ({len(missing)})")

print("Misplaced elements: ")
for i in missing:
    print(i)