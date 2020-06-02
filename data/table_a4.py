import pandas as pd
import settings

Y = list(settings.tables["А.4"][settings.task_2_y])
X1 = list(settings.tables["А.4"][settings.task_2_x1])
X2 = list(settings.tables["А.4"][settings.task_2_x2])
X3 = list(settings.tables["А.4"][settings.task_2_x3])
X4 = list(settings.tables["А.4"][settings.task_2_x4])

table = pd.DataFrame(
    list(zip(Y, X1, X2, X3, X4)), columns=["Y", "X1", "X2", "X3", "X4"]
)
