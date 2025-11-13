import pandas as pd
df=pd.read_csv(input("enter csv file"))
print(df.mean())
print(df.std())
print(df.median())
print(df.mode())