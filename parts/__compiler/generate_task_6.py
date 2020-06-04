from data.table_a7 import table


print(
    r"""\newpage
\section{Завдання 6}
Група з 8 експертів оцінила за 5-бальною шкалою необхідність включення 13 компетенцій у профіль посади торгового представника: \\
\includegraphics[width = 15cm, height = 9cm]{16.PNG} \\
Розрахувати коефіцієнт конкордації та перевірити його значущість. \\Сформулювати висновки щодо узгодженості думок експертів. \\
Номери експертів для мого варіанту: 1, 6, 7. \\
\subsection{Коефіцієнт конкордації}
Кендалл запропонував показник тісноти статистичного зв’язку між декількома змінними – коефіцієнт конкордації (узгодженості). Він розраховується за формулою:\\
\includegraphics[width = 16cm, height = 2.5cm]{18.PNG} \\
\includegraphics[width = 16cm, height = 13cm]{19.PNG} \\
\includegraphics[width = 16cm, height = 9cm]{20.PNG} \\
\includegraphics[width = 16cm, height = 5cm]{21.PNG} \\ \\
Так как в матрице имеются связанные ранги (одинаковый ранговый номер) в оценках 1-го, 2-го, 3-го экспертов, произведем их переформирование. Переформирование рангов производиться без изменения мнения эксперта, то есть между ранговыми номерами должны сохраниться соответствующие соотношения (больше, меньше или равно). Также не рекомендуется ставить ранг выше 1 и ниже значения равного количеству параметров (в данном случае n = 13). Переформирование рангов производится в табл."""
)

print(
    r"""\begin{table}[H]
\centering
\begin{tabular}{|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c| } 
\hline
\bigcell{l}{}
& 
\bigcell{l}{$1$}
& 
\bigcell{l}{$2$}
& 
\bigcell{l}{$3$}
& 
\bigcell{l}{$4$}
& 
\bigcell{l}{$5$}
& 
\bigcell{l}{$6$}
& 
\bigcell{l}{$7$}
& 
\bigcell{l}{$8$}
& 
\bigcell{l}{$9$}
& 
\bigcell{l}{$10$}
& 
\bigcell{l}{$11$}
& 
\bigcell{l}{$12$}
& 
\bigcell{l}{$13$}
& 
\bigcell{l}{$\displaystyle \sum$}\\"""
)


def wrap_in_bigcell(x):
    if isinstance(x, float) and int(x) == x:
        r = int(x)
    else:
        r = x
    return f"\\bigcell{{l}}{{{r}}}"


for column, values in table.iteritems():
    print("\\hline")
    print(wrap_in_bigcell(column), "& ")
    print(" & ".join([wrap_in_bigcell(value) for value in values]))
    print(f" & {sum(values)}")
    print(r"\\")

print("\\hline\n")
print(wrap_in_bigcell(r"$\displaystyle \sum_{j=1}^3r_{ij}$"), " & ")
print(" & ".join([wrap_in_bigcell(sum(value)) for name, value in table.iterrows()]))
print(f" & {sum([sum(value) for name, value in table.iterrows()])}")
print(r"\\")

print("\\hline")
print(
    wrap_in_bigcell(
        r"$\displaystyle \sum_{j=1}^3r_{ij}-$ \\$- \displaystyle \frac{m(n+1)}{2}$"
    ),
    " & ",
)
print(
    " & ".join([wrap_in_bigcell(sum(value) - 21) for name, value in table.iterrows()])
)
print(f" & {sum([sum(value) - 21 for name, value in table.iterrows()])}")
print(r"\\")

print("\\hline")
print(
    wrap_in_bigcell(
        r"$ (\displaystyle \sum_{j=1}^3r_{ij} -$\\ $- \displaystyle \frac{m(n+1)}{2} )^2$"
    ),
    "& ",
)
print(
    " & ".join(
        [wrap_in_bigcell((sum(value) - 21) ** 2) for name, value in table.iterrows()]
    )
)
print(f" & {sum([(sum(value) - 21)**2 for name, value in table.iterrows()])}")
print(r"\\")

print("\\hline")
print(
    r"""\end{tabular}
\end{table}"""
)

T_j_kj = [
    sum([len(k) ** 3 - len(k) for i, k in table.groupby(j) if len(k) > 1]) / 12
    for j in ["1", "2", "3"]
]

w = sum([(sum(value) - 21) ** 2 for name, value in table.iterrows()]) / (
    1638 - 3 * sum(T_j_kj)
)

print(
    r"Так як присутні об’єднані ранги в аналізованих упорядкуваннях, то для розрахунку коефіцієнту конкордації користуємося формулою (2), де поправочний коефіцієнт $T_j^{k_j}$ (відповідає змінній $x_j$) розраховується як і для коефіцієнта Спірмена:\\"
)
print(
    r"$$\displaystyle \widehat{\omega} = \displaystyle \frac{\displaystyle \sum_{i=1}^{13}\left ( \displaystyle \sum_{j=1}^3r_{ij} - 21 \right )^2}{\displaystyle \frac{19656}{12} - 3\displaystyle \sum_{j=1}^3T_j^{k_j}} =",
    f"{round(w, 3)}$$\\\\",
)
print(
    r"""Коефіцієнт конкордації приймає значення від 0 до 1. Чим більше значення коефіцієнта конкордації, тим більший ступінь узгодженості думок експертів. При W=1 є повна узгодженість думок експертів; якщо W=0, то узгодженість практично відсутня. Оскільки в моєму випадку $\displaystyle \widehat{\omega} = 0.25$, то це вказує на наявність слабкого ступеня узгодженості думок експертів.\\ \\
Тепер перевіримо статистичну значущість аналізованого зв’язку: \\
При наявності об’єднаних рангів розраховується статистика 
$$\displaystyle \chi_{CT}^2 = \frac{\displaystyle S}{\displaystyle \frac{1}{12}mn(n+1) - \displaystyle \frac{1}{n-1}\sum_{j=1}^mT_j^{k_j}}$$"""
)

chi_kr = 21.02607
chi_st = sum([(sum(value) - 21) ** 2 for name, value in table.iterrows()]) / (
    45.5 - 1 / 12 * sum(T_j_kj)
)

print(
    r"Маємо: $\displaystyle \chi_{CT}^2 = "
    + f"{round(chi_st, 3)}"
    + ",$ а $\chi^2(0.05, 12) = 21.02607$\\ \\"
)

if chi_st < chi_kr:
    print(
        r"Отримали, що $\displaystyle \chi_{CT}^2 < \chi^2(\alpha; n-1)$ а це означає, що коефіцієнт конкордації незначимо відрізняється від нуля з ймовірністю 95\% і $\widehat{\omega} = "
        + f"{round(w, 3)}"
        + r"$ - величина випадкова, а тому отримані результати не мають сенсу і не можуть використовуватися в подальших дослідженнях.\\"
    )
else:
    print(
        r"Отримали, що $\displaystyle \chi_{CT}^2 > \chi^2(\alpha; n-1)$ а це означає, що коефіцієнт конкордації значимо відрізняється від нуля з ймовірністю 95\%, а тому отримані результати мають сенс і можуть використовуватися в подальших дослідженнях.\\"
    )
