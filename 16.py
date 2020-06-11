import numpy as np 
X=np.array([[1,4],[1,5], [2,3],[2,5],[3,4],[3,5],[4,5]])
#X=np.array([[1,4],[1,5], [2,5],[3,4],[3,5],[4,4],[4,3]])
from scipy.spatial import distance_matrix
import matplotlib.pyplot as plt

#матрица расстояний (попарных сравнений), а каждый элемент - 
#расстояние между объектом ij

Gamma=distance_matrix(X, X)
print(Gamma)
n = len(Gamma)

#Попарних скалярних добутків

B=np.zeros((n,n))
for i in range(n):
    for j in range(n):
        B[i,j]=1/2*(-Gamma[i,j]**2+1 / n * np.sum(Gamma ** 2, axis=0)[j] + 1 / n * np.sum(Gamma ** 2, axis=1)[i]- 1 / n ** 2 * np.sum(Gamma ** 2))

lambdas,lambdas_v=np.linalg.eig(B)

lambdas_sqrt = np.sqrt(lambdas)
lambdas_matrix = np.diag(lambdas_sqrt)

#Центрированная матрица

X_restored = np.dot(lambdas_v, lambdas_matrix)

x = X_restored[:, 0]
y = X_restored[:, 1]
plt.scatter(x, y)
plt.show()