import pandas as pd
import numpy as np
from scipy.stats import t as Student
from scipy.stats import norm
from scipy.stats import f as fisher
from scipy.stats import chi2
from statistics import median
df = pd.read_csv('C:\\Users\\Kostya\\Desktop\\Table_5.csv')

X = '1'
Y = '3'
med1 = median(df[X])
med2 = median(df[Y])

a = len(df[(df[X]>=med1) & (df[Y]>=med2)])
b = len(df[(df[X]<med1) & (df[Y]>=med2)])
c = len(df[(df[X]>=med1) & (df[Y]<med2)])
d = len(df[(df[X]<med1) & (df[Y]<med2)])

Ka = (a*d-b*c)/(a*d+b*c)

Kk = (a*d-b*c)/np.sqrt((a+b)*(b+d)*(d+c)*(a+c))