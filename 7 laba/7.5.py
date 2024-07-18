import numpy as np
import scipy.linalg


def log(X, m, C):
    D = X.shape[1]
    diff = X - m
    norm_coef = -0.5 * (D * np.log(2 * np.pi) + np.log(np.linalg.det(C)))
    log_density = norm_coef - 0.5 * np.sum(np.matmul(diff, np.linalg.solve(C, diff.T).T), axis=1)
    return log_density


N = int(input("Enter quantity: "))
D = int(input("Enter size: "))

X = np.random.rand(N, D)
m = np.random.rand(D)
C = np.random.rand(D, D)

log_density = log(X, m, C)
print("Answer:")
print(log_density)
