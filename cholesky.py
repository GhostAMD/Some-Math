from scipy.linalg import cholesky, solve_triangular
import numpy as np
def algo_cholesky(A):
    R= np.zeros_like(A)
    R[0][0] = np.sqrt(A[0][0])
    for j in range(1, A.shape[0]):
        R[0][j] = A[0][j] / R[0][0]
    for i in range(1, A.shape[0]):
        for j in range(0,A.shape[0]):
            R[i][i] = np.sqrt(A[i][i]- np.dot(R[:i,i],R[:i,i]))
            if i != j:
                if i < j:
                    R[i][j] = (A[i][j] - np.dot(R[:i,i],R[:i,j])) / R[i][i]
                else:
                    R[i][j] = 0
    return R
    
def cholesky_decomposition(matrix):
    R = cholesky(matrix, lower=True)
    return R.T

# test 
A= np.array([[1,2,1],[2,13,-1],[1,-1,3]])
R =cholesky_decomposition(A)
print (R)
R2=algo_cholesky(A)
print (R2)
print ("Verification de la decomposition:")
print(np.allclose(R, R2))



#resoudre un systeme
"""def solve_cholesky(A, b):
    L = cholesky(A, lower=True)
    y = np.linalg.solve_triangular(L, b)
    x = np.linalg.solve_triangular(L.T, y)
    return x
# Test de la résolution d'un système"""


