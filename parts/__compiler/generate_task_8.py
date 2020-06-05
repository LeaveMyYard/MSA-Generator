import settings
import pandas as pd
import numpy as np
from settings import table_for_task_8 as table
from utils import dataframe_to_latex_table

print(
    r"""\newpage
\section{Завдання 8}
1. Розрахувати характеристику $\chi^2$ квадратичної спряженості ознак, коефіцієнт Крамера та інформаційну характеристику $Y^2$. Перевірити їх значущість, сформулювати висновки.\\
2. Розрахувати коефіцієнти Пірсона і Чупрова, зробити висновки. \\"""
)

df = table.copy()
df["$n_{i \\bullet}$"] = n_ip = [sum(row) for name, row in df.iterrows()]
df = df.transpose()
df["$n_{\\bullet i}$"] = n_pj = [sum(row) for name, row in df.iterrows()]
df = df.transpose()

n = n_pj[-1]
n_pj = n_pj[:-1]

print(
    dataframe_to_latex_table(
        df, caption="Розподiл женихiв та наречених за вiковими категорiями"
    )
)

print(
    r"""\subsection{Характеристика $\chi^2$ квадратичної спряженостi ознак $x_1$, $x_2$}
\includegraphics[width = 16cm, height = 16cm]{22.PNG} \\
\subsection{Iнформацiйна характеристика ступеня тiсноти статистичного зв’язку $Y^2$}
\includegraphics[width = 16cm, height = 6cm]{23.PNG} \\ \\
Розрахуємо характеристику $\chi^2,$ для цього спочатку розрахуємо величини: \\"""
)

m1 = m2 = 5

phi_2 = sum(
    [
        sum([table.values[i, j] ** 2 / (n_ip[i] * n_pj[j]) for j in range(m2)])
        for i in range(m1)
    ]
)

print(
    r"$$1 + \phi^2 = \sum_{i=1}^{m_1}\sum_{j=1}^{m_2}\displaystyle \frac{n_{ij}^2}{n_{i\bullet}n_{\bullet j}} = "
    + f"{round(phi_2, 4)}$$"
)

chi2_st = n * (phi_2 - 1)
chi2_kr = 26.296

print(
    f"Тодi $\\phi^2 = {round(phi_2, 4)} - 1 = {round(phi_2, 4) - 1}$ i $\\chi^2_{{CT}} = n\\phi^2 = {round(chi2_st, 3)}$\\"
)

phi_2 -= 1

if chi2_st > chi2_kr:
    print(
        r"""Розглянемо питання про значущiсть розрахованих коефiцiєнтiв. Так як:\\ 
    $$\chi^2_{CT} > \chi_{KP}^2(0.05;16) = 26.296,$$ то коефiцiєнт $\chi^2_{CT}$ значимо вiдрiзняється вiд нуля з ймовiрнiстю 95\%. \\"""
    )
else:
    print(
        r"""Розглянемо питання про значущiсть розрахованих коефiцiєнтiв. Так як:\\ 
    $$\chi^2_{CT} < \chi_{KP}^2(0.05;16) = 26.296,$$ то коефiцiєнт $\chi^2_{CT}$ не значимо вiдрiзняється вiд нуля з ймовiрнiстю 95\%. \\"""
    )

print(
    r"""Незручнiсть використання характеристики $\chi^2$ пов’язана з тим, що її верхня межа прямує до нескiнченностi при збiльшеннi об’єму вибiрки n. Тому замiсть $\chi^2$ часто використовують характеристику $C,$ яку називають \textbf{коефiцiєнтом Крамера}. Вона вже знаходиться в дiапазонi $0 \leq  C \leq  1$. При цьому нульове значення C свiдчить про строгу статистичну незалежнiсть ознак, а значення C = 1 — про можливiсть однозначного вiдновлення значення однiєї змiнної по вiдомому значенню iншої.\\ Якщо статистичний зв’язок значущий, то виникає питання про iнтервальнi оцiнки характеристик цього зв’язку. Тому розрахуємо коефіцієнт Крамера:"""
)

C = np.sqrt(chi2_st / (n * 4))

print(
    f"$$\\displaystyle C = \\displaystyle \\sqrt{{\\frac{{\\chi^2_{{CT}}}}{{n\\cdot min[m_1 - 1, m_2 - 1]}}}}= \\sqrt{{\\displaystyle \\frac{{{chi2_st}}}{{{n * 4}}}}} = {round(C, 4)}.$"
)

print(
    r"""Так як статистичний зв’язок значущий, то виникає питання про iнтервальнi оцiнки характеристик цього зв’язку.\\
За наближенi iнтервали довiри для iстинних значень коефiцiєнта квадратичної спряженостi i коефiцiєнта Крамера можна прийняти такi iнтервали (при довiрчiй ймовiрностi $1 - 2\alpha$).\\
Визначимо iнтервал довiри для $\chi^2_{CT}$, скориставшись грубою оцiнкою $\displaystyle \sigma_{\chi^2}^2 = 4\chi^2_{CT}:$ \\"""
)

nm_chi = chi2_st - 1.64 * np.sqrt(4 * chi2_st)
bm_chi = chi2_st + 1.64 * np.sqrt(4 * chi2_st)

