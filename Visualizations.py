import pandas as pd
from matplotlib.pyplot import plot

'''Data'''

data = pd.read_csv ('studentsdata.csv')
print (data)
print ('*' * 50)

'''Bar Plot'''

department1 = data.groupby ('department').agg ({'amount_paid': 'mean'})
## or
department2 = data.groupby (['department'])['amount_paid'].mean ()
print (department1)
print ('*' * 50)
print (department2)

plot (department1)
