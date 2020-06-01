#! /usr/bin/env python
# -*- coding: utf-8 -*-

import pandas as pd
import sys

from data.table_a2 import table

import settings

print(
    r"""
\section{Завдання №1}
1. Згрупувати початкові дані за незалежною ознакою. \\
2. Розрахувати коефіцієнт детермінації. \\
3. Розрахувати коефіцієнт Фехнера.\\
4. Сформулювати висновки.
\subsection{Розв'язання}
Розглядаються наступні показники виробничо-господарської діяльності 30 підприємств:
\\
\textbf{Y"""
    + str(settings.task_1_y)
    + r"""} — """
    + str(settings.task_1_y_meaning)
    + r"""\\
\textbf{X"""
    + str(settings.task_1_x)
    + r"""} — """
    + str(settings.task_1_x_meaning)
    + r"""\\ \\
Спочатку згрупуємо початкові дані за незалежною ознакою $X_{"""
    + str(settings.task_1_x)
    + r"""} \;$. \\ Згруповані дані представимо у вигляді таблиці. \\
За даними таблиці розрахуємо коефіцієнт детермінації між $X_{"""
    + str(settings.task_1_x)
    + r"""} \;$ і $Y_{"""
    + str(settings.task_1_y)
    + r"""} \;$. \\"""
)

grouped = table.groupby("X")

groups = []
mean_values = []
results = []

current_index = 1

print(
    r"""\begin{tabular}{ |c| c| c|} 
\hline
\bigcell{l}{"""
    + settings.task_1_x_meaning
    + r"""}
& 
\bigcell{l}{"""
    + settings.task_1_y_meaning
    + r"""} 
& 
\bigcell{l}{} \\
\hline"""
)

for i, (x, group) in enumerate(grouped):
    group = group.set_index(
        pd.Index(range(current_index, current_index + len(group))), drop=True
    )

    print(r"\bigcell{l}{", end="")

    if len(group) == 1:
        print(f"$x_{{{group.index.values[0]}}} = {x}$", end="")
    elif len(group) == 2:
        print(
            f"$x_{{{group.index.values[0]}}} = x_{{{group.index.values[1]}}} = {x}$",
            end="",
        )
    else:
        print(
            f"$x_{{{group.index.values[0]}}} = \\dots = x_{{{group.index.values[-1]}}} = {x}$",
            end="",
        )
    print("}\n&")

    print(r"\bigcell{l}{", end="")

    print(r"$\displaystyle", end=" ")
    for raw_index, (index, value) in enumerate(group.iterrows()):
        print(
            f'y_{{{index}}} = {value["Y"]}, '
            + (r"\;\; " if (raw_index + 1) % 3 != 0 else "\\\\\n"),
            end="",
        )

    print("$}\n&")

    print(r"\bigcell{l}{", end="")
    ym = group["Y"].mean()
    result = round(sum([(yi - ym) ** 2 for yi in group["Y"]]), 3)
    results.append(result)
    print(f"$\\displaystyle \\overline{{y_{{{i+1}}}}} = {round(ym, 3)}\\\\")
    print(
        f"\\displaystyle\\sum_{{i = {current_index}}}^{{{current_index + len(group) - 1}}}"
        + f"(y_i - \\overline{{y}})^2 = {result}$",
        end="",
    )

    print("}\\\\\n\\hline")

    current_index += len(group)

    groups.append(group)

print(r"\end{tabular} \\ \\ \\ \\ ")

# print(table.groupby("X")["Y"].apply(list))

print(
    r"""Нехай нас цікавить ступінь тісноти статистичного зв’язку між результуючим показником y та пояснюючою змінною x. Очевидно, що ступінь тісноти зв’язку можна вважати максимальним, якщо по заданому значенню змінної x можна відтворити відповідне значення змінної y. І навпаки: якщо значення величини x не несе ніякої інформації про значення показника y , то зв’язок відсутній зовсім, і відповідний вимірник ступеня його тісноти повинен приймати мінімально можливе значення.\\
Введемо поняття ступеня виміру тісноти зв’язку під назвою коефіцієнт детермінації. Розглянемо його вибіркову характеристику. Обчислення вибіркового (емпіричного) значення коефіцієнта детермінації y по x виконується
за формулою 
Розрахуємо вибіркове значення дисперсії "нев'язок"  $\displaystyle \epsilon(x):$ згідно з формулою: $$\displaystyle S_{\epsilon}^2 = \frac{1}{n}\sum_{j=1}^s\sum_{i = 1}^{\nu_j}(y_{ji} - \overline{y_j})^2$$ отримаємо: """
)

s2e = sum(results) / 30

print(
    r"$$\displaystyle S_{\epsilon}^2 = \frac{1}{30}"
    + "("
    + " + ".join([str(i) for i in results])
    + f") = {round(s2e, 3)}$$"
)

print(r"Далі розрахуємо $\displaystyle \overline{y} \; - $ середнє значення ознаки:")

y_avg = sum(table.Y) / 30

print(
    r"$$\displaystyle \overline{y} = \frac{1}{n}\sum_{i=1}^{n}y_{i}"
    + r" = \frac{1}{30}\sum_{i=1}^{30}y_{i} = "
    + f"{round(y_avg, 3)}$$"
)

print(r"Тоді середнє значення ознаки буде дорівнювати:")

