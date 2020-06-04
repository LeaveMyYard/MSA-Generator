from data.table_a4_v2 import table
import pandas as pd
import numpy as np
import scipy.linalg as spla
import settings

matrix_to_string = (
    lambda R: "\\begin{pmatrix}\n"
    + (" \\\\ \n".join([" & ".join([str(round(val, 3)) for val in row]) for row in R]))
    + "\\end{pmatrix}"
)

print(
    r"""\newpage
\section{Завдання 4}
Розглядаються наступні соціально-економічні показники 52 країн світу:
\begin{enumerate}
    \item Чисельність населення (тис. чол.)
    \item Народжуваність (на 1000 чол.)
    \item Смертність (на 1000 чол.)
    \item Смертність серед малюків (на 1000 чол.)
    \item Середнє число дітей у родині
    \item ВВП на душу населення (у дол. США за купівельною спроможністю валют)
    \item Густина населення (кількість чол. на кв. км)
    \item Відсоток міського населення
    \item Відсоток грамотних
    \item Приріст населення (\% на рік)
    \item Тривалість життя чоловіків (у роках)
    \item Тривалість життя жінок (у роках)
\end{enumerate}"""
)

print(
    f"Для мого варіанту \\mbox{{\\boldmath$Y_{{1}}={settings.task_3_y1}, Y_{{2}}={settings.task_3_y2}$,\\;\\;$X_{{1}}={settings.task_2_x1}$,\\;\\;$X_{{2}}={settings.task_2_x2}$,\\;\\;$X_{{3}}={settings.task_2_x3}$,\\;\\;$X_{{4}}={settings.task_2_x4}.$}}"
)

print(
    r"""\begin{enumerate} 
    \item Розрахувати канонічні коефіцієнти кореляції $r_1,r_2$ та відповідні їм
канонічні змінні $U_1,U_2,V_1,V_2$.
    \item За результатами попереднього аналізу виключити з розгляду одну з незалежних змінних та повторити розрахунки п.1. Порівняти значення максимальних коефіцієнтів канонічних кореляцій та перевірити, чи значимо вони відрізняються один від одного (t-тест).
   \item Сформулювати змістовні висновки за отриманими результатами.
\end{enumerate}
\newpage
\subsection{Метод канонічних кореляцій}
Канонічна кореляція – це розповсюдження парної кореляції на випадок, коли існує декілька результативних показників Y і декілька факторів X . При цьому не вимагається відсутність кореляції як в групі результативних показників, так і в групі факторних. Алгоритм розрахунків методу канонічних кореляцій будується таким чином, що початкові змінні замінюються їх лінійними незалежними комбінаціями.\\
Основна мета застосування цього методу полягає в пошуку максимальних кореляційних зв’язків між групами змінних. Крім того, метод канонічних кореляцій дає можливість скоротити об’єм початкових даних за рахунок відсіву
маловпливових чинників. \\
\includegraphics[width = 15cm, height = 15cm]{8.PNG} \\
\includegraphics[width = 16cm, height = 10cm]{9.PNG} \\
\includegraphics[width = 15cm, height = 15cm]{10.PNG} \\
Отже, алгоритм розв’язування задачі такий: побудувавши матрицю $R_{22}^{-1}R_{21}R_{11}^{-1}R_{12},$ знаходимо її власні числа і власні вектори. Проранжуємо власні числа $\lambda^2$ так, щоб $\lambda_1^2 \geq \lambda_2^2 \geq \dots \geq \lambda_p^2.$ Тоді $\lambda_1^2$ буде відповідати максимальний канонічний коефіцієнт кореляції. При визначенні вектора A і канонічних коефіцієнтів кореляції знак при $\lambda$ вибирається виходячи з економічного змісту множин X і Y. 
\subsection{Оцінка значущості канонічних кореляцій}
\includegraphics[width = 16cm, height = 14cm]{11.PNG} \\
\subsection{Скорочення кiлькостi початкових змiнни}
\includegraphics[width = 15cm, height = 15cm]{12.PNG} \\ \\
\textbf{1.} Спочатку запишемо матрицю парних коефіцієнтів кореляції: \\"""
)

lab_4_data = table

