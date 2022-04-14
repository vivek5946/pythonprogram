import pandas
import numpy as np
import pandas as pd

# data sructures in python
# series and Dataframes
# series is list with indexes

a = pd.Series([1, 2, 5, 'python', None, 456])
print(type(a))
print(a)

# Dataframe==> it is collection of series and row column representation
# each column will be series
print(a[0])
my_dic1 = {'dehli': 32, 'Goa': 31, 'bang': 29}
city = pd.Series(my_dic1)
print(city)
# dataframe
df1 = pd.DataFrame({'name': ['tom', 'jack', 'sam', 'johan'], 'gender': [
                   'm']*4, 'city': ['bang', 'pune']*2})
print(df1)
# add a new column==>marks
df1['marks'] = [87, 89, 75, 92]
# indexing
print(df1.iloc[1:3, 0:3])  # it will print row 1 and 3 till third column
