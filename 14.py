import settings
import numpy as np

df = settings.task_14_table

df_st = (df - df.mean()) / df.std(ddof=1)

n = len(df)
p = len(df.columns)

R = df.corr().values

print("R")
print(R)

chi_st = -(n - (2 * p + 5) / 6) * np.log(np.abs(np.linalg.det(R)))

print()
print("chi_st", chi_st, ">? 18.307")

alpha, L = np.linalg.eig(R)

print()
print("eigenvalues", alpha)
print()
print("L")
print(L, "\n")

A = L.dot(np.diag(np.sqrt(alpha)))

print("A")
print(np.round(A, 2))

K1 = np.sum(A[1:3, 0] ** 2) / np.sum(A[:, 0] ** 2)
print("K1(x2, x3) =", K1)

K1 = np.sum(A[1:4, 0] ** 2) / np.sum(A[:, 0] ** 2)
print("K1(x2, x3, x4) =", K1)

K2 = np.sum(A[[0], 1] ** 2) / np.sum(A[:, 1] ** 2)
print("K2(x1) =", K2)

K2 = np.sum(A[[4], 1] ** 2) / np.sum(A[:, 1] ** 2)
print("K2(x5) =", K2)

K2 = np.sum(A[[0, 4], 1] ** 2) / np.sum(A[:, 1] ** 2)
print("K2(x1, x5) =", K2)


print()

E = np.cov(df.values.T)

print("E")
print(np.round(E, 3))

w, b = np.linalg.eig(E)

print("Alpha", w)


def chi(r):
    n1 = n - r - (2 * (p - r) + 1 + 2 / (p - r)) / 6
    return n1 * (
        -np.log(np.linalg.det(E))
        + np.prod(w[:r])
        + (p - r) * np.log((np.trace(E) - np.sum(w[:r])) / (p - r))
    )


Z = L.dot(df.values.T)

print(np.round(Z, 2))
