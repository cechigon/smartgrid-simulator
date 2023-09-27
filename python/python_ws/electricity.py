import pandas as pd
import math

df = pd.read_csv("https://www.tepco.co.jp/forecast/html/images/juyo-d1-j.csv",encoding = "shift-jis", skiprows=14, nrows=24, header=None)

for i, r in df.iterrows():
    if pd.isnull(r[4]):
        print(input)
        break
    else:
        input = r