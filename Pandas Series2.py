import pandas as pd

# Extracting element from a series
data = [1, 40, 5, 7, 8, 9]
ser1 = pd.Series(data)
## Using dictionary
state_dict = {'Lagos': 'Ikeja',
              'Delta': 'Asaba',
              'Kaduna': 'Kaduna'}
ser2 = pd.Series(state_dict)
## importing file and converting to series
data1 = pd.read_excel ('students.xlsx', usecols=['name']).squeeze(0)
### There squeeze=True converts to a series
# Extracting
print(ser1[2])
print('*'*120)
print(ser1[0:3])
print('*'*120)
print(ser1[[1,4]])
print('*'*120)
## Extracting using names
print(ser2['Lagos'])
print('*'*120)
print(ser2[['Lagos','Kaduna']])
print('*'*120)
## using the get method to return as ordinary string and not object without index
print(type(ser2.get('Lagos')))
print(ser2.get('Lagos'))
print(ser2.get(['Lagos']))
print('*'*120)
# Mathmatical operations on a series
print(ser1.min())
print(ser1.max())
print(ser1.min()+ser1.max())
print(ser1.sum())
print(ser1.count())
print('*'*120)
## get the average
print(ser1.sum()/ser1.count())
print(ser1.mean())
print('*'*120)
## Return index/position of  numbers using operations
print(ser1.idxmin())
print(ser1.idxmax())
print('*'*120)
## Using Index out to get numbers using operations
print(ser1[ser1.idxmin()])
print(ser1[ser1.idxmax()])
print('*'*120)
## Describe a series
print(ser1.describe())