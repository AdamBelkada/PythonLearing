import pandas as pd 
#define a dictionary
data = {
    'apples':[3,2,0,1],
    'oranges':[0,3,7,2]
}
#pass it to a dataframes

purchases = pd.DataFrame(data)
#print(purchases)

# #use a given index for the first column
# purchases_indexed = pd.DataFrame(data, index=['June', 'Robert', 'Lily', 'David'])
# print ("this is purshase df")
# print(purchases_indexed)
# print ("print June's purchase")
# print(purchases_indexed.loc['June'])
# print ("import csv data")
# r_csv_purchase = pd.read_csv('purchases.csv',index_col=0)
# print(r_csv_purchase)
# #print("export to CSV")
# purchases_indexed.to_csv('new_purchases.csv')

#%%
import pandas as pd 
#%%

movies_df = pd.read_csv("IMDB-Movie-Data.csv", index_col="Title")
print ("first rows moveie_df")
movies_df.head()
#%%
print ("last rows moveie_df")
movies_df.tail()
#%%
print ("info movies_df")
print (movies_df.info())
# %%
print("movie shap")
movies_df.shape
# %%
temp_df =movies_df.append(movies_df)
temp_df.shape
# %%
temp_df = temp_df.drop_duplicates()
temp_df.shape
# %%
print ("this should return 0 data because all data will dups,keep = false")
temp_df =movies_df.append(movies_df)
temp_df.drop_duplicates(inplace=True, keep=False)
temp_df.shape
# %%
movies_df.columns

# %%
movies_df.isnull()

# %%
movies_df.isnull().sum()

# %%
revenue = movies_df['Revenue (Millions)']
# %%
revenue.head()
# %%
revenue_mean = revenue.mean()
revenue_mean
# %%
revenue.fillna(revenue_mean,inplace=True)
revenue
# %%
movies_df.isnull().sum()

# %%
movies_df.describe()
# %%
movies_df['Genre'].describe()
# %%
prom = movies_df.loc['Prometheus']
prom
# %%
prom = movies_df.iloc[1]
prom
# %%
condition = (movies_df['Director'] == "Ridley Scott")

condition.head()
# %%
movies_df[movies_df['Rating'] >= 8.6].head(3)
# %%
movies_df[(movies_df['Director'] == 'Christopher Nolan') | (movies_df['Director'] == 'Ridley Scott')].head()
# %%
def rating_function(x):
    if x >= 8.0:
        return "good"
    else:
        return "bad"

# %%
movies_df["Rating_category"] = movies_df["Rating"].apply(rating_function)

movies_df.head(2)
# %%
