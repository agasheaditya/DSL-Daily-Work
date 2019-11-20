import pandas as pd
import numpy as np

df = pd.read_csv("Tdata.csv")
print(df)
series_obj = list(df.columns)
print("Choose sequence From this :-    ",*series_obj[:-1])
user_series_ip = []
print()
print("Enter timeseries sequence: ")
for i in range(len(series_obj)-1):
    x = input("=> ")
    user_series_ip.append(x)

print(*user_series_ip)
table = pd.pivot_table(df,index=user_series_ip,values="Sales",aggfunc=np.sum)#,columns=["State","City","Product","Sales"]
#print(table)

df1 = pd.DataFrame(table)
#print(df1)
df1.to_csv("output.csv")
df2 =  pd.read_csv("output.csv")
print(df2)

count_TS = 0
for i in df2.columns:
    if i =="":
        continue
    count_TS += df2[i].count()


print("Total Timeseries = ",count_TS + 1 -(df2['Sales'].count()))

