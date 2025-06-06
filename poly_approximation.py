import numpy as np
import matplotlib.pyplot as plt
from cmath import cos

def poly_interpolation(X,Y):
    
    n = len(X)
    P = np.poly1d([0])
    
    for i in range(n):
        L = np.poly1d([1])
        for j in range(n):
            if i!=j:
                L *=  np.poly1d([1,-X[j]])/ (X[i] - X[j])
        P += Y[i] * L
    
    return P

def chebyshev_points(a, b, n):
    return np.array([0.5* (a + b) + 0.5 * (b - a) * np.cos((2 * k + 1) * np.pi / (2 * n)) for k in range(n)])

def plot_polynomial(function, lim_inf, lim_sup, num_points, chebyshev):
    
    if chebyshev:
        x_vals = chebyshev_points(lim_inf, lim_sup, num_points)
    else: 
        x_vals = np.linspace(lim_inf, lim_sup, num_points)
    
    y_cos = np.array([function(x) for x in x_vals])
    polynomial = poly_interpolation(x_vals, y_cos)
    y_poly = polynomial(x_vals)
    print(polynomial)
    
    x_smooth = np.linspace(-1, 1, 500)  # 500 points pour une courbe lisse
    y_real = np.array([function(x) for x in x_smooth])
    
    # Plotting the polynomial
    plt.figure(figsize=(10, 6))
    plt.plot(x_vals, y_poly, label='Interpolating Polynomial', color='black')
    plt.plot(x_smooth, y_real, label='cos(x)', color='red', linestyle='--')
    plt.show()
 
# Example usage:
if __name__ == "__main__":
    def f(x):
        return 1/(1+(10 * x*x))
    plot_polynomial(f, -1, 1, 30, False) # Change to True for Chebyshev points
    
    