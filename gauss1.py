import numpy as np

def eliminasi_gauss(A, b):
    A = A.astype(float)
    b = b.astype(float)
    n = len(b)

    # Eliminasi Maju (Forward Elimination)
    for i in range(n):
        if A[i][i] == 0:
            for j in range(i+1, n):
                if A[j][i] != 0:
                    A[[i, j]] = A[[j, i]]
                    b[i], b[j] = b[j], b[i]
                    break
        for j in range(i+1, n):
            factor = A[j][i] / A[i][i]
            A[j] = A[j] - factor * A[i]
            b[j] = b[j] - factor * b[i]

    # Substitusi Mundur (Back Substitution)
    x = np.zeros(n)
    for i in range(n-1, -1, -1):
        x[i] = (b[i] - np.dot(A[i][i+1:], x[i+1:])) / A[i][i]
    return x

# Contoh Soal:
# 2x + 3y - z = 5
# 4x + 4y - 3z = 3
# -2x + 3y - z = 1
A = np.array([[2, 3, -1],
              [4, 4, -3],
              [-2, 3, -1]])
b = np.array([5, 3, 1])

solusi = eliminasi_gauss(A.copy(), b.copy())

print("Solusi sistem persamaan dengan metode Eliminasi Gauss:")
for i, val in enumerate(solusi):
    print(f"x{i+1} = {val:.2f}")
