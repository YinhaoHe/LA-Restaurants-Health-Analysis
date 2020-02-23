import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
import os
import seaborn as sns
import json

df=pd.read_csv("restaurant-and-market-health-inspections.csv")
print(df.head(3).T)


# print(df.columns.values)