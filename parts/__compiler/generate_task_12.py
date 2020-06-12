import settings
from utils import dataframe_to_latex_table, array_2d_to_latex

import numpy as np

print(
    r"""\section{Завдання 12}
За результатами розбиття на два класи агломеративним методом або методом k-середнiх класифiкувати новi об’єкти методом дискримiнантного аналiзу. Об’єкти для дискримiнацiї обрати самостiйно. Надати змiстовну iнтерпретацiю результатам. 
\subsection{Розв'язання}
Розглянуті нижче методи відносяться до таксономічних методів. Таксономія – це наука про правила упорядкування і класифікації.\\
Основним поняттям у таксономічних методах є таксономічна відстань. Це відстань між точками багатовимірного простору, яка найчастіше розраховується за правилами аналітичної геометрії або коефіцієнтів зв’язку. 
\subsection{Дискримінантний аналіз}
Дискримінантний аналіз об’єднує статистичні методи, змістом яких є розрізнення (дискримінація) об’єктів спостереження одночасно за певною групою ознак. Поряд із задачами багатовимірного групування на практиці виникають
задачі розподілу нових об’єктів між уже існуючими групами. Саме такі задачі розв’язуються методами дискримінантного аналізу. Ці методи дозволяють виявити відмінності між групами (класами) і надають можливість класифікувати нові
об’єкти за принципом максимальної подібності.\\
Методи дискримінантного аналізу знаходять застосування в різних галузях діяльності людини: економіці, соціології, медицині, психології, археології і т. д.\\
Усі процедури дискримінантного аналізу можна розбити на дві групи. Перша група процедур дозволяє інтерпретувати відмінності між існуючими класами. В цьому випадку визначається:\\
1) чи можна, маючи певний набір характеристик, відрізнити один клас об’єктів від іншого;\\
2) наскільки якісно відібрані характеристики дозволяють виявити відмінності між класами;\\
3) які з відібраних характеристик є найбільш інформативними.\\
Друга група процедур дозволяє проводити класифікацію нових об’єктів між уже існуючими класами в тих випадках, коли невідомо наперед, до якого з цих класів вони належать. Класифікація здійснюється на основі дискримінантних
функцій, які будуються за значеннями характеристик об’єктів існуючих класів. \\
Ознаки, які використовуються для того, щоб відрізняти один клас від іншого, називають дискримінантними змінними. Кожна з них повинна  вимірюватись або за інтервальною шкалою, або за шкалою відношень.\\
Теоретично кількість дискримінантних змінних не обмежена, але на практиці кількість об’єктів спостереження повинна перевищувати кількість дискримінантних змінних щонайменше на два, тобто $m > n + 2$.
На дискримінантні змінні накладаються також певні обмеження. По-перше, кожна змінна повинна бути лінійно незалежною з іншими змінними. Інакше вона не несе нової інформації про відмінність об’єктів і тому є зайвою. По-друге, змінні
кожного з даних класів повинні підпорядковуватися нормальному закону розподілу. По-третє, коваріаційні матриці для генеральних сукупностей припускаються рівними між собою для різних класів.\\
У разі, якщо реальна картина у вибіркових сукупностях відрізняється від висунутих передумов, слід вирішувати питання про доцільність використання процедур дискримінантного аналізу для класифікації нових спостережень, оскільки в цьому випадку важко вести розрахунки кожного критерію класифікації.\\
Нехай маємо певну множину одиниць спостережень – генеральну сукупність. Кожна одиниця спостереження характеризується декількома ознаками $x_1, x_2, \dots, x_n,$ які відібрані як дискримінантні змінні.\\
Припустимо, що вся множина об’єктів розбита на декілька підмножин. З кожної підмножини взята вибірка об’ємом $n_k$, де k – номер підмножини, $k = 1,...,p$. Тоді дискримінантна функція записується як лінійна комбінація
дискримінантних змінних у вигляді $$f(x)=a_1x_1+a_2x_2+\dots+a_nx_n.$$
При цьому функції будуються таким чином, щоб з одного боку вони забезпечували максимальну відмінність середніх значень кожного класу, а з іншого – щоб значення різних функцій для кожного класу були некорельовані. \\
\includegraphics[width = 16cm, height = 18cm]{12_1.PNG} \\
\includegraphics[width = 16cm, height = 23cm]{12_2.PNG} \\ 
\begin{center}
    \textbf{Перевірка гіпотез}
\end{center}
У дискримінантному аналізі при побудові дискримінантної функції виникають три питання:\\
1. Наскільки значущі змінні, що відібрані в ролі дискримінантних, і чи є їх набір достатнім?\\
2. Чи придатна для класифікації побудована дискримінантна функція?\\
3. Наскільки побудована функція узгоджується з деякою гіпотетичною функцією, яка розподіляє генеральні сукупності? \\
\includegraphics[width = 16cm, height = 23cm]{12_3.PNG} \\ 
\includegraphics[width = 16cm, height = 23cm]{12_4.PNG} \\ 
\includegraphics[width = 16cm, height = 6cm]{12_5.PNG} \\ 
У таблиці наведені дані показників країн світу. За допомогою методу k-середніх провели їх розбиття
на два класи.\\
Тут:
\begin{itemize}
    \item $x_1$ - ВВП на душу населення (у дол. США за купівельною спроможністю валют),
    \item  $x_2$ - Відсоток міського населення,
    \item $x_3$ - Відсоток грамотних,
    \item $x_4$ - Тривалість життя чоловіків (у роках).
\end{itemize}  
\textbf{Країни}
\begin{itemize}
\item Норвегія (1)
\item ОАЕ (2)
\itemПАР (3)
\itemПівденна Корея (4)
\itemПівнічна Корея (5)
\itemПольща (6)
\itemПортугалія (7)
\itemРосія (8)
\itemСаудівська Аравія (9)
\itemСінгапур (10)
\end{itemize}"""
)

