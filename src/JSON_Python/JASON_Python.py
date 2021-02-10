import numpy as np
import pandas as pd
from pandas import Series, DataFrame
from pandas.io.json import  json_normalize
import json
#TODO hahaha
###########################Define a Json object#########################
Book_object = """
  {
   "book":[
      {
         "id":"444",
         "language":"C",
         "edition":"First",
         "author":"Dennis Ritchie "
      },
      {
         "id":"555",
         "language":"C++",
         "edition":"second",
         "author":" Bjarne Stroustrup "
      }
   ]
} 
"""
Book_data = json.loads(Book_object)
print(Book_data)
df_book = DataFrame(Book_data['book'])
print(df_book)

# json.dumps(data)
##################################Read a JSON file#############################
User_Data = json.loads(open('user.json','r').read())
print(User_Data)
# df_user = pd.DataFrame(User_Data)
# print (df_user)

# ###############################################################################
# df_user_normalized = json_normalize(data=User_Data)
# print (df_user_normalized)

