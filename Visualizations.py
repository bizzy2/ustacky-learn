import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# %%
'''Data'''

data = pd.read_csv ('studentsdata.csv')
print (data)
print ('*' * 50)
# %%
'''Bar Plot'''

department1 = data.groupby ('department').agg ({'amount_paid': 'mean'})

## or

department2 = data.groupby (['department'])['amount_paid'].mean ()
print (department1)
print ('*' * 50)
print (department2)

p = department1.plot.bar ()
plt.show ()

# %%
'''Histogram Plot'''

h = data['amount_paid'].plot.hist ()
plt.show ()

# %%
'''Histogram Plot'''

l = data['amount_paid'].plot.line (x='department', y='amount_paid')
plt.show ()

ln = data.plot.line (x='department', y='amount_paid')
plt.show ()

# %%
'''Scatter Plot'''

df = pd.DataFrame (np.random.randn (1000, 4), columns=list ('ABCD'))
## print (df)
df.plot.scatter (x='A', y='B')
plt.show ()
df.plot.scatter (x='A', y='B', c='C')
plt.show ()
df.plot.scatter (x='A', y='B', c='blue')
plt.show ()

# %%
'''Hexagonal Plot'''
