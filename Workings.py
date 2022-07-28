## imports
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

plt.style.use ('fivethirtyeight')

# %%
'''Data'''
data = pd.read_csv ('studentsdata.csv')
data1 = sns.load_dataset ('iris')
df = pd.DataFrame (np.random.randn (1000, 4), columns=list ('ABCD'))

# %%
'''Data Manipulation'''
department = data.groupby (['department'])['amount_paid'].mean ()

# %%
'''Data plotting'''
# %%
'''Bar Plot'''

department.plot.bar ()
plt.show ()

# %%
'''Histogram'''

data['amount_paid'].plot.hist ()
plt.show ()

# %%
'''Scatter Plot'''

df.plot.scatter (x='A', y='B')
plt.show ()

# %%
'''Hexa Plot'''

df.plot.hexbin (x='A', y='B', gridsize=10)
plt.show ()

# %%
'''Box Plot'''

df.plot.box ()
plt.show ()

# %%
'''Dist Plot'''

sns.jointplot (x='petal_length', y='petal_width', data=data1)
plt.show ()
sns.jointplot (x='petal_length', y='petal_width', data=data1, hue='species')
plt.show ()

# %%
'''joint Plot'''

sns.jointplot () (data1, hue='species')
plt.show ()

# %%
'''box Plot'''

sns.boxplot (x='species', y='petal_width', data=data1)
plt.show ()

# %%
'''violin Plot'''

sns.violinplot (x='species', y='petal_width', data=data1)
plt.show ()

# %%
'''pair Plot'''

sns.pairplot (data=data1, hue='species')
plt.show ()

# %%
'''Heat map'''

sns.heatmap (data=data1.corr (), annot=True, square=True)
plt.show ()
# %%
print (data1.corr())
