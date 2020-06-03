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

print(f"$X = (" + ", ".join([str(i + 1) for i in ranks1]) + ")^T$\\")
print(f"$Y = (" + ", ".join([str(i + 1) for i in ranks2]) + ")^T$\\")

print(
    r"""Так как в матрице имеются связанные ранги (одинаковый ранговый номер) 2-го ряда, произведем их переформирование. Переформирование рангов производиться без изменения важности ранга, то есть между ранговыми номерами должны сохраниться соответствующие соотношения (больше, меньше или равно). Также не рекомендуется ставить ранг выше 1 и ниже значения равного количеству параметров (в данном случае n = 40). \\"""
)

ranks1 = rankdata(first)
ranks2 = rankdata(second)

print(f"$X = (" + ", ".join([str(i + 1) for i in ranks1]) + ")^T$\\")
print(f"$Y = (" + ", ".join([str(i + 1) for i in ranks2]) + ")^T$\\")

print(
    f"У першій ранжировцi маємо {len(ranks1) - len(set(ranks1))} значень з нерозрiзненими рангами."
)

print(
    f"У другiй ранжировцi маємо {len(ranks2) - len(set(ranks2))} значень з нерозрiзненими рангами."
)
