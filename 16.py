import numpy as np

from scipy.spatial import distance_matrix
import matplotlib.pyplot as plt

X = np.array([[1, 5], [1, 4], [1, 3], [2, 4], [2, 3], [3, 4], [4, 4]])
# X=np.array([[1,4],[1,5], [2,5],[3,4],[3,5],[4,4],[4,3]])

# матрица расстояний (попарных сравнений), а каждый элемент -
# расстояние между объектом ij

Gamma = distance_matrix(X, X)
print(np.round(Gamma, 3))
n = len(Gamma)

# Попарних скалярних добутків

B = np.zeros((n, n))
for i in range(n):
    for j in range(n):
        B[i, j] = (
            1
            / 2
            * (
                -Gamma[i, j] ** 2
                + 1 / n * np.sum(Gamma ** 2, axis=0)[j]
                + 1 / n * np.sum(Gamma ** 2, axis=1)[i]
                - 1 / n ** 2 * np.sum(Gamma ** 2)
            )
        )

lambdas, lambdas_v = np.linalg.eig(B)

lambdas_sqrt = np.sqrt(lambdas)
lambdas_matrix = np.diag(lambdas_sqrt)

# Центрированная матрица

X_restored = lambdas_v @ lambdas_matrix

# print(np.round(X_restored, 2))

x = X_restored[:, 0]
y = X_restored[:, 2]

# print(x)
# print(y)
plt.scatter(x, y)
plt.show()
