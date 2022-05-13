import pandas as pd

data = ['me', 'myself', 'I', 'you']
ser = pd.Series (data)
print (ser)
data2 = [1, 40, 5, 7, 8, 9]
ser2 = pd.Series (data2)
print (ser2)
print ('*' * 120)
state = ['Lagos', 'Delta', 'Kaduna']
capital = ['Ikeja', 'Asaba', 'Kaduna']
ser3 = pd.Series (data=capital, index=state)
print (ser3)
print ('*' * 120)
# Using dictionary
state_dict = {'Lagos': 'Ikeja',
              'Delta': 'Asaba',
              'Kaduna': 'Kaduna'}
print (state_dict)
ser4 = pd.Series (state_dict)
print (ser4)
print ('*' * 120)
# importing file and converting to series
# data3 = pd.read_excel ('students.xlsx',usecols=['name'],squeeze=True)
# print (data3)
print ('*' * 120)

# working with methods and attributes
## methods require brackets, attributes don't
## get the index of a dictionary
print (ser4.index)  # How attribute looks like
print ('*' * 120)
## get the values of a dictionary
print (ser4.values)  # How attribute looks like
print ('*' * 120)
## get the data type
print (ser4.dtype)
print ('*' * 120)

# Making use of methods
print (ser2.mean ())  # How methods looks like
print (ser2.max ())
print (ser2.sum ())
print ('*' * 120)
# convert from int to str
print (ser2.astype (str))
print ('*' * 120)

# Working with some in-built functions
## converting to a list
listt = list (ser2)
print (listt)
print ('*' * 120)
## converting to a list to dict
dictt = dict (ser4)
print (state_dict)
print (dictt)
print ('*' * 120)
## sorting a list
print (sorted (listt))
print ('*' * 120)
## Length
print(len(listt))
