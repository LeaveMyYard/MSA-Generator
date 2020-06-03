import pandas as pd
import settings

X = list(settings.tables["А.6"][settings.task_3_1])
Y = list(settings.tables["А.6"][settings.task_3_2])

table = pd.DataFrame(list(zip(X, Y)), columns=["1", "2"])
