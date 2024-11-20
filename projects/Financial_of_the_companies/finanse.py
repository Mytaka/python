import numpy as np
import pandas as pd

df = pd.read_csv('projects\Financial_of_the_companies\dataset.csv')
print(df.info())

print(df.head())

# df['2023'].dropna(how=any,inplace=True)
# print(df['2023'][:])

groups = df.groupby('Територіальний розріз').agg({'2021': np.sum,
                                               '2022': np.sum,
                                               '2023': np.sum})

print(groups)

#ser = groups['2023'] - groups['2021']

#print(ser)
#print(ser.max())
#print(ser.min())

