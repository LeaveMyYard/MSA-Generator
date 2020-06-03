import pandas as pd
import settings

Y1 = list(settings.tables["А.4"][settings.task_3_y1])
Y2 = list(settings.tables["А.4"][settings.task_3_y2])
X1 = list(settings.tables["А.4"][settings.task_2_x1])
X2 = list(settings.tables["А.4"][settings.task_2_x2])
X3 = list(settings.tables["А.4"][settings.task_2_x3])
X4 = list(settings.tables["А.4"][settings.task_2_x4])

table = pd.DataFrame(
    list(zip(X1, X2, X3, X4, Y1, Y2)), columns=["X1", "X2", "X3", "X4", "Y1", "Y2"]
)
