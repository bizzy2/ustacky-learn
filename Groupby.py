import pandas as pd

''''Data input'''

data3 = pd.read_csv ('studentsdata.csv')
print (data3.head ())
print ('*' * 50)

''''Group by Department'''

department = data3.groupby ('department')
print (department)
print ('*' * 50)

## Get the groups from above

print (department.groups)  # the tuples represents the position of occurrence
print ('*' * 50)

## Call occurrence

print (data3.loc[0])
print ('*' * 50)
print (data3.loc[11])
print ('*' * 50)

## How many unique values are present in department

print (data3['department'].nunique ())
print ('*' * 50)

## How many elements per group (Department for example)

print (department.size ())
print ('*' * 50)

''''Get element per group'''

print (department.get_group ('Biochemistry'))
print ('*' * 50)
print (department.get_group ('Statistics'))
print ('*' * 50)
print (department.get_group ('Sociology'))
print ('*' * 50)

## Mathematical manipulations on the groups gotten
print (department.get_group ('Biochemistry')['amount_paid'].sum ())
print ('*' * 50)
print (department.get_group ('Statistics')['amount_paid'].sum ())
print ('*' * 50)
print (department.get_group ('Sociology')['amount_paid'].sum ())
print ('*' * 50)
print (department['amount_paid'].sum ())
print ('*' * 50)
print (department['amount_paid'].mean ())
print ('*' * 50)
print (department['amount_paid'].max ())
print ('*' * 50)
print (department['amount_paid'].min ())
print ('*' * 50)

'''' Aggregation '''

print (department.agg ({'amount_paid': 'sum',
                        'age': 'mean',
                        'grade': 'mean'
                        }))
print ('*' * 50)

print (department.agg ({'amount_paid': ['sum', 'mean', 'max', 'min'],
                        'age': ['mean', 'max', 'min'],
                        'grade': ['mean', 'max', 'min']
                        }))
print ('*' * 50)

## Iterate over all department return data

for name, data in department:
    print(name)
    print(data)
    print ('*' * 50)