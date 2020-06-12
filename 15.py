import pandas as pd
import numpy as np
import settings

df = settings.task_15_table
df_st = (df - df.mean()) / df.std(ddof=1)

print(df_st)

n = len(df)
m = p = len(df.columns)

XH = df_st.values

R = df.corr().values

print("R")
print(R)

chi_st = -(n - (2 * p + 5) / 6) * np.log(np.abs(np.linalg.det(R)))
print()
print("chi_st", chi_st, ">? 18.307")

R_1 = np.linalg.inv(R)

h2 = 1 - 1 / np.diag(R_1)

print("h2\n", h2)

Rh = R.copy()

np.fill_diagonal(Rh, h2)

print("Rh\n", Rh)

alpha, eigvec = np.linalg.eig(R)
alpha, eigvec = np.array(sorted(zip(alpha, eigvec), key=lambda x: x[0], reverse=True)).T

print("Eigenvalues, Eigenvectors")

eigvec = np.stack(eigvec)

print(alpha)
print(eigvec)

r = 3  # len(list(filter(lambda x: x > 1, alpha)))

print("r =", r)

V = np.array(eigvec[:r])

A = V.T.dot(np.diag(alpha[:r] ** 0.5))

print("A\n", np.round(A.astype(float), 2))

chi_st = (n - (2 * m + 5) / 6 - 2 * r / 3) * np.log(
    np.linalg.det(A.T.dot(A).astype(float)) / np.linalg.det(R)
)

print(chi_st, ">? 11.34")

qval = {}

for i in range(5, 91, 5):
    T12 = np.array(
        [
            [np.cos(np.deg2rad(i)), np.sin(np.deg2rad(i)), 1],
            [-np.sin(np.deg2rad(i)), np.cos(np.deg2rad(i)), 0],
            [0, 0, 1,],
        ]
    )

    T13 = np.array(
        [
            [np.cos(np.deg2rad(i)), 0, np.sin(np.deg2rad(i))],
            [0, 1, 0,],
            [-np.sin(np.deg2rad(i)), 0, np.cos(np.deg2rad(i))],
        ]
    )

    T23 = np.array(
        [
            [1, 0, 0,],
            [0, np.cos(np.deg2rad(i)), np.sin(np.deg2rad(i))],
            [0, -np.sin(np.deg2rad(i)), np.cos(np.deg2rad(i))],
        ]
    )

    T = T12.dot(T13).dot(T23)

    Ah = A.dot(T)

    q = np.sum((np.sum(Ah ** 4, axis=1) - np.sum(Ah ** 2, axis=1) ** 2) / (r ** 2))

    # print(i, q)

    qval[q] = (T, i)

qmax = max(qval.keys())

(T, i) = qval[qmax]

print("max angle", i)
print("T\n", T)

Ah = A.dot(T.T)

print("Ah\n", np.round(Ah.astype(float), 2))

F = A.T.dot(np.linalg.inv(R)).dot(XH.T)

print("F\n", np.round(F.astype(float), 2))
