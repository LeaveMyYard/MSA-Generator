import settings
import numpy as np

df = settings.task_14_table

df_st = (df - df.mean()) / df.std(ddof=1)

n = len(df)
p = len(df.columns)

R = df.corr().values

print(R)

chi_st = -(n - (2 * p + 5) / 6) * np.log(np.abs(np.linalg.det(R)))

print()
print("chi_st", chi_st)

alpha, L = np.linalg.eig(R)

print()
print("eigenvalues", alpha)
print()
print(L)

A = L.T.dot(np.diag(np.sqrt(alpha)))

print(np.round(A, 2))
