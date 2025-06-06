from scipy.linalg import lu, det, solve_triangular
import numpy as np

A=[[1,4],
   [-1,2]]

B=[[-2,3,0],
   [1,0,-4],
   [2,0,5]]

def resolution_LU(A, b):
    # Decomposition en LU
    P, L, U = lu(A)
    # Résolution de Ly = Pb
    y = solve_triangular(L, np.dot(P,b), lower=True)
    x = solve_triangular(U, y)
    return x

# Test de la fonction

print("Matrice B:")
print(B)
b=np.transpose([1,2,3])
x = resolution_LU(B, b)
print("Solution x:")
print(x)
print("Vérification de la solution:")
print(np.dot(B, x))

#calculer l'inverse de B
inverse_B= resolution_LU(B, np.eye(3))
print("Inverse de B:")
print(inverse_B)
