import settings
from settings import table_for_task_8
from utils import dataframe_to_latex_table

print(
    r"""\newpage
\section{Завдання 8}
1. Розрахувати характеристику $\chi^2$ квадратичної спряженості ознак, коефіцієнт Крамера та інформаційну характеристику $Y^2$. Перевірити їх значущість, сформулювати висновки.\\
2. Розрахувати коефіцієнти Пірсона і Чупрова, зробити висновки. \\"""
)

print(dataframe_to_latex_table(table_for_task_8))
