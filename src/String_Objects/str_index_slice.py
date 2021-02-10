#%%
import pandas as pd
import os
print (os.getcwd())

#%%
data = pd.read_csv('nba.csv')
data.dropna(inplace=True)
print (data)

# %%
#here e exist in each row of the column (series)
short_data = data.head()
short_data["Index Name"] = short_data["Name"].str.index("e")
short_data
# %%
#just testing on a scalar string
stra = "My name is Adam"
print (stra.index('name'))

# %%
try: 
    short_data["Index Name"]= short_data["Name"].str.index("a") 
except Exception as err: 
    print(err) 
      
# display 
short_data 
# %%
#substring "slice"
short_data["Sub_Name"]= short_data["Name"].str.slice(start=1,stop =2)
print (short_data)
# %%