x2 = lab_4_data.iloc[:, 0]
# print(x2)

n = lab_4_data.iloc[:, 0].size
overlinex_i = [
    lab_4_data.iloc[:, 0].sum() / n,
    lab_4_data.iloc[:, 1].sum() / n,
    lab_4_data.iloc[:, 2].sum() / n,
    lab_4_data.iloc[:, 3].sum() / n,
]
overliney_i = [lab_4_data.iloc[:, 4].sum() / n, lab_4_data.iloc[:, 5].sum() / n]
sigma_x = [0, 0, 0, 0]
sigma_y = [0, 0]
for i in range(n):
    sigma_x[0] += (lab_4_data.iloc[i, 0] ** 2 - overlinex_i[0]) ** 2
    sigma_x[1] += (lab_4_data.iloc[i, 1] ** 2 - overlinex_i[1]) ** 2
    sigma_x[2] += (lab_4_data.iloc[i, 2] ** 2 - overlinex_i[2]) ** 2
    sigma_x[3] += (lab_4_data.iloc[i, 3] ** 2 - overlinex_i[3]) ** 2
    sigma_y[0] += (lab_4_data.iloc[i, 4] ** 2 - overliney_i[0]) ** 2
    sigma_y[1] += (lab_4_data.iloc[i, 5] ** 2 - overliney_i[1]) ** 2
for k in range(len(sigma_x)):
    sigma_x[k] = np.sqrt(sigma_x[k] / (n - 1))
for k in range(len(sigma_y)):
    sigma_y[k] = np.sqrt(sigma_y[k] / (n - 1))
Z_standart = np.zeros((52, 6))
for i in range(n):
    Z_standart[i, 0] = (lab_4_data.iloc[i, 0] - overlinex_i[0]) / sigma_x[0]
    Z_standart[i, 1] = (lab_4_data.iloc[i, 1] - overlinex_i[1]) / sigma_x[1]
    Z_standart[i, 2] = (lab_4_data.iloc[i, 2] - overlinex_i[2]) / sigma_x[2]
    Z_standart[i, 3] = (lab_4_data.iloc[i, 3] - overlinex_i[3]) / sigma_x[3]
    Z_standart[i, 4] = (lab_4_data.iloc[i, 4] - overliney_i[0]) / sigma_y[0]
    Z_standart[i, 5] = (lab_4_data.iloc[i, 5] - overliney_i[1]) / sigma_y[1]
Standart = pd.DataFrame(
    {
        "X1": Z_standart[:, 0],
        "X2": Z_standart[:, 1],
        "X3": Z_standart[:, 2],
        "X4": Z_standart[:, 3],
        "Y1": Z_standart[:, 4],
        "Y2": Z_standart[:, 5],
    }
)

# print(Standart)

R = Standart.corr()
print("$$" + matrix_to_string(np.array(R)) + "$$")

print(r"Матриці $R_{11}^{-1}, R_{22}^{-1}, R_{12}$ відповідно дорівнюють:")

R11 = R.iloc[0:4, 0:4]
R12 = R.iloc[0:4, 4:6]
R21 = R.iloc[4:6, 0:4]
R22 = R.iloc[4:6, 4:6]

print(r"$$R_{22}^{-1} = " + matrix_to_string(spla.inv(R11)) + "$$")
print(r"$$R_{22}^{-1} = " + matrix_to_string(spla.inv(R22)) + "$$")
print(r"$$R_{12}^{-1} = " + matrix_to_string(np.array(R12)) + "$$")

print("Розрахуємо власнi числа i вектори матрицi: ")

C = spla.inv(R22).dot(R21.dot(spla.inv(R11).dot(R12)))

print(r"$$ C = R_{22}^{-1}R_{21}R_{11}^{-1}R_{12} = " + matrix_to_string(C) + "$$")

[lambda1_2, lambda2_2], [B1, B2] = np.linalg.eig(C)

print(
    f"Отримаємо: $$\\lambda_1^{{2}}={round(lambda1_2, 3)}, \\; \\; B_1 = ({round(B1[0], 3)}, {round(B1[1], 3)})^{{T}}, \\; \\; \\lambda_2^{{2}} = {round(lambda2_2, 3)}, \\; \\; B_2 = ({round(B2[0], 3)}, {round(B2[1], 3)})^{{T}}$$"
)

