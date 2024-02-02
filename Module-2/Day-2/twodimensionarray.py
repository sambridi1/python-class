A = [[2,3,4],[3,4,5],[5,6,7]]
B = [[1,2,3],[2,3,4],[4,5,6]]
C = [[0, 0, 0],
     [0, 0, 0],
     [0, 0, 0]]
for i in range(3):
    for j in range(3):
        C[i][j] = A[i][j] + B[i][j]
print("Result of matrix addition:")
for row in C:
    print(row)