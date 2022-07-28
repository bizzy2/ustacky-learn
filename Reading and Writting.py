## Reading CSV, Excel, and Json Files

# %%
import pandas as pd

# %%
''' Reading csv and write to csv '''
data = pd.read_csv ('studentsdata.csv')
print (data)

## save to a new file
data.to_csv ('studentsdatav2.csv')
data1 = pd.read_csv ('studentsdatav2.csv')
print (data1)

# %%
''' Reading Excel and write to Excel '''
data3 = pd.read_excel ('students.xlsx')
print (data3)

## save to a new file
data3.to_excel ('students2.xlsx', sheet_name='data')
data4 = pd.read_excel ('students2.xlsx')
print (data4)

# %%
''' Reading json and write to json '''
data3.to_json ('students.json')
data5 = pd.read_json ('students.json')
print (data5)

# %%
url = 'https://v6.exchangerate-api.com/v6/696b902431afa23d6e429dbe/latest/USD'

data6 = pd.read_json (url)
print(data6)
data6.to_json('exchangerate.json')
