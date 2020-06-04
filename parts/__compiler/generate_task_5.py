from data.table_a6 import table
from scipy.stats import rankdata
import numpy as np

print(
    r"""\newpage
\section{Завдання 5}
Розглядаються 17 показників ефективності виробничо-господарської діяльності 40 підприємств:\\
1 Продуктивність праці\\
2 Індекс зниження собівартості продукції\\
3 Рентабельність\\
4 Трудомісткість одиниці продукції\\
5 Питома вага робітників у складі промислово-виробничого персоналу\\
6 Питома вага покупних виробів\\
7 Коефіцієнт змінності устаткування\\
8 Премії та винагороди на одного робітника\\
9 Питома вага втрат від браку\\
10 Фондовіддача\\
11 Середньорічна чисельність промислово-виробничого персоналу\\
12 Середньорічна вартість основних виробничих фондів\\
13 Середньорічний фонд заробітної платні промислово-виробничого персоналу\\
14 Фондоозброєність праці\\
15 Оборотність нормованих оборотних коштів\\
16 Оборотність ненормованих оборотних коштів\\
17 Невиробничі витрати\\
Використовуючи початковi данi, розрахувати коефiцiєнти рангової кореляцiї Спiрмена та Кендалла. Перевiрити їх значущiсть. Який висновок можна зробити стосовно
вигляду залежностi мiж ознаками (лiнiйна чи нелiнiйна)?
\subsection{Кореляційний аналіз порядкових (ординарних) змінних: рангова кореляція}
Порядкова змінна дозволяє упорядкувати статистично досліджені об’єкти за ступенем прояву в них деякої властивості. Результатом виміру порядкової змінної є деяка умовна числова позначка, що вказує місце цього об’єкту в ряді з усіх n аналізованих об’єктів, упорядкованих за зменшенням (зростанням) ступеня прояву в них властивості, яку ми вивчаємо. Цю позначку називають рангом. Якщо значення ознаки мають однакову кількісну оцінку, то ранг всіх цих значень дорівнює середньому арифметичному відповідних номерів місць, які вони
визначають. Ці ранги називають зв’язаними. Якщо об’єкти ранжировані за двома ознакам, то маємо можливість оцінити тісноту зв’язку між ознаками, користуючись рангами, тобто тісноту рангової кореляції. Рангова кореляція розраховується при умові, що ознаки підпорядковуються різним законам розподілу або закони
розподілу невідомі.\\
Серед методів оцінки тісноти зв’язку найчастіше використовують рангові коефіцієнти Спірмена і Кендалла. Ці коефіцієнти можуть використовуватися для визначення тісноти зв’язку як між порядковими, так і між кількісними змінними.\\
\subsection{Коефіцієнт кореляції Спірмена}
\includegraphics[width = 16cm, height = 6cm]{13.PNG} \\
\includegraphics[width = 16cm, height = 15cm]{14.PNG} \\ 
\includegraphics[width = 16cm, height = 6cm]{15.PNG} \\ 
Проранжуємо показники ефективності виробничо-господарської діяльності 40 підприємств, отримаємо:\\"""
)

first = np.array(table["1"])
ranks1 = rankdata(first, method="min")

second = np.array(table["2"])
ranks2 = rankdata(second, method="min")

k1 = sum([1 for i, k in table.groupby("1") if len(k) > 1])
k2 = sum([1 for i, k in table.groupby("2") if len(k) > 1])

print(f"$X = (" + ", ".join([str(i + 1) for i in ranks1]) + ")^T$\\")
print(f"$Y = (" + ", ".join([str(i + 1) for i in ranks2]) + ")^T$\\")

print(f"У першій ранжировцi маємо {k1} груп нерозрiзнених рангiв.")
print(f"У другiй ранжировцi маємо {k2} груп нерозрiзнених рангiв.")

Tx = sum([len(k) ** 3 - len(k) for i, k in table.groupby("1") if len(k) > 1])
Ty = sum([len(k) ** 3 - len(k) for i, k in table.groupby("2") if len(k) > 1])

if Tx == Ty == 0:
    print("Так як не має нерозрізнених рангів, використаємо формулу (1):")
else:
    print("Так як є нерозрізнені ранги, використаємо формулу (2):")

if Tx != 0:
    print(
        f"$$T_x = \\displaystyle \\frac{{1}}{{12}}["
        + " + ".join(
            [f"{len(k)}^2 - {len(k)}" for i, k in table.groupby("1") if len(k) > 1]
        )
        + f"] = {Tx}$$"
    )

if Ty != 0:
    print(
        f"$$T_y = \\displaystyle \\frac{{1}}{{12}}["
        + " + ".join(
            [f"{len(k)}^2 - {len(k)}" for i, k in table.groupby("2") if len(k) > 1]
        )
        + f"] = {Ty}$$"
    )

sumDi = sum([(i - j) ** 2 for i, j in zip(ranks1, ranks2)])

print(f"$$ \\displaystyle \\sum_{{i=1}}^{{40}}d_i^2 = {sumDi} $$")

if Tx == Ty == 0:
    print(
        r"Розрахунки коефіцієнта кореляції Спірмена за формулою (1)(формула використовується, якщо сукупнiсть значень ознаки не має зв’язаних рангів):\\"
    )
    rC = 1 - (6 * sumDi) / (40 ** 3 - 40)

    print(
        f"$$ r^C = 1 - \\displaystyle \\frac{{6\\cdot{sumDi}}}{{40^3-40}} = {round(rC, 4)}$$"
    )

