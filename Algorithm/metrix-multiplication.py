#ADVANCED: MATRIX MULTIPLICATION


# Native Method: Multiplying two matrices using nested loops

# 2X2 matrix "X"
X = [[1, 2],[2, 3]]

# 2X2 matrix "Y"
Y = [[2, 3],[3, 4]]

# Initialize the result matrix for X * Y
result_XY = [[0, 0], [0, 0]]

# Perform the multiplication of X and Y
for i in range(len(X)):            # Iterate over rows of X
    for j in range(len(Y[0])):      # Iterate over columns of Y
        for k in range(len(Y)):     # Iterate over rows of Y
            result_XY[i][j] += X[i][k] * Y[k][j]

print("Result of X * Y:", result_XY)

# 2X2 matrix "Z"
Z = [[6, 7], [2, 6]]

# Initialize the result matrix for (X * Y) * Z
result_XZ = [[0, 0], [0, 0]]

# Perform the multiplication of result_XY and Z
for i in range(len(result_XY)):       # Iterate over rows of result_XY
    for j in range(len(Z[0])):        # Iterate over columns of Z
        for k in range(len(Z)):       # Iterate over rows of Z
            result_XZ[i][j] += result_XY[i][k] * Z[k][j]

print("Result of (X * Y) * Z:", result_XZ)

P = [[9, 9], [7, 6]]
# Initialize the result matrix for P * Z
result_PZ = [[0, 0], [0, 0]]

# Perform the multiplication of Z and P
for i in range(len(result_XZ)):       # Iterate over rows of result_XY
    for j in range(len(P[0])):        # Iterate over columns of Z
        for k in range(len(P)):       # Iterate over rows of Z
            result_PZ[i][j] += result_XZ[i][k] * P[k][j]

print("Result of Z * P:", result_PZ)