r1 = np.sqrt(lambda1_2)
r2 = np.sqrt(lambda2_2)
print(
    f"Тодi канонiчнi коефiцiєнти кореляцiї дорiвнюють: $$r_1 =\\sqrt{{\\lambda_1^2}} = \\sqrt{{{round(lambda1_2, 3)}}} = {round(r1, 3)}, \\; \\; r_2 =\\sqrt{{\\lambda_2^2}} = \\sqrt{{{round(lambda2_2, 3)}}} =  {round(r2, 3)}$$ "
)

print(r"Далi знаходимо компоненти векторiв $A_1$ i $A_2$: \\")

A1 = (1 / r1) * spla.inv(R11).dot(R12.dot(B1))
A2 = (1 / r2) * spla.inv(R11).dot(R12.dot(B2))

print(
    r"$$ A_1 = \frac{1}{\lambda_1}R_{11}^{-1}R_{12}B_{1} ="
    + matrix_to_string(A1.reshape(4, 1))
    + "$$"
)
print(
    r"$$ A_2 = \frac{1}{\lambda_2}R_{11}^{-1}R_{12}B_{2} ="
    + matrix_to_string(A2.reshape(4, 1))
    + "$$"
)

print(r"Отже, максимальний коефiцiєнт канонiчної кореляцiї дорiвнює ")
if r2 > r1:
    print(f"$r_2={round(r2, 3)}$")
else:
    print(f"$r_1={round(r1, 3)}$")

print("Йому вiдповiдають канонiчнi змiннi:")

if r2 > r1:
    print(
        f"$$U_2 = {round(A2[0], 3)}x_1 {'+' if A2[1] >= 0 else ''} {round(A2[1], 3)}x_2 {'+' if A2[2] >= 0 else ''} {round(A2[2], 3)}x_3 {'+' if A2[3] >= 0 else ''} {round(A2[3], 3)}x_4, \; \; \; V_2 = {round(B2[0], 3)}y_1 {'+' if B2[1] >= 0 else ''} {round(B2[1], 3)}y_2.$$"
    )
else:
    print(
        f"$$U_1 = {round(A1[0], 3)}x_1 {'+' if A1[1] >= 0 else ''} {round(A1[1], 3)}x_2 {'+' if A1[2] >= 0 else ''} {round(A1[2], 3)}x_3 {'+' if A1[3] >= 0 else ''} {round(A1[3], 3)}x_4, \; \; \; V_2 = {round(B1[0], 3)}y_1 {'+' if B1[1] >= 0 else ''} {round(B1[1], 3)}y_2.$$"
    )

print(
    r"Іншому коефiцiєнтовi канонiчної кореляцiї "
    + f"$r_{1 if r2 > r1 else 2} = {round(r1 if r2 > r1 else r2, 3)}$"
    + r" вiдповiдає така пара канонiчних змiнних:"
)
if r2 < r1:
    print(
        f"$$U_2 = {round(A2[0], 3)}x_1 {'+' if A2[1] >= 0 else ''} {round(A2[1], 3)}x_2 {'+' if A2[2] >= 0 else ''} {round(A2[2], 3)}x_3 {'+' if A2[3] >= 0 else ''} {round(A2[3], 3)}x_4, \; \; \; V_2 = {round(B2[0], 3)}y_1 {'+' if B2[1] >= 0 else ''} {round(B2[1], 3)}y_2.$$"
    )
else:
    print(
        f"$$U_1 = {round(A1[0], 3)}x_1 {'+' if A1[1] >= 0 else ''} {round(A1[1], 3)}x_2 {'+' if A1[2] >= 0 else ''} {round(A1[2], 3)}x_3 {'+' if A1[3] >= 0 else ''} {round(A1[3], 3)}x_4, \; \; \; V_2 = {round(B1[0], 3)}y_1 {'+' if B1[1] >= 0 else ''} {round(B1[1], 3)}y_2.$$"
    )