else:
    print(
        r"Розрахунки коефіцієнта кореляції Спірмена за формулою (2)(формула використовується, якщо сукупнiсть значень ознаки має зв’язанi ранги):\\"
    )
    rC = (1 / 6 * (40 ** 3 - 40) - sumDi - Tx - Ty) / np.sqrt(
        (1 / 6 * (40 ** 3 - 30) - 2 * Tx) * (1 / 6 * (40 ** 3 - 30) - 2 * Ty)
    )
    print(
        f"$$r^C = \\displaystyle\\frac{{\\displaystyle |\\frac{{1}}{{6}}(40^3 - 40) - {sumDi} - {Tx} - {Ty}}}{{\\displaystyle \\sqrt{{\\left [ \\frac{1}{6}(40^3 - 40) - 2 \\cdot {Tx} \\right ]\\left [ \\frac{{1}}{{6}}(40^3 - 40) - 2 \\cdot {Ty} \\right ]}}}} = {round(rC, 4)}"
    )
    print(r"Розрахунки за формулою (1)(для випадку незв’язаних рангiв) дають: ")

    rC2 = 1 - (6 * sumDi) / (40 ** 3 - 40)

    print(
        f"$$ r^C = 1 - \\displaystyle \\frac{{6\\cdot{sumDi}}}{{40^3-40}} =  {round(rC2, 4)}$$"
    )


print(
    r"Перевіримо статистичну значущість коефіцієнта Спірмена  при $\alpha = 0.05$. \\"
)

tst = abs(rC) * np.sqrt(38 / (1 - rC ** 2))
tkr = 2.3337

print(
    r"Розраховуємо $\displaystyle t_{CT} = \displaystyle |r^C|\displaystyle \sqrt{\displaystyle\frac{n-2}{1-(r^C)^2}} ="
    + f"{round(abs(rC), 4)} \\cdot \\displaystyle \\sqrt{{\\displaystyle \\frac{{38}}{{{1 - rC**2}}}}} = {round(tst, 4)}$\\\\"
)
print(
    r"Обчислимо $t_{KP} = t\left ( \displaystyle \frac{\alpha}{2}, n-2 \right ) = t(0.025, 38) = 2.3337$\\"
)

if tst > tkr:
    print(
        r"Так як $\displaystyle t_{CT} > t_{KP}$, то з ймовірністю 95\%  $r^C$ значимо відрізняється від нуля, зв’язок між ознаками статистично підтверджується з цією ж ймовірністю."
    )
else:
    print(
        r"Так як $\displaystyle t_{CT} < t_{KP}$, то з ймовірністю 95\%  $r^C$ незначимо відрізняється від нуля, відсутність зв’язку між ознаками статистично підтверджується з цією ж ймовірністю."
    )

print(
    r"""\subsection{Коефіцієнт кореляції Кендалла}
Коефіцієнт Кендалла використовується для виміру взаємозв’язку між кількісними і якісними ознаками, що характеризують однорідні об’єкти, ранжировані за одним правилом.\\
\includegraphics[width = 17cm, height = 18cm]{17.PNG} \\ 
Розрахуємо коефіцієнт кореляції Кендалла. Для цього спочатку ранжируємо значення X в порядку зростання. Виписуємо ранги відповідних $y_i$:\\"""
)

placed_y = ranks2[first.argsort()]

print("R_y: " + ", ".join([str(y) for y in placed_y]))
P = sum(
    [sum([1 for val2 in placed_y[i:] if val2 > val]) for i, val in enumerate(placed_y)]
)
Q = sum(
    [sum([1 for val2 in placed_y[i:] if val2 < val]) for i, val in enumerate(placed_y)]
)

S = P - Q

print(
    f"Визначаємо $P$ як суму кількості наступних рангів, що перевищують взятий ранг: $P = {P}$\\\\"
)
print(
    f"$Q$ визначається як сума кількості наступних рангів, що менше взятого рангу:  $Q = {Q}$\\\\"
)
print(f"Тоді $S = P - Q = {P} - {Q} = {S}$ \\\\ \\\\")

rK = 2 * S / 1560
rKst = 0.22

print(
    r"Розрахуємо ранговий коефіцієнт Кендалла $r^K$: $\displaystyle r^K = \displaystyle \frac{2S}{n(n-1)} = "
    + f"\\frac{{{2*S}}}{{1560}} = {round(rK, 4)}.$ \\"
)

print(
    r"""Перевіримо коефіцієнт $r^K$ на значущість при $\alpha = 0.05.$ Маємо: \\
$\displaystyle u_{1 - \displaystyle \frac{\alpha}{2}}\displaystyle \sqrt{\displaystyle\frac{2(2n+5)}{9n(n-1)}} = \displaystyle u_{ \displaystyle 0.975}\displaystyle \sqrt{\displaystyle\frac{2(2\cdot40+5)}{9\cdot40(40-1)}} = \displaystyle 1.96 \displaystyle \sqrt{\displaystyle\frac{170}{14040}} = 1.96 \cdot 0.11 = 0.22.$\\"""
)

if rK > rKst:
    print(
        r"Так як $r^K > 0.22$ , то коефіцієнт Кендалла значимо відрізняється від нуля з ймовірністю 95\%. \\ \\"
    )

else:
    print(
        r"Так як $r^K < 0.22$ , то коефіцієнт Кендалла не значимо відрізняється від нуля з ймовірністю 95\%. \\ \\"
    )

if rK < rC:
    print(
        f"Так як коефіцієнт Спірмена $r^C = {round(rC, 4)},$ а коефіцієнт Кендалла $r^K = {round(rK, 4)},$ то $r^C > r^K$, а це вказує на лінійну залежність між ознаками"
    )
else:
    print(
        f"Так як коефіцієнт Спірмена $r^C = {round(rC, 4)},$ а коефіцієнт Кендалла $r^K = {round(rK, 4)},$ то $r^C < r^K$, а це вказує на нелінійну залежність між ознаками"
    )

