import pandas as pd
import numpy as np

df = pd.read_excel("data.xlsx")
#print(df)

table = pd.pivot_table(df,index=["State","City","Product"],values="Sales",aggfunc=np.sum)#,columns=["State","City","Product","Sales"]
#print(table)

df1 = pd.DataFrame(table)
#print(df1)
df1.to_excel("output.xlsx")
df2 =  pd.read_excel("output.xlsx")
print(df2)

count_TS = 0
for i in df2.columns:
    if i =="":
        continue
    count_TS += df2[i].count()


print("Total Timeseries = ",count_TS + 1 -(df2['Sales'].count()))

##
##import pandas as pd
##import numpy as np
##
##df = pd.read_excel("data.xlsx",sheet_name="Sheet2")
###print(df)
##
##table = pd.pivot_table(df,index=["State","City","Product"],values="Sales",aggfunc=np.sum)#,columns=["State","City","Product","Sales"]
###print(table)
##
##df1 = pd.DataFrame(table)
###print(df1)
##df1.to_excel("output1.xlsx")
##df2 =  pd.read_excel("output1.xlsx")
##print(df2)
##
##count_TS = 0
##for i in df2.columns:
##    if i =="":
##        continue
##    count_TS += df2[i].count()
##
##
##print("Total Timeseries = ",count_TS + 1 -(df2['Sales'].count()))
##