print(
    r"Зазначимо, що в записах $U_1,V_1,U_2,V_2$ змінні $x_1, x_2, x_3, x_4, y_1, y_2$– це стандартизовані початкові змінні. \\\\"
)

n = 52
m = 1
p = 2
q = 4

chi_ct_2_forboth = -(n - m - 0.5 * (q + p + 1)) * (
    np.log((1 - r1 ** 2) * (1 - r2 ** 2))
)
chi_ct_2_onlyfor_r2 = -(n - m - 0.5 * (q + p + 1) + r1 ** 2) * (np.log((1 - r2 ** 2)))

print(
    r"""\textbf{2.} Для перевiрки значущостi коефiцiєнтiв канонiчної кореляцiї скористаємося критерiєм Бартлетта. Сформулюємо гiпотези: $$H_A^1: r_1 \neq 0, H_0^1: r_1 = r_2 = 0.$$
Тодi: $$\chi_{CT}^2= -[52 - 1 - 0.5(4+2+1)]ln[(1-r_1^2)(1 - r_2^2)] = """
    + str(round(chi_ct_2_forboth, 3))
    + r"$$"
)

print(r"$$\chi_{KP}^2=\chi^2(\alpha;(q-m-1)\times(p-m-1)) = (0.2; 8) = 11.0301.$$")

print(
    r"""Так як $\chi_{CT}^2 > \chi_{KP}^2$, то з ймовірністю $80\%$ $r_1$ значимо відрізняється від
нуля. 
Перевiримо значущiсть другого коефiцiєнта канонiчної кореляцiї $r_2$"""
)

print(
    r"""Маємо такi гiпотези: $$H_A^2: r_2 \neq 0, \; H_0^2: r_2 = 0.$$
Далi, $$\chi_{CT}^2= -[52 - 1 - 0.5(4+2+1)+ r_1^2]ln(1-r_2^2) = """
    + f"{round(chi_ct_2_onlyfor_r2, 3)}"
    + r"""$$
$$\chi_{KP}^2=\chi^2(\alpha;(q-m-1)\times(p-m-1)) = (0.2; 3) = 4.642.$$"""
)

print(
    r"""Отримали $\chi_{CT}^2 > \chi_{KP}^2,$ а це означає, що $r_2$ значимо вiдрiзняється вiд нуля з ймовiрнiстю $80\%$. 
\subsection{Iнтерпретацiя результатiв канонiчного аналiз}
Отже, отримані такі значимі пари канонiчних змiнних i вiдповiдні їм коефiцiєнти кореляцiї:"""
)
print(
    f"$$U_1 = {round(A1[0], 3)}x_1 {'+' if A1[1] >= 0 else ''} {round(A1[1], 3)}x_2 {'+' if A1[2] >= 0 else ''} {round(A1[2], 3)}x_3 {'+' if A1[3] >= 0 else ''} {round(A1[3], 3)}x_4, \; \; \; V_2 = {round(B1[0], 3)}y_1 {'+' if B1[1] >= 0 else ''} {round(B1[1], 3)}y_2, r_1={round(r1, 3)}$$"
)
print(
    f"$$U_2 = {round(A2[0], 3)}x_1 {'+' if A2[1] >= 0 else ''} {round(A2[1], 3)}x_2 {'+' if A2[2] >= 0 else ''} {round(A2[2], 3)}x_3 {'+' if A2[3] >= 0 else ''} {round(A2[3], 3)}x_4, \; \; \; V_2 = {round(B2[0], 3)}y_1 {'+' if B2[1] >= 0 else ''} {round(B2[1], 3)}y_2, r_2={round(r2, 3)}$$"
)

removed_index = min(enumerate(np.abs(A1)), key=lambda x: x[1])[0]

print(
    r""" НЕ ГЕНЕРИРУЕТСЯ! Величини коефiцiєнтів канонiчної кореляцiї $r_1 = 0.21$, $r_2 = 0.918$ означають, що на тривалість життя чоловіків (у роках) i тривалість життя жінок (у роках) суттєво впливають наступні чинники: $x_1$ - народжуваність (на 1000 чол.), $x_2$ - середнє число дітей у родині, $x_3$ - густина населення (кількість чол. на кв. км) та $x_4$ - відсоток міського населення.
Для $r_1$ коефiцiєнт при $x_2$ найбiльший за модулем, тому чинник $x_2$ є найбiльш впливовим в цій лiнiйнiй комбiнацiї, для $r_2$ коефiцiєнт при $x_1$ найбiльший за модулем, тому чинник $x_1$ є найбiльш впливовим в цій лiнiйнiй комбiнацiї. А коефiцiєнт при $x_3$ малий і для $r_1$, і для $r_2$, тому чинник $x_3$ видалимо з розгляду i повторимо всi розрахунки."""
)

