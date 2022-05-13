import pandas as pd
import numpy as np

'''creating pandas from dictionary'''

stud_dict = {'Student': ['Ibrahim', 'Emeka', 'Ayomede'],
             'Score': [40, 39, 98]}
print (stud_dict)
print ('*' * 50)
## convert the above dict to dataframe
data = pd.DataFrame (stud_dict)
print (data)
print ('*' * 50)
## Creating PD from an array, we create a 2- Dimen Array
array = np.array ([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])
print (array)
print ('*' * 50)
data1 = pd.DataFrame (array, columns=['a', 'b', 'c', 'd', 'e'])
print (data1)
print ('*' * 50)
## Creating PD from a list
a_list = [{'a': 1, 'b': 2, 'c': 3}, {'a': 4, 'b': 5, 'c': 6}]
print (a_list)
print ('*' * 50)
data2 = pd.DataFrame (a_list)
print (data2)
print ('*' * 50)
## How about having NAN (Missing Data)
a_list = [{'a': 1, 'b': 2}, {'a': 4, 'b': 5, 'c': 6}]
print (a_list)
print ('*' * 50)
data2 = pd.DataFrame (a_list)
print (data2)
print ('*' * 50)
##  Creating PD from Excel or CSV
data3 = pd.read_excel ('students.xlsx', sheet_name='students')
print (data3)
print ('*' * 50)
## get the first six rows of the above
print (data3.head (6))
print ('*' * 50)
## get the last six rows of the above
print (data3.tail (6))
print ('*' * 50)

'''pandas Attributes and Methods'''

## create and two-dimensional array
array2 = np.arange (15).reshape (5, 3)
print (array2)
print ('*' * 50)
## create index
index = ['a', 'b', 'c', 'd', 'e']
## create columns
columns = ['col1', 'col2', 'col3']
## Create PD
data4 = pd.DataFrame (data=array2, index=index, columns=columns)
print (data4)
print ('*' * 50)
## Applying attribute
print (data4.index)
print (data4.values)
print (data4.columns)
print (data4.dtypes)
print (data4.axes)
print (data4.info ())
print ('*' * 50)
## To make the index a column, we reset the inplace to true
data4.reset_index (inplace=True)
print (data4)
print ('*' * 50)
## To reset the index back
data4.set_index ('index', inplace=True)
print (data4)
print ('*' * 50)

'''PD Selection and Indexing (iloc( integer-location), and loc selection)'''

print (data3.info ())
print (data3.describe ())
print ('*' * 50)
## one square is used data3[name], it returns a series, but two squares returns PD
print (data3['name'])
print (data3[['name']])
print ('*' * 50)
## using iloc
print (data3.iloc[14])
print (data3.iloc[0:9, 0])  # note when printed, row 9 not inclusive
print ('*' * 50)
print (data3.loc[14])
print (data3.loc[0:9, 'name'])  # note when printed, row 9  inclusive
print ('*' * 50)
## Selecting different rows
print (data3.iloc[0:9, [0, 3]])
print (data3.loc[0:9, ['name', 'Biology_score']])
print ('*' * 50)

'''Filtering PD'''

## Select biology scores greater than 70
pd70 = data3['Biology_score'] >= 70
print (pd70)
print ('*' * 50)
## Return data points from above
print (data3[pd70])
## Select biology scores >= 70 and Maths_score>=70
pd70 = (data3['Biology_score'] >= 70) & (data3['Maths_score'] >= 70)
print (pd70)
print ('*' * 50)
## Return data points from above
print (data3[pd70])
## Select biology scores >= 70 or Maths_score>=70
pd70 = (data3['Biology_score'] >= 70) | (data3['Maths_score'] >= 70)
print (pd70)
print ('*' * 50)
## Return data points from above
print (data3[pd70])
print ('*' * 50)
## Adding a data
Ayo = pd.Series (data=['Ayomide Ibrahim', 25, 'Football', 75, 68, 68], index=data3.columns, name=20)
data3 = data3.append (Ayo)
print (data3.tail ())
print ('*' * 50)
## dropping row
data3 = data3.drop (labels=[20])
print (data3.tail ())
print ('*' * 50)
## inserting new column
data3['Physics'] = np.random.randint (70, 100, 20)
print (data3.tail ())
print ('*' * 50)
## or
data3['Agric'] = 70
print (data3.tail ())
print ('*' * 50)
## inserting in a particular location
data3.insert (loc=2, column='Chemistry', value=np.random.randint (70, 100, 20))
print (data3.tail ())
print ('*' * 50)
## Deleting columns
del data3['Chemistry']
print (data3.tail ())
print ('*' * 50)

'''Handling Missing Data'''

## Get missing data
print (data3.isnull ())
print ('*' * 50)
## get the summary above
print (data3.isnull ().sum ())
print ('*' * 50)
## what of not missing
print (data3.notnull ().sum ())
print ('*' * 50)
## filling the null values
datamani = data3.fillna (value=0)
print (datamani)
print ('*' * 50)
## or
dataffill = data3.fillna (method='ffill')  # forward fill, i.e get above value and fill in
print (dataffill)
print ('*' * 50)
## or
databfill = data3.fillna (method='bfill')  # backward fill, i.e get below value and fill in
print (databfill)
print ('*' * 50)
## drop missing data
datadropna = data3.dropna ()
print (datadropna)
