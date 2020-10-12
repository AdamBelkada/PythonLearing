import pandas as pd
#import from a list of lists
data = [['tom', 10], ['nick', 15], ['juli', 14]]
df = pd.DataFrame(data, columns = ['Name', 'Age']) 
#print (df)

#import from a dict of arrays
data = {'Name':['Tom', 'nick', 'krish', 'jack'], 'Age':[20, 21, 19, 18]}  
df = pd.DataFrame(data) 
# print (df) 

#repeat same value for all rows
data = {'Name':['Tom', 'nick', 'krish', 'jack'], 'Age':20}  #notice no array symbole
df = pd.DataFrame(data) 
#print (df) 

# indexed dataframe with arrays
data = {'Name':['Tom', 'Jack', 'nick', 'juli'], 'marks':[99, 98, 95, 90]}  
df = pd.DataFrame(data, index =['rank1', 'rank2', 'rank3', 'rank4']) 
#print(df)

#list of dictionaries, if a column missing, will nan value
data = [{'a': 1, 'b': 2, 'c':3}, {'a':10, 'b': 20, 'c': 30}] 
df = pd.DataFrame(data) 
#print (df)
#adding indexes

#dictionnay of series
d = {'one' : pd.Series([10, 20, 30, 40], index =['a', 'b', 'c', 'd']), 
      'two' : pd.Series([10, 20, 30, 40], index =['a', 'b', 'c', 'd'])} 

df = pd.DataFrame(d) 
# print (df)

#using pandans from_records   --here using a list of dicts
data = [{'col_1': 3, 'col_2': 'a'},
        {'col_1': 2, 'col_2': 'b'},
        {'col_1': 1, 'col_2': 'c'},
        {'col_1': 0, 'col_2': 'd'}]
df = pd.DataFrame.from_records(data)
print (df)