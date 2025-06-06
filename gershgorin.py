import matplotlib.pyplot as plt
import numpy as np

def GershgorinCircles(A):
    i, j= 0, 0
    n = A.shape[0]
    circles = []
    for i in range(n):
        center = A[i, i]
        radius_row = sum(abs(A[i, j]) for j in range(n) if i!=j)
        radius_col = sum(abs(A[j, i]) for j in range(n) if i!=j)
        radius = min(radius_row, radius_col)
        circles.append((center, radius))
    return circles

def plot_gershgorin_circles(A):
    circles = GershgorinCircles(A)
    fig, ax = plt.subplots()
    for center, radius in circles:
        circle= plt.Circle((np.real(center),np.imag(center)), radius, color='blue', fill=False, linestyle='dashed')
        ax.add_artist(circle)
        ax.plot(np.real(center), np.imag(center), 'ro')  # Center of the circle
    ax.set_xlim(-10, 10)
    ax.set_ylim(-10, 10)
    plt.xlabel('Real')
    plt.ylabel('Imaginary')
    plt.grid(True)
    plt.show()
    
# Example usage
if __name__ == "__main__":
    A = np.array([[3+1j, -1.5, 0, 1.5j],
                  [0.5, 4, 1j, 0.5j],
                  [np.sqrt(2), np.sqrt(2)*1j, 2+3j, 0],
                  [1j, 1, 1j, 4j]], dtype=complex)
    
    lamda = np.linalg.eig(A)
    print("Eigenvalues of A:")
    print(lamda[0])
    
    plot_gershgorin_circles(A)
    

    
        