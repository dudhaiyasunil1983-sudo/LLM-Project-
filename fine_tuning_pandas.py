import pandas as pd

df=pd.read_csv("data.csv")

df=df.dropna()

df=df[df["response"].str.len()>10]

df.to_csv("cleaned_data.csv",index=False)