print(f"Найменьший коефіцієнт - $x_{removed_index + 1}$")

print(r"Спочатку запишемо матрицю парних коефіцієнтів кореляції:")

R = Standart.loc[:, Standart.columns != f"X{removed_index + 1}"].corr()
print("$$" + matrix_to_string(np.array(R)) + "$$")

print(r"Матриці $R_{11}^{-1}$, $R_{22}^{-1}$, $R_{12}$ відповідно дорівнюють:")

R11 = R.iloc[0:3, 0:3]
R12 = R.iloc[0:3, 3:5]
R21 = R.iloc[3:5, 0:3]
R22 = R.iloc[3:5, 3:5]

print(r"$$R_{22}^{-1} = " + matrix_to_string(spla.inv(R11)) + "$$")
print(r"$$R_{22}^{-1} = " + matrix_to_string(spla.inv(R22)) + "$$")
print(r"$$R_{12}^{-1} = " + matrix_to_string(np.array(R12)) + "$$")

print("Розрахуємо власнi числа i вектори матрицi: ")

C = spla.inv(R22).dot(R21.dot(spla.inv(R11).dot(R12)))

print(r"$$ C = R_{22}^{-1}R_{21}R_{11}^{-1}R_{12} = " + matrix_to_string(C) + "$$")

[lambda1_2, lambda2_2], [B1, B2] = np.linalg.eig(C)

print(
    f"Отримаємо: $$\\lambda_1^{{2}}={round(lambda1_2, 3)}, \\; \\; B_1 = ({round(B1[0], 3)}, {round(B1[1], 3)})^{{T}}, \\; \\; \\lambda_2^{{2}} = {round(lambda2_2, 3)}, \\; \\; B_2 = ({round(B2[0], 3)}, {round(B2[1], 3)})^{{T}}$$"
)

r1 = np.sqrt(lambda1_2)
r2 = np.sqrt(lambda2_2)
print(
    f"Тодi канонiчнi коефiцiєнти кореляцiї дорiвнюють: $$r_1 =\\sqrt{{\\lambda_1^2}} = \\sqrt{{{round(lambda1_2, 3)}}} = {round(r1, 3)}, \\; \\; r_2 =\\sqrt{{\\lambda_2^2}} = \\sqrt{{{round(lambda2_2, 3)}}} =  {round(r2, 3)}$$ "
)

print(r"Далi знаходимо компоненти векторiв $A_1$ i $A_2$: \\")

A1 = (1 / r1) * spla.inv(R11).dot(R12.dot(B1))
A2 = (1 / r2) * spla.inv(R11).dot(R12.dot(B2))

print(
    r"$$ A_1 = \frac{1}{\lambda_1}R_{11}^{-1}R_{12}B_{1} ="
    + matrix_to_string(A1.reshape(3, 1))
    + "$$"
)
print(
    r"$$ A_2 = \frac{1}{\lambda_2}R_{11}^{-1}R_{12}B_{2} ="
    + matrix_to_string(A2.reshape(3, 1))
    + "$$"
)

print(r"Отже, максимальний коефiцiєнт канонiчної кореляцiї дорiвнює ")
if r2 > r1:
    print(f"$r_2={round(r2, 3)}$")
else:
    print(f"$r_1={round(r1, 3)}$")

print("Йому вiдповiдають канонiчнi змiннi:")

if r2 > r1:
    print(
        f"$$U_2 = {round(A2[0], 3)}x_1 {'+' if A2[1] >= 0 else ''} {round(A2[1], 3)}x_2 {'+' if A2[2] >= 0 else ''} {round(A2[2], 3)}x_3, \; \; \; V_2 = {round(B2[0], 3)}y_1 {'+' if B2[1] >= 0 else ''} {round(B2[1], 3)}y_2.$$"
    )
