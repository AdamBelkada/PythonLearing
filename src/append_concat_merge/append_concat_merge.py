# DataFrame.append(other, ignore_index=False, verify_integrity=False, sort=False)[source]
# pandas.concat(objs: Union[Iterable[‘DataFrame’], Mapping[Label, ‘DataFrame’]], axis='0', join: str = "'outer'", ignore_index: bool = 'False', keys='None', levels='None', names='None', verify_integrity: bool = 'False', sort: bool = 'False', copy: bool = 'True')
# DataFrame.merge(right, how='inner', on=None, left_on=None, right_on=None, left_index=False, right_index=False, sort=False, suffixes='_x', '_y', copy=True, indicator=False, validate=None)
# DataFrame.join(other, on=None, how='left', lsuffix='', rsuffix='', sort=False)
import pandas as pd
import numpy as np
# df1 = pd.DataFrame({
# 'A':[1,2,3,4],
# 'B':[True,False,True,True],
# 'C':['C1','C2','C3','C4']
# })
# df2 = pd.DataFrame({
# 'A':[5,7,8,5],
# 'B':[False,False,True,False],
# 'C':['C1','C3','C5','C8']
# })
# print ("data frame df1")
# print (df1)
# print ("\ndata frame df1")
# print (df2)
# #Contact axis
# print ("axis=0")
# print (pd.concat([df1,df2],axis=0))
# print ("axis=1")
# print (pd.concat([df1,df2],axis=1))
print ("-------------------------------------using concat with join parameter----------------------------")
#Concat with join
df1 = pd.DataFrame({
'A':[1,2,3,4],
'B':[True,False,True,True],
'C':['C1','C2','C3','C4']
})
df2 = pd.DataFrame({
    'A':[5,7,8,5],
    'B':[False,False,True,False],
    'C':['C1','C3','C5','C8']},
index=[2,3,4,5]
)
df_outer = pd.concat([df1,df2],axis=1,join='outer')
# print (df1)
# print (df2)
# print (df_outer)

# df_inner = pd.concat([df1,df2],axis=1,join='inner')
# print (df_inner)

print("-------------------------------------using merge with how parameter----------------------------")
df1 = pd.DataFrame({
'A':[1,2,3,4],
'B':[True,False,True,True],
'C':['C1','C2','C3','C4']
})
df2 = pd.DataFrame({
    'A':[5,7,8,5],
    'B':[False,False,True,False],
    'C':['C1','C3','C5','C8']},
index=[2,3,4,5]
)
df_merge_how = df1.merge(df2,on = 'C',how = 'inner') #using On if only the column we are joining with has the same name in both df,use left_on,right_on otherwise
print (df_merge_how)

df_merge_how_suffix = df1.merge(df2,on = 'C',how = 'inner',suffixes=('_1','_2')) 
print (df_merge_how_suffix)


print("-------------------------------------using Join----------------------------")
df_join = df1.join(df2,on = 'A',lsuffix='_1',rsuffix='_2') #it's going join on the index still, need to convert the column into an idex first
print(df1)
print (df2)
# df_join.shape()
print(df_join)

print('re-indexing the data frames to perform join on column keys') #
df_join_reindex = df1.set_index('C').join(df2.set_index('C'),on = 'C',lsuffix='_1',rsuffix='_2')
print (df_join_reindex)