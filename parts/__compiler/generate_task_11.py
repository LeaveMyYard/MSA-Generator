import numpy as np

import settings
from utils import dataframe_to_latex_table

print(
    r"""\section{Завдання 11}
\begin{itemize}
    \item Використовуючи початковi данi завдання 10, провести класифiкацiю об’єктiв
на два класи методом k-середнiх.
\item Провести класифiкацiю об’єктiв методом пошуку згущень.
\item Надати змiстовну iнтерпретацiю результатам.
\end{itemize}
\subsection{Розв'язання}
Поряд з ієрархічними методами існує група ітеративних методів класифікації. Суть їх полягає в тому, що процес класифікації починається з задання деяких початкових умов (кількості утворених класів, поріг завершення процесу класифікації і тому подібне). Більшість цих методів дуже чутлива до зміни і вибору класифікаційних процедур і задання початкових параметрів. Наприклад, вибрана випадково кількість класів може не тільки сильно збільшити трудомісткість процесу класифікації, але і привести до утворення «розмитих» або мало наповнених класів. Тому доцільно спочатку провести класифікацію одним з ієрархічних методів або за допомогою експертних оцінок, а потім вже підбирати початкове розбиття і статистичний критерій для роботи ітераційного алгоритму. Як і в ієрархічній класифікації, в ітераційних методах існує проблема визначення кількості класів. Не всі ітераційні методи вимагають початкового задання кількості класів. Але для остаточного розв’язання питання про структуру сукупності об’єктів можна використати декілька алгоритмів, змінюючи або число утворених класів, або встановлений поріг близькості для об’єднання об’єктів в класи. Тоді виникає можливість вибрати найкраще розбиття за заданим критерієм якості. \\
\subsubsection{Метод k-середніх}
Метод k-середніх належить до групи ітераційних методів еталонного типу, що орієнтовані на використання принципу «найближчого центру». Перерахунок центру класу може здійснюватися в ході ітерації після кожної зміни складу класу або по завершенні ітерацій. \\
\includegraphics[width = 16cm, height = 13cm]{lab10_3.PNG} \\ \\
Розглянемо 10 об’єктів, які необхідно розбити на два класи за допомогою методу k-середніх. Кожен з об’єктів описується чотирма змінними $x_1, x_2, x_3, x_4.$"""
)

X = settings.task_10_classification_rows
Y = np.array([v - 1 for v in settings.task_10_classification_countries])

df = settings.task_10_table_raw
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
iteration_n = 1
while 1:
    print("Iteration: ", iteration_n)
    iteration_n += 1
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
        print(i, ":", s1, s2)
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
