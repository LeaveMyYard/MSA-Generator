import settings
import pandas as pd

X = settings.tables["А.10"][settings.task_7_X]
Y = settings.tables["А.10"][settings.task_7_Y]

if settings.task_7_X == "С":
    X = [{"ч": 1, "ж": 0}[d] for d in X]

table = pd.DataFrame(list(zip(X, Y)), columns=[settings.task_7_X, settings.task_7_Y])
