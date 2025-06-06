import numpy as np

def calcul_lambda(t, R):
    Y = np.log(R)
    mean_t = np.mean(t)
    mean_Y = np.mean(Y)
    b = np.sum((t - mean_t) * (Y - mean_Y)) / np.sum((t - mean_t) ** 2)
    a = mean_Y - b * mean_t
    return -b

def calcul_coeffs(t, h):
    a = np.column_stack((np.ones_like(t), np.sin(2*np.pi*t/12), np.cos(2*np.pi*t/12)))
    coeffs, _, _, _ = np.linalg.lstsq(a, h, rcond=None)
    return coeffs
    
# Example usage:
if __name__ == "__main__":
    t = np.array([1000, 2000, 3000, 4000, 5000])
    R = np.array([13.5, 12, 10.8, 9.9, 8.9])
    
    lambda_value = calcul_lambda(t, R)
    print("Calculated lambda:", lambda_value)
    
    t = np.array([0, 2, 4, 6, 8, 10])
    h = np.array([1, 1.6, 1.4, 0.6, 0.2, 0.8])
    
    coeffs = calcul_coeffs(t, h)
    print("Calculated coefficients:", coeffs)