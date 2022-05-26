import pandas as pd


df=pd.read_csv('spotify.csv')

df['despacit_sum'] = df['Despacito'].groupby('Despacito').sum()

print(df)