import pandas as pd

df = pd.read_excel("15.xlsx")

print(df)

R = df.corr()

print(R)
