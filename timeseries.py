import pandas as pd
import numpy as np

df = pd.read_excel("data.xlsx")
#df = df.drop(['Sales'],1)
#print(df)
#print(df.stack())
#cols = (list(df.columns))
#print(cols)
state = df.unstack('Sales')
set1= list(set(state))
#print(set1)
#print(len(set1))

pivot = pd.pivot_table(df,index=["State","City","Product"],values="Sales",aggfunc=np.sum)#columns="Product"#
df1 = pd.DataFrame(pivot)#, columns =pivot.index
df1.to_excel("output.xlsx")

df2 = pd.read_excel("output.xlsx")
print(df2)
cols = list(df2.columns)
count_TS = 0
for i in cols:
    if i =="":
        continue
    count_TS += df2[i].count()


print("Total Timeseries = ",count_TS + 1 -(df2['Sales'].count()))
