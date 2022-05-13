import pandas as pd

'''Merging two data frames'''

## Merging when there is similarities

data_dict1 = {'Name': ['Ibrahim', 'Emeka', 'Emmanuel'],
              'Age': [24, 25, 27],
              'Sport': ['Football', 'Volleyball', 'Swimming']}

data_dict2 = {'Name': ['Nnamdi', 'Ayomide', 'Emeka'],
              'Age': [24, 27, 25],
              'Sport': ['Football', 'Swimming', 'Volleyball']}
data = pd.DataFrame (data_dict1, index=(0, 1, 2))
print (data)
print ('*' * 50)
data2 = pd.DataFrame (data_dict2, index=(3, 4, 1))
print (data2)
print ('*' * 50)

## Stitching/Group together, Note concat and append are same

print (pd.concat ([data, data2]))
print ('*' * 50)
print (data.append (data2))
print ('*' * 50)
## Merge across axis
mdata = pd.concat ([data, data2], axis=1)
print (mdata)
print ('*' * 50)

## Add the join/intercept parameter for similarities
mdata = pd.concat ([data, data2], axis=1, join='inner')
print (mdata)
print ('*' * 50)

## Merge data using two points (keys)
mdata = pd.concat ([data, data2], keys=['X', 'Y'])  # Keys are also important for indexing data points
print (mdata)
print ('*' * 50)
print (mdata.loc['X'])
print ('*' * 50)
print (mdata.loc['Y'])
print ('*' * 50)
'''Combining Columns/Dataframe'''

details1 = {'Key 1': ['k0', 'K1', 'K2', 'K3'],
            'Key 2': ['k0', 'K1', 'K0', 'K1'],
            'Name': ['Ibrahim', 'Emeka', 'Emmanuel', 'Nnamdi'],
            'Age': [24, 27, 25, 26]}

details2 = {'Key 1': ['k0', 'K1', 'K2', 'K3'],
            'Key 2': ['k0', 'K0', 'K0', 'K0'],
            'Course': ['Physics', 'Statistics', 'Mathematics', 'Chemistry'],
            'Sport': ['Football', 'Volleyball', 'Swimming', 'Basketball']}
ddf1 = pd.DataFrame (details1)
ddf2 = pd.DataFrame (details2)
print (ddf1, '\n', ddf2)
print ('*' * 50)
## now merge
mergedData = pd.merge (ddf1, ddf2, 'inner', on='Key 1')
print (mergedData)
print ('*' * 50)
## Using both keys
mergedData = pd.merge (ddf1, ddf2, on=['Key 1', 'Key 2'])  # Interception is found in the 'on' specified
print (mergedData)
print ('*' * 50)
## Using the how
mergedData = pd.merge (ddf1, ddf2, how='inner', on=['Key 1', 'Key 2'])  # Interception is found in the 'on' specified
print (mergedData)
print ('*' * 50)

mergedData = pd.merge (ddf1, ddf2, how='left', on=['Key 1', 'Key 2'])  # Interception is found in the 'on' specified
print (mergedData)
print ('*' * 50)

mergedData = pd.merge (ddf1, ddf2, how='right', on=['Key 1', 'Key 2'])  # Interception is found in the 'on' specified
print (mergedData)
print ('*' * 50)

mergedData = pd.merge (ddf1, ddf2, how='outer', on=['Key 1', 'Key 2'])  # Interception is found in the 'on' specified
print (mergedData)
print ('*' * 50)

'''Joining Dataframe'''

details3 = {'Key': ['k0', 'K1', 'K2', 'K3'],
            'Name': ['Ibrahim', 'Emeka', 'Emmanuel', 'Nnamdi'],
            'Age': [24, 27, 25, 26]}

details4 = {'Course': ['Physics', 'Statistics', 'Mathematics', 'Chemistry'],
            'Sport': ['Football', 'Volleyball', 'Swimming', 'Basketball']}
dff3 = pd.DataFrame (details3)
## Hence we're joining on index we create an index in the pd creation
dff4 = pd.DataFrame (details4, index=['K1', 'K2', 'K3', 'K4'])
print (dff3)
print ('*' * 50)
print( dff4)
print ('*' * 50)
Mergedff = dff3.join (dff4, on='Key')
print (Mergedff)