print(dataframe_to_latex_table(settings.task_12_table_1, caption="Класс 1"))
print(dataframe_to_latex_table(settings.task_12_table_2, caption="Класс 2"))

print(
    r"Методом дискримінантного аналізу потрібно класифікувати ще чотири країни, значення ознак для яких наведені нижче: "
)

print(dataframe_to_latex_table(settings.task_12_table_new, caption="Новые страны"))

print(
    r"""Дискримінантна функція має вигляд $\displaystyle f(x) = a_1x_1 + a_2x_2 + a_3x_3 + a_4x_4.$ \\
Коефіцієнти $a_1, a_2,a_3,a_4 $визначаються за формулою $\displaystyle A=S^{-1}(\overline{X_1} - \overline{X_2})$, де $X_1 , X_2$ – вектори середніх у першій і другій вибірці (класі), $A$ – вектор коефіцієнтів, $S$ – об’єднана коваріаційна матриця. 
Розрахуємо середні значення кожної змінної в окремих класах: \\"""
)

df1 = settings.task_12_table_1
df2 = settings.task_12_table_2

X1_overline = np.array(df1.mean(axis=0))
X2_overline = np.array(df2.mean(axis=0))

add = r"\displaystyle \overline"

print(
    f"$$ {', '.join([add + f'{{x_{{{i}1}}}} = {round(val, 2)}' for i, val in enumerate(X1_overline)])} $$"
)
print(
    f"$$ {', '.join([add + f'{{x_{{{i}2}}}} = {round(val, 2)}' for i, val in enumerate(X2_overline)])} $$"
)

X1_overline = X1_overline.reshape((4, 1))
X2_overline = X2_overline.reshape((4, 1))

S = 1 / 8 * (X1_overline.dot(X1_overline.T) + X2_overline.dot(X2_overline.T))

print(
    r"Розрахуємо $S = \displaystyle\frac{1}{m_1+m_2-2}(\tilde{X_1}^T\tilde{X_1}+\tilde{X_2}^T\tilde{X_2})=$"
)

print(array_2d_to_latex(S, rounding=2))

print(
    r"Знайдемо вектор коефіцієнтів дискримінантної функції за формулою $\displaystyle A=S^{-1}(\overline{X_1} - \overline{X_2})$"
)

A = np.linalg.inv(S).dot(X1_overline - X2_overline)

print(array_2d_to_latex(A, rounding=5))

print(
    r"Тоді дискримінантна функція має вигляд $\displaystyle f(x) =",
    " + ".join(
        [f"{round(val, 5)}x_{{{i+1}}}" for i, val in enumerate(A.reshape((4,)))]
    ),
)

print(r"Розрахуємо значення дискримінантної функції для кожної країни обох класів: \\")

f_1 = []
f_2 = []

for i, val in enumerate(df1.values):
    f_val = np.round(A.T.dot(val.reshape((4, 1))), 2)[0, 0]
    f_1.append(f_val)
    print(f"$$ f_{{1{i+1}}} = {f_val} $$")

for i, val in enumerate(df2.values):
    f_val = np.round(A.T.dot(val.reshape((4, 1))), 2)[0, 0]
    f_2.append(f_val)
    print(f"$$ f_{{2{i+1}}} = {f_val} $$")

print(
    f"Маємо $$\\displaystyle \\overline{{f_1}} = {np.round(np.mean(f_1), 2)}, \\;\\; \\overline{{f_2}} = {np.round(np.mean(f_2), 2)}$$"
)

C = (np.mean(f_1) + np.mean(f_2)) / 2

print(
    r"Тоді константа дискримінації $C$ дорівнює $\displaystyle C = \frac{\overline{f_1} -\overline{f_2}}{2}= "
    + f"{np.round(C, 2)}"
    + r".$\\"
    + r"Тепер можна провести класифікацію чотирьох країн. Для цього розрахуємо їхні значення дискримінантних функцій: "
)

f = []

for i, val in enumerate(settings.task_12_table_new.values):
    f_val = np.round(A.T.dot(val.reshape((4, 1))), 2)[0, 0]
    f.append(f_val)
    print(f"$$ f_{{{i+1}}} = {f_val} $$")

print(
    r"Ті краіни, в яких $f$ меньше, ніж $C$ віднесимо до другого класу, інші - до першого."
)
