import settings
import numpy as np

from utils import array_2d_to_latex

print(
    r"""\newpage
\section{Завдання 10}
\begin{itemize}
\item Розрахувати матрицю вiдстаней мiж об’єктами (див. додаток Б), використовуючи у якостi мiри схожостi евклiдову метрику у просторi ознак. 
\item Провести класифiкацiю об’єктiв агломеративним методом, використовуючи у
якостi мiри близькостi кластерiв метод «ближнього сусiда». Накреслити дендрограму. На скiльки класiв доцiльно розбити початкову сукупнiсть об’єктiв?
\item Провести класифiкацiю об’єктiв дивiзимним методом. Накреслити дендрограму.
На скільки класів доцільно розбити початкову сукупність об’єктів? 
\item Надати змiстовну iнтерпретацiю результатам кластеризацiї.
\end{itemize}
\subsection{Розв'язання}
Пiд класифiкацiєю ми будемо розумiти розподiл сукупностi об’єктiв або явищ на однорiднi групи або вiднесення кожного iз об’єктiв до одного з вiдомих класiв (груп).\\
Доцiльнiсть i ефективнiсть застосування тих чи iнших методiв класифiкацiї обумовленi математичною постановкою задачi. Визначальним моментом у виборi математичної постановки задачi є вiдповiдь на питання: на якiй апрiорнiй iнформацiї будується модель? \\
При цьому апрiорна iнформацiя складається з двох частин:\\
- з апрiорних знань про дослiджуванi класи;\\
- з апрiорної статистичної iнформацiї, тобто так званих навчальних вибiрок.\\
При наявностi навчальних вибiрок класифiкацiя проводиться методами параметричного i непараметричного дискримiнантного аналiзу. У випадку вiдсутностi навчальних вибiрок використовуються методи кластерного аналiзу, таксономiї i рiзнi статистичнi гiпотези.\\
До розробки апарату багатовимiрного статистичного аналiзу всi методи класифiкацiї базувалися на використаннi комбiнацiйного групування.\\
Уся сукупнiсть об’єктiв спочатку розбивається на групи значеннями першої, найбiльш важливої ознаки. Потiм усерединi кожної видiленої групи утворюють пiдгрупи за значеннями наступної ознаки i так далi. Цей пiдхiд одержав назву монотетичного.\\
Недолiки такого пiдходу полягають у тому, що кiлькiсть утворених груп є досить великою, у той час як деякi з них можуть мати незначну наповнюванiсть, а то i зовсiм порожнiми. Це призводить до ускладнення процесу групування нових об’єктiв та змiстовного аналiзу одержаних груп.\\
Розвиток засобiв комп’ютерної технiки дозволив значно збагатити процес класифiкацiї. Це призвело до розробки нових напрямкiв у розв’язаннi задач класифiкацiї багатовимiрних даних. Одним з них є застосування методiв кластерного аналiзу.\\
На вiдмiну вiд комбiнацiйних угрупувань, кластерний аналiз приводить до розбиття на класи з урахуванням всiх ознак одночасно. Такий пiдхiд до розбиття на класи називається полiтетичним.\\
Якщо вiдсутнi навчальнi вибiрки або апрiорна iнформацiя про розподiл генеральної сукупностi ознак, то класифiкацiю об’єктiв можна робити методами кластерного аналiзу.\\
Методами кластерного аналiзу можна розв’язувати такi задачi:\\
- класифiкацiя з урахуванням ознак, що дає поглибленi знання про сукупнiсть об’єктiв;\\
- перевiрка наявностi деякої структури в сукупностi об’єктiв;\\
- побудова нових класифiкацiй для слабо вивчених явищ, коли необхiдно встановити наявнiсть зв’язку всерединi сукупностi i привнести до неї структуру.\\
Методи кластерного аналiзу вченi подiляють на такi групи:\\
- iєрархiчнi агломеративнi методи;\\
- iєрархiчнi дивiзимнi методи;\\
- iтеративнi методи групування;\\
- методи пошуку згущень;\\
- методи пошуку модальних значень щiльностi;\\
- факторнi методи;\\
- методи, що базуються на теорiї графiв.\\
Слiд зазначити, що iснують методи кластерного аналiзу, що не вписуються у вищезгадану класифiкацiю.\\
Агломеративнi (об’єднуючi) методи послiдовно об’єднують окремi кластери (класи) в новi, а дивiзимнi  (подiляючi) методи, навпаки, розчленовують кластери на окремi групи. Iснують декiлька алгоритмiв реалiзацiї цих методiв.\\
У iтеративних методах процес класифiкацiї починається iз задання деяких початкових умов (кiлькiсть кластерiв, початковi кластери, порiг завершення процесу класифiкацiї i т. д.). Тому якiсть класифiкацiї i швидкiсть збiгу алгоритму залежить вiд iнтуїцiї i вмiння користувача. Буде краще, якщо за початковi кластери взяти результати роботи iєрархiчних агломеративних методiв.\\
При проведеннi класифiкацiї необхiдно ввести поняття схожостi об’єктiв. Для кiлькiсної оцiнки схожостi введемо поняття метрики, тобто вiдстанi мiж об’єктами.\\
У кластерному аналiзу використовуються рiзнi метрики.\\ Ми будемо використовувати \textbf{Евклідову метрику:} \\ \includegraphics[width = 17cm, height = 5cm]{lab10_1.PNG} \\
Оцінка схожості між об’єктами досить сильно залежить від абсолютного значення ознаки і від ступеня її варіації в сукупності. Щоб усунути вплив подібного явища на процедуру класифікації, необхідно значення змінних стандартизувати (нормалізувати) таким чином: \\ \includegraphics[width = 17cm, height = 3cm]{lab10_2.PNG} \\
Подібність між об’єктами може бути визначена за допомогою вибіркових коефіцієнтів кореляції. Однак слід зважувати на те, що коефіцієнт кореляції вимірює лише лінійний зв’язок між об’єктами. У випадку нелінійного зв’язку за міру близькості об’єктів можна брати кореляційне відношення.\\
Рангові коефіцієнти кореляції використовуються для оцінки близькості об’єктів у випадку, якщо ознаки є ранговими даними.\\
Надалі будемо вважати, що вихідні ознаки вимірюються кількісно. \\ \\
Розрахуємо матрицю вiдстаней мiж об’єктами (див. додаток Б), використовуючи у якостi мiри схожостi евклiдову метрику у просторi ознак."""
)

raw_data = settings.task_10_table_raw.values

xj = np.mean(raw_data, axis=0)

d_xi = np.sqrt(np.sum((raw_data - xj) ** 2, axis=0) / (len(raw_data) - 1))

z = (raw_data - xj) / d_xi

distance_matrix = np.array(
    [[np.sqrt(sum([(xi - xj) ** 2 for xi, xj in zip(i, j)])) for i in z] for j in z]
)

print(array_2d_to_latex(distance_matrix, rounding=2))
