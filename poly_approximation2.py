import numpy as np
import matplotlib.pyplot as plt

def poly_horner(X, a, z):
    n = len(a) - 1
    P = a[n]
    for i in range(n - 1, -1, -1):  
        P = P * (z - X[i]) + a[i]
    return P

def diff_divise(X, Y, i, j):
    if i == j:
        return Y[i]
    return (diff_divise(X, Y, i + 1, j) - diff_divise(X, Y, i, j - 1)) / (X[j] - X[i])

def coef_newton(X, Y):
    n = len(X)
    a = np.zeros(n)
    for i in range(n):
        a[i] = diff_divise(X, Y, 0, i)
    return a

# Exemple d'utilisation
if __name__ == "__main__":
    # Points d'interpolation
    X = np.array([-1, 0, 1])
    Y = np.array([1, 2, -1])
    
    # Calcul des coefficients du polynôme de Newton
    a = coef_newton(X, Y)
    print("Coefficients du polynôme de Newton :", a)
    
    # Générer des points pour une courbe lisse
    x_smooth = np.linspace(-2, 2, 100)
    y_poly = poly_horner(X, a, x_smooth)
    
    # Tracé du polynôme
    plt.figure(figsize=(10, 6))
    plt.plot(x_smooth, y_poly, label="Polynôme de Newton", color="blue")
    plt.scatter(X, Y, color="red", label="Points d'interpolation")
    plt.xlabel("x")
    plt.ylabel("y")
    plt.title("Interpolation de Newton")
    plt.legend()
    plt.grid(True)
    plt.show()