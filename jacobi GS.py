import numpy as np

def init_EF(matrix):
    D, F, E = np.zeros(np.shape(matrix)), np.zeros(np.shape(matrix)), np.zeros(np.shape(matrix))
    for i in range (np.shape(matrix)[0]):
        for j in range (np.shape(matrix)[0]):
            if i==j:
                D[i][j]=matrix[i][j]
            elif i<j:
                E[i][j]=-matrix[i][j]
            else:
                F[i][j]=-matrix[i][j]
    return D, F, E
                  
def solution_iterative(A, b, methode):
    
    D, F, E= init_EF(A)

    if methode=="Jacobi":
        M=D
        N=F+E
    elif methode=="Gauss-Seidel":
        M=D+F
        N=E
        
    M_inv=np.linalg.inv(M)
    err=1
    err_seuil=1e-10
    nb_ite= 0
    nb_ite_max= 1000
    x=np.ones(np.shape(A)[1])
    
    while err>err_seuil and nb_ite<nb_ite_max:
        
        # Mise à jour de x
        x_new = M_inv @ (b - N @ x)
        x = x_new
        
        # Calcul de l'erreur
        err = np.linalg.norm(A @ x - b)/ np.linalg.norm(b)
        
        print("Iteration:", nb_ite, "Error:", err)
        if err < err_seuil:
            print("Convergence achieved.")
            break
        if nb_ite >= nb_ite_max:
            print("Maximum iterations reached without convergence.")
            break
    
        nb_ite += 1
    return x

# Example:
if __name__ == "__main__":
    A = np.array([[4, -1, 0, 0],
                  [-1, 4, -1, 0],
                  [0, -1, 4, -1],
                  [0, 0, -1, 3]], dtype=float)
    b = np.array([15, 10, 10, 10], dtype=float)

    x_jacobi = solution_iterative(A, b, "Jacobi")
    print("Solution using Jacobi method:", x_jacobi)

    x_gauss_seidel = solution_iterative(A, b, "Gauss-Seidel")
    print("Solution using Gauss-Seidel method:", x_gauss_seidel)

