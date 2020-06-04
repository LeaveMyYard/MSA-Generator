import settings
import pandas as pd
from scipy.stats import rankdata

exp_1 = rankdata(settings.tables["А.7"][settings.exp_1])
exp_2 = rankdata(settings.tables["А.7"][settings.exp_2])
exp_3 = rankdata(settings.tables["А.7"][settings.exp_3])

table = pd.DataFrame(list(zip(exp_1, exp_2, exp_3)), columns=["1", "2", "3"])
