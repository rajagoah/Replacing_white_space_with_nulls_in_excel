import openpyxl
import numpy as np
import pandas as pd
from pip._vendor.pyparsing import col

path = r"C:\Users\aarajago\OneDrive - Capgemini\aakarsh personal\00Python\Replacing_blank_with_NULL\test_xl.csv"
df = pd.read_csv(path)

lst = ['Numbers','name']
df2 = pd.DataFrame([[56, 'dsd'],[57, '']], columns = lst)

df3 = df.append(df2, ignore_index= True)
df5=df3.replace(r'^\s*$', np.nan, regex= True)
df5 = df5.fillna('NULL')
df5.to_excel("output_excel.xlsx")
df5.to_csv("output_csv.csv")

