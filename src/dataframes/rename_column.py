import pandas as pd
import numpy as np
# d = {'one' : pd.Series([10, 20, 30, 40], index =['a', 'b', 'c', 'd']), 
#       'two' : pd.Series([10, 20, 30, 40], index =['a', 'b', 'c', 'd'])} 

# df = pd.DataFrame(d) 
# print (df)
# print (df.iloc[2])
# df_one = pd.DataFrame( df['one'])
# print (df_one.loc[:])
# df_one = pd.concat(df_one,df['two'].loc[1:len(df)],axis=1)
# print (df_one)

di = {'col1':pd.Series ([1,2,3,4,5,6,7,8,9,10], index=[40,41,42,43,44, 45, 46, 47, 48, 49])
    ,'col2':pd.Series (np.nan, index=[40,41,42,43,44, 45, 46, 47, 48, 49])
     }
df=pd.DataFrame(di)
print (df)
# print (df.iloc[0:3,0:1])
df_lead = df['col1'].shift(-1)
print (df_lead)

df['col1_lead'] = df_lead 
print(df)
# df_rename = pd.DataFrame(df['col1'])
# print (df_rename)

# df_rename.columns(['ssss'])
# print (df_rename)

