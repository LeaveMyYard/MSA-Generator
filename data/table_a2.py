"""
    My A2 table data
"""

import pandas as pd
import settings

X = list(settings.tables["А.2"][f"X{settings.task_1_x}"])
Y = list(settings.tables["А.2"][f"Y{settings.task_1_y}"])

table = pd.DataFrame(list(zip(Y, X)), columns=["Y", "X"])
