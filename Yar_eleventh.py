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

E1 = df_st.loc[Y[0]].values
E2 = df_st.loc[Y[1]].values
w1 = 1
w2 = 1

s1 = set()
s2 = set()
s1_p = set()
s2_p = set()

for i in range(2, 10):
    d1 = np.sqrt(((E1 - df_st.loc[Y[i]].values) ** 2).sum())
    d2 = np.sqrt(((E2 - df_st.loc[Y[i]].values) ** 2).sum())
    if d1 <= d2:
        E1 = (w1 * E1 + df_st.loc[Y[i]].values) / (w1 + 1)
        w1 += 1
        s1.add(i)
    else:
        E2 = (w2 * E2 + df_st.loc[Y[i]].values) / (w2 + 1)
        w2 += 1
        s2.add(i)
t = 0
while 1:
    s1_p = s1.copy()
    s2_p = s2.copy()
    s1.clear()
    s2.clear()
    t += 1
    for i in range(10):
        d1 = np.sqrt(((E1 - df_st.loc[Y[i]].values) ** 2).sum())
        d2 = np.sqrt(((E2 - df_st.loc[Y[i]].values) ** 2).sum())
        if d1 <= d2:
            E1 = (w1 * E1 + df_st.loc[Y[i]].values) / (w1 + 1)
            w1 += 1
            s1.add(i)
        else:
            E2 = (w2 * E2 + df_st.loc[Y[i]].values) / (w2 + 1)
            w2 += 1
            s2.add(i)
    if s1 == s1_p and s2 == s2_p:
        break
ss1 = []
ss2 = []
for i in s1:
    ss1.append(i)
for i in s2:
    ss2.append(i)
c1 = (df_st.loc[Y[ss1]]).sum().values / len(ss1)
c2 = (df_st.loc[Y[ss2]]).sum().values / len(ss2)

c = np.zeros((2, 10))
for i in range(10):
    c[0][i] = np.sqrt(((c1 - df_st.loc[Y[i]].values) ** 2).sum())
    c[1][i] = np.sqrt(((c2 - df_st.loc[Y[i]].values) ** 2).sum())
# print(s1, s2)

R_max = 0
R_min = 1e9
D = np.zeros((len(Y), len(Y)))
for i in range(len(Y)):
    for j in range(len(Y)):
        D[i][j] = np.sqrt(((df_st.loc[Y[i]] - df_st.loc[Y[j]]) ** 2).sum())
        R_max = max(R_max, D[i][j])
        if D[i][j] != 0:
            R_min = min(R_min, D[i][j])
R = 1.2

used = []
for i in range(10):
    used.append(False)
cl = []
start = [-1]
rs_p = set()
rs = set()
while 1:
    rs_p = rs.copy()
    rs.clear()
    if len(start) == 1:
        for i in range(10):
            if used[i] == False:
                start = df_st.loc[Y[i]].values
                break
    if len(start) == 1:
        break
    for i in range(10):
        if used[i] == False:
            if np.sqrt(((start - df_st.loc[Y[i]].values) ** 2).sum()) < R:
                rs.add(i)
    rss = []
    for i in rs:
        rss.append(i)

    if rs == rs_p:
        for i in rss:
            used[i] = True
        start = [-1]
        cl.append(rss)
    else:
        start = (df_st.loc[Y[rss]]).sum().values / len(rss)
    print(cl)
