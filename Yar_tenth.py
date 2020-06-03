import pandas as pd
import numpy as np
from scipy.stats import t as Student
from scipy.stats import norm
from scipy.stats import f as fisher
from scipy.stats import chi2

df = pd.read_csv("C:\\Users\\Kostya\\Desktop\\Table_2.csv")

X = ["X1", "X6", "X8", "X9"]
Y = np.array(range(30, 40))

df = df.loc[Y]
df = df[X]
n = len(df)

std = df.std(ddof=1)

df_st = (df - df.mean()) / std

D = np.zeros((len(Y), len(Y)))
for i in range(len(Y)):
    for j in range(len(Y)):
        D[i][j] = np.sqrt(((df_st.loc[Y[i]] - df_st.loc[Y[j]]) ** 2).sum())

D = np.round(D, 2)
print(D)
a = []
used = []
for i in range(10):
    b = [i]
    a.append(b)
    used.append(True)

DD = D

for i in range(n, 2, -1):
    in1 = 0
    in2 = 0
    m = 1e9
    for j in range(i):
        for k in range(j + 1, i):
            if DD[j][k] < m:
                m = DD[j][k]
                in1 = j
                in2 = k
    if in1 > in2:
        t = in1
        in1 = in2
        in2 = t

    right_in1 = 0
    right_in2 = 0
    t = -1
    for j in range(n):
        if used[j]:
            t += 1
        if t == in1:
            right_in1 = j
            break
    t = -1
    for j in range(n):
        if used[j]:
            t += 1
        if t == in2:
            right_in2 = j
            break
    print(right_in1, right_in2)
    in1 = right_in1
    in2 = right_in2
    # print(m)
    used[in2] = False
    for j in range(len(a[in2])):
        a[in1].append(a[in2][j])
    D1 = []
    for j in range(n):
        d = []
        if used[j] == False:
            continue
        for k in range(n):
            if used[k] and used[j]:
                mi = 1e9
                for j1 in range(len(a[j])):
                    for k1 in range(len(a[k])):
                        mi = min(
                            mi,
                            np.sqrt(
                                (
                                    (df_st.loc[Y[a[j][j1]]] - df_st.loc[Y[a[k][k1]]])
                                    ** 2
                                ).sum()
                            ),
                        )
                d.append(mi)
        D1.append(d)
        np.array(D1)
    DD = D1
    print(np.round(D1, 2))
    vv = []
    for j in range(n):
        if used[j]:
            vv.append(a[j])
    # print(vv)
cl = {}
cl[-1] = np.array(range(n))
while len(cl) != n:
    m = 0
    in1 = 0
    in2 = 0
    keyy = 0
    ee = []
    for key, e in cl.items():
        if len(e) == 1:
            continue
        for j in range(len(e)):
            for k in range(len(e)):
                if D[e[j]][e[k]] > m:
                    m = D[e[j]][e[k]]
                    in1 = e[j]
                    in2 = e[k]
                    keyy = key
                    ee = e
    # print(m)
    del cl[keyy]
    cl[in1] = [in1]
    cl[in2] = [in2]
    for j in range(len(ee)):
        if ee[j] != in1 and ee[j] != in2:
            if D[in1][j] < D[in2][j]:
                cl[in1].append(ee[j])
            else:
                cl[in2].append(ee[j])
    # print(cl)