s2y = sum([(yi - y_avg) ** 2 for yi in table.Y]) / 30

print(
    r"$$\displaystyle S^{2}_{y} = \frac{\displaystyle \sum_{i=1}^{n} (y_{i}"
    + r" - \overline{y})^2}{n} = \frac{1}{30}\sum_{i=1}^{30} (y_{i} - \overline{y})^2 = "
    + f"{round(s2y, 3)}$$"
)

print(r"Маємо:")

kd = 1 - s2e / s2y

print(
    r"$$\displaystyle \widehat{K}_{d}(y;x) = 1 - \displaystyle"
    + r"\frac{\displaystyle S^{2}_{\epsilon}}{\displaystyle S^{2}_{y}} = "
    + f"1 - \\frac{{{round(s2e, 3)}}}{{{round(s2y, 3)}}} = {round(kd, 4)}$$"
)

print(
    r"""\subsection{Висновок}
Коефіцієнт детермінації -  поняття ступеня виміру тісноти зв’язку, це статистичний показник, що використовується в статистичних моделях як міра залежності варіації залежної змінної від варіації незалежних змінних.  Вiн характеризує долю варiацiї залежної змiнної, обумовленої регресiєю. \\
Коефiцiєнт детермiнацiї належить промiжку $[0;1].$ Чим ближче значення коефіцієнта до 1, тим сильніше залежність і тим краще модель описує статистичні дані. 
У моєму випадку значення $K_{d} = """
    + str(round(kd, 4))
    + r""",$ тобто він вказує на те, що """
    + str(round(kd * 100, 2))
    + r"""\% варіації рівняпродуктивності праці на досліджуваних підприємствах зумовлено варіацією фондовідаччі. При значеннях показників тісноти зв'язку менше $0.7$ величина коефіцієнта детермінації завжди буде нижче 50\%. Це означає, що на частку варіації факторних ознак доводиться менша частина в порівнянні з іншими неврахованими в моделі факторами, що впливають на зміну результативного показника. Побудовані при таких умовах регресивні моделі мають низьке практичне значення.
\subsection{Коефiцiєнт Фехнера}
Коефіцієнт Фехнера визначається виразом:
$$\displaystyle K_{\phi} = \frac{C - H}{n}$$
де $C, \; H$ - число випадків (спостережень, об’єктів), в яких по парі ознак $x$ і $y$ спостерігається відповідно збіг або незбіг знаків відхилень від середніх рівнів, а $n$ – кількість спостережень. \\
Зазначимо, що коефіцієнт Фехнера за абсолютною величиною не перевищує 1. Якщо він дорівнює $\pm 1$, то зв’язок між ознаками близький до функціонального. Про вигляд зв’язку – лінійний чи нелінійний – по величині коефіцієнта Фехнера нічого певного сказати не можна. \\
Визначити, чи існує зв’язок між фондовідаччею та продуктивністю праці, використовуючи дані таблиці. \\"""
)

x_mean = table.X.mean()
y_mean = table.Y.mean()

df_feh = pd.DataFrame(
    {
        i
        + 1: [
            table.X.iloc[i],
            "-" if table.X.iloc[i] < x_mean else "+",
            table.Y.iloc[i],
            "-" if table.Y.iloc[i] < y_mean else "+",
        ]
        for i in table.index.values
    },
    index=[
        r"Фондовiдачча $x$",
        r"Знак \\ $x-\overline{x}$",
        r"Продуктивнiсть працi $y$",
        r"Знак \\ $y-\overline{y}$",
    ],
)

dfs = [
    df_feh.loc[:, 0:8],
    df_feh.loc[:, 9:16],
    df_feh.loc[:, 17:24],
    df_feh.loc[:, 25:].copy(),
]

dfs[3].loc[:, r"$\sum$"] = [round(sum(table.X), 3), "", round(sum(table.Y), 3), ""]
dfs[3].loc[:, r"$\overline{z}$"] = [round(x_mean, 3), "", round(y_mean, 3), ""]

for df in dfs:
    print(
        r"""\begin{table}[H]
\centering
\begin{tabular}{|c |c |c |c |c |c |c |c |c |}
\hline
\bigcell{l}{\\$i$}
""",
        end="",
    )

    for name in df.columns:
        print(f"& \n\\bigcell{{l}}{{${name}$}}\n", end="")
    print(r"\\")

    for index, row in df.iterrows():
        print(f"\\hline\n\\bigcell{{l}}{{{index}}}")
        for val in row:
            print(f"&\n\\bigcell{{l}}{{{f'${val}$' if val != '' else ''}}}\n", end="")
        print(r"\\")

    print(
        r"""\hline
\end{tabular}
\end{table}"""
    )

# for i, v in df_feh.iteritems():
#     print()
#     print(v)

C = len(
    list(
        filter(
            lambda value: value[r"Знак \\ $x-\overline{x}$"]
            == value[r"Знак \\ $y-\overline{y}$"],
            [v[1] for v in df_feh.iteritems()],
        )
    )
)

print(f"Маємо  $C = {C}, \\; \\; H = {30 - C},$ тоді")

print(
    f"$$\\displaystyle K_{{\\phi}} = \\frac{{C - H}}{{n}} = {round((C - (30 - C)) / 30, 2)}$$"
)