else:
    print(
        f"$$U_1 = {round(A1[0], 3)}x_1 {'+' if A1[1] >= 0 else ''} {round(A1[1], 3)}x_2 {'+' if A1[2] >= 0 else ''} {round(A1[2], 3)}x_3, \; \; \; V_2 = {round(B1[0], 3)}y_1 {'+' if B1[1] >= 0 else ''} {round(B1[1], 3)}y_2.$$"
    )

print(
    r"Іншому коефiцiєнтовi канонiчної кореляцiї "
    + f"$r_{1 if r2 > r1 else 2} = {round(r1 if r2 > r1 else r2, 3)}$"
    + r" вiдповiдає така пара канонiчних змiнних:"
)
if r2 < r1:
    print(
        f"$$U_2 = {round(A2[0], 3)}x_1 {'+' if A2[1] >= 0 else ''} {round(A2[1], 3)}x_2 {'+' if A2[2] >= 0 else ''} {round(A2[2], 3)}x_3, \; \; \; V_2 = {round(B2[0], 3)}y_1 {'+' if B2[1] >= 0 else ''} {round(B2[1], 3)}y_2.$$"
    )
else:
    print(
        f"$$U_1 = {round(A1[0], 3)}x_1 {'+' if A1[1] >= 0 else ''} {round(A1[1], 3)}x_2 {'+' if A1[2] >= 0 else ''} {round(A1[2], 3)}x_3, \; \; \; V_2 = {round(B1[0], 3)}y_1 {'+' if B1[1] >= 0 else ''} {round(B1[1], 3)}y_2.$$"
    )

print(
    r"Зазначимо, що в записах $U_1,V_1,U_2,V_2$ змінні $x_1, x_2, x_3, y_1, y_2$– це стандартизовані початкові змінні. \\\\"
)

n = 52
m = 1
p = 2
q = 4

chi_ct_2_forboth = -(n - m - 0.5 * (q + p + 1)) * (
    np.log((1 - r1 ** 2) * (1 - r2 ** 2))
)
chi_ct_2_onlyfor_r2 = -(n - m - 0.5 * (q + p + 1) + r1 ** 2) * (np.log((1 - r2 ** 2)))

print(
    r"""\textbf{2.} Для перевiрки значущостi коефiцiєнтiв канонiчної кореляцiї скористаємося критерiєм Бартлетта. Сформулюємо гiпотези: $$H_A^1: r_1 \neq 0, H_0^1: r_1 = r_2 = 0.$$
Тодi: $$\chi_{CT}^2= -[52 - 1 - 0.5(4+2+1)]ln[(1-r_1^2)(1 - r_2^2)] = """
    + str(round(chi_ct_2_forboth, 3))
    + r"$$"
)

print(r"$$\chi_{KP}^2=\chi^2(\alpha;(q-m-1)\times(p-m-1)) = (0.2; 8) = 11.0301.$$")

print(
    r"""Так як $\chi_{CT}^2 > \chi_{KP}^2$, то з ймовірністю $80\%$ $r_1$ значимо відрізняється від
нуля. 
Перевiримо значущiсть другого коефiцiєнта канонiчної кореляцiї $r_2$"""
)

print(
    r"""Маємо такi гiпотези: $$H_A^2: r_2 \neq 0, \; H_0^2: r_2 = 0.$$
Далi, $$\chi_{CT}^2= -[52 - 1 - 0.5(4+2+1)+ r_1^2]ln(1-r_2^2) = """
    + f"{round(chi_ct_2_onlyfor_r2, 3)}"
    + r"""$$
$$\chi_{KP}^2=\chi^2(\alpha;(q-m-1)\times(p-m-1)) = (0.2; 3) = 4.642.$$"""
)

print(
    r"""Отримали $\chi_{CT}^2 > \chi_{KP}^2,$ а це означає, що $r_2$ значимо вiдрiзняється вiд нуля з ймовiрнiстю $80\%$."""
)
print(r"Це означає, що чинник $x_3$ можна не брати до уваги при розрахунках. ")
