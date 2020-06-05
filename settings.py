import pandas as pd

# ----- Setup this -----
name = "Жукова Павла Петровича"
variant = 7
overleaf_project_directory = r"C:\Users\blackbox1\Documents\GitHub\MSA-TEX"

task_1_y_meaning = "[!Продуктивнiсть працi!]"
task_1_x_meaning = "[!Премії для одного виробника!]"

task_2_y_meaning = "[!Тривалість життя у чоловіків!]"
task_2_x1_meaning = "[!Чисельність населення!]"
task_2_x2_meaning = "[!Народжуванність!]"
task_2_x3_meaning = "[!Смертність!]"
task_2_x4_meaning = "[!Відсоток грамотних!]"

table_for_task_8 = pd.DataFrame(
    data={
        "До 25 років": [
            18212 * variant,
            1914 * variant,
            147 * variant,
            8 * variant,
            4 * variant,
        ],
        "25-34": [
            5574 * variant,
            6677 * variant,
            1112 * variant,
            85 * variant,
            18 * variant,
        ],
        "35-44": [
            498 * variant,
            2171 * variant,
            2595 * variant,
            419 * variant,
            43 * variant,
        ],
        "44-54": [
            98 * variant,
            368 * variant,
            1177 * variant,
            1280 * variant,
            308 * variant,
        ],
        "55 і більше": [
            19 * variant,
            75 * variant,
            271 * variant,
            840 * variant,
            1701 * variant,
        ],
    },
    index=["До 25 років", "25-34", "35-44", "44-54", "55 і більше"],
).transpose()


# ----- Do not touch this -----

sheets = [f"А.{i}" for i in range(1, 15)]

tables = {
    sheet: pd.read_excel(r"data\stat_analiz.xlsx", sheet_name=sheet) for sheet in sheets
}

# ----- Task 1, 2 -----

task_1_y = tables["А.1"].loc[tables["А.1"]["Варіант"] == variant]["Y"].values[0]
task_1_x = tables["А.1"].loc[tables["А.1"]["Варіант"] == variant]["X"].values[0]

# ----- Task 3 -----

task_2_y = (
    tables["А.3"].loc[tables["А.3"]["Варіант"] == variant]["Y для завд. 3"].values[0]
)
task_2_x1 = tables["А.3"].loc[tables["А.3"]["Варіант"] == variant]["X1"].values[0]
task_2_x2 = tables["А.3"].loc[tables["А.3"]["Варіант"] == variant]["X2"].values[0]
task_2_x3 = tables["А.3"].loc[tables["А.3"]["Варіант"] == variant]["X3"].values[0]
task_2_x4 = tables["А.3"].loc[tables["А.3"]["Варіант"] == variant]["X4"].values[0]

task_2_x_meaning = [
    task_2_x1_meaning,
    task_2_x2_meaning,
    task_2_x3_meaning,
    task_2_x4_meaning,
]

# ----- Task 4 -----

task_3_y1 = (
    tables["А.3"].loc[tables["А.3"]["Варіант"] == variant]["Y для завд. 4(1)"].values[0]
)
task_3_y2 = (
    tables["А.3"].loc[tables["А.3"]["Варіант"] == variant]["Y для завд. 4(2)"].values[0]
)

# ----- Task 5 -----

task_3_1 = tables["А.5"].loc[tables["А.5"]["Варіант"] == variant]["Ознаки1"].values[0]
task_3_2 = tables["А.5"].loc[tables["А.5"]["Варіант"] == variant]["Ознаки2"].values[0]

# ----- Task 6 -----

exp_1 = (
    tables["А.8"]
    .loc[tables["А.8"]["Варіант"] == variant]["Номери експертів(1)"]
    .values[0]
)
exp_2 = (
    tables["А.8"]
    .loc[tables["А.8"]["Варіант"] == variant]["Номери експертів(2)"]
    .values[0]
)
exp_3 = (
    tables["А.8"]
    .loc[tables["А.8"]["Варіант"] == variant]["Номери експертів(3)"]
    .values[0]
)

# ----- Task 7 -----

task_7_X = tables["А.9"].loc[tables["А.9"]["Варіант"] == variant]["Ознаки1"].values[0]
task_7_Y = tables["А.9"].loc[tables["А.9"]["Варіант"] == variant]["Ознаки2"].values[0]
