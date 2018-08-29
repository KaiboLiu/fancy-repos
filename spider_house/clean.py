import pandas as pd
import sys

fileName = 'rent_lianjia_bj.txt' if len(sys.argv) == 1 else sys.argv[1]
print(fileName)
f = open(fileName,'r')

df = pd.read_csv(f, sep=',', header=None, encoding='utf-8',
                 names=['area', 'title', 'type', 'square', 'orient', 'place', 'floor', 'total_floor', 'price', 'year', 'unit_price'])


print(df.describe())   #list the statistic table of all the numerical columns
print(type(df.describe()))
