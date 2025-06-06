import numpy as np


def methode_puissance_norm2(A,x0,nb_ite_max,err_seuil):
    nb_ite=0
    err=2*err_seuil
    
    x=x0
    z= A@x0
    while err > err_seuil and nb_ite < nb_ite_max :
        x=z/np.linalg.norm(z)

        z=A@x
        beta=x.T@z
        
        err=np.linalg.norm(z-beta*x)
        nb_ite+=1

    return nb_ite, err, beta, x

def methode_puissance_norminf(A,x0,nb_ite_max,err_seuil):
    nb_ite=0
    err=2*err_seuil
    
    x=x0
    z=A@x 
    
    while err > err_seuil and nb_ite < nb_ite_max :       
        j=np.argmax(abs(z))
        x=z/z[j]

        z=A@x
        beta=z[j]
        
        err=np.linalg.norm(z-beta*x)
        nb_ite+=1
        
    return nb_ite, err, beta, x

def methode_puissance_inverse(A,x0,nb_ite_max,err_seuil):
    nb_ite=0
    err=2*err_seuil
    
    x=x0
    z= np.linalg.solve(A, x0)
    while err > err_seuil and nb_ite < nb_ite_max :
        

        z=np.linalg.solve(A, x)
        x=z/np.linalg.norm(z)
        
        beta=x.T@A@x
        
        err=np.linalg.norm(z-beta*x)
        nb_ite+=1

    return nb_ite, err, beta, x

def deflation(A, k):
    n=np.shape(A)[0]
    eigenvalues = []
    eigenvectors = []
    
    for i in range(k):
        x0 = np.ones(n)
        nb_ite_max = 100
        err_seuil = 1e-6
        
        nb_ite, err, beta, x = methode_puissance_norm2(A, x0, nb_ite_max, err_seuil)
        
        eigenvalues.append(beta)
        eigenvectors.append(x)
        
        # Deflation step
        x = x / np.linalg.norm(x)  # Normalize the eigenvector
        A = A - beta * np.outer(x, x)
        
    return eigenvalues, eigenvectors



# Example usage:
if __name__ == "__main__":
    A = np.array([[5, 0, 0], [0, 6, 0],[0, 0, 7]], dtype=float)
    n= np.shape(A)[0]
    x0 = np.ones(n)
    nb_ite_max = 100
    err_seuil = 1e-6
    print(methode_puissance_inverse(A, x0, nb_ite_max, err_seuil))