print(
    f"H.M.: $\\chi^2_{{CT}} - u_{{1 - 0.05}}\\sqrt{{4\\chi^2_{{CT}}}} = {round(chi2_st, 4)} - 1.64\\sqrt{{4\\cdot{round(chi2_st, 4)}}} = {round(nm_chi, 3)}$\\"
)
print(
    f"В.M.: $\\chi^2_{{CT}} + u_{{1 - 0.05}}\\sqrt{{4\\chi^2_{{CT}}}} = {round(chi2_st, 4)} + 1.64\\sqrt{{4\\cdot{round(chi2_st, 4)}}} = {round(bm_chi, 3)}$\\"
)

print(
    f"Отже, з ймовiрнiстю 95\\% iстинне значення показника $\\chi^2$ буде знаходитися в промiжку $[{round(nm_chi, 3)}; {round(bm_chi, 3)}]$.\\\\ \\\\"
)

nm_c = C - 1.64 * np.sqrt(1 / (n * 4))
bm_c = C + 1.64 * np.sqrt(1 / (n * 4))

print(
    f"H.M.: $C - u_{{1 - 0.05}}\\sigma_C = C - u_{{1 - 0.05}}\\cdot \\displaystyle \\sqrt{{\\frac{{1}}{{\\displaystyle n \\cdot min[m_1-1,m_2-1]}}}} = {round(nm_c, 3)}$\\"
)
print(
    f"В.M.: $C + u_{{1 - 0.05}}\\sigma_C = C + u_{{1 - 0.05}}\\cdot \\displaystyle \\sqrt{{\\frac{{1}}{{\\displaystyle n \\cdot min[m_1-1,m_2-1]}}}} = {round(bm_c, 3)}$\\"
)

print(
    f"Отже, з ймовiрнiстю 95\\% iстинне значення показника $C$ буде знаходитися в промiжку $[{round(nm_c, 3)}; {round(bm_c, 3)}]$.\\ "
)

Y2 = 2 * (
    sum(
        [
            table.values[i, j] * np.log(table.values[i, j])
            for i in range(m1)
            for j in range(m2)
        ]
    )
    - sum([n_ip[i] * np.log(n_ip[i]) for i in range(m1)])
    - sum([n_pj[j] * np.log(n_pj[j]) for j in range(m2)])
    + n * np.log(n)
)

print(f"Розрахуємо iнформацiйну характеристику\\\\ $Y^2 = {round(Y2, 3)}$\\")

if Y2 > chi2_kr:
    print(
        r"Так як $Y^2 > \chi_{KP}^2 = \chi^2(0.05;16) = 26.296,$ то з ймовiрнiстю 95\% значення коефiцiєнта $Y^2$ значимо вiдрiзняється вiд нуля. "
    )
else:
    print(
        r"Так як $Y^2 < \chi_{KP}^2 = \chi^2(0.05;16) = 26.296,$ то з ймовiрнiстю 95\% значення коефiцiєнта $Y^2$ не значимо вiдрiзняється вiд нуля. "
    )

print(r"\subsection{ Коефiцiєнти Пiрсона i Чупрова}")
print(r"\includegraphics[width = 16cm, height = 6cm]{24.PNG} \\")
print(
    r"""Коефіцієнти взаємної зв'язаності, наприклад, Чупрова K і Пірсона С застосовуються для визначення тісноти зв’язку у ситуаціях, коли кожна якісна ознака складається більш ніж з двох груп. Коефіцієнт Чупрова К використовується у разі неоднакової кількості рядків і стовпчиків таблиці спряженості (k, Ф k2).\\
Чим ближче величина коефіцієнтів до одиниці, тим тісніше зв'язок.\\
Визначимо коефiцiєнти Пiрсона i Чупрова. Маємо: \\"""
)

Kpirs = np.sqrt(phi_2 / (1 + phi_2))
Kchup = np.sqrt(phi_2 / 16)

print(
    r"$K_{Pirs} = \displaystyle \sqrt{\displaystyle \frac{\phi^2}{1 + \phi^2}} = "
    + f"{round(Kpirs, 3)}$\\"
)
print(
    r"$K_{Chup} = \displaystyle \sqrt{\displaystyle \frac{\phi^2}{(m_1 - 1)(m_2 - 1)}} = "
    + f"{round(Kchup, 3)}$ \\"
)

print(r"Розрахуємо коефiцiєнти $K_{Pirs}, K_{Chup}$ за модифiкованими формулами:\\")

Kpirs2 = np.sqrt(chi2_st / (n + chi2_st))
Kchup2 = np.sqrt(chi2_st / (n * 16))

print(
    r"$K_{Pirs} = \displaystyle \sqrt{\displaystyle \frac{\chi_{CT}^2}{n + \chi_{CT}^2}} = "
    + f"{round(Kpirs2, 3)}$\\"
)
print(
    r"$K_{Chup} = \displaystyle \sqrt{\displaystyle \frac{\chi_{CT}^2}{n(m_1 - 1)(m_2 - 1)}} = "
    + f"{round(Kchup2, 3)}$ \\"
)

print(
    r"Результати розрахункiв за рiзними формулами збiглися. Результат, отриманий за формулою $K_{Chup}$, бiльш точний, тому що враховується кiлькiсть груп у кожнiй ознацi."
)

