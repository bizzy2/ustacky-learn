import numpy as np
import pandas as pd
import seaborn as sns

plt.style.use('fivethirtyeight')
''''
import warnings
warnings.formatwarning('ignore')
'''
# %%
'''Data'''

data = pd.read_csv('studentsdata.csv')
print(data)
print('*' * 50)
# %%
'''Bar Plot'''

department1 = data.groupby('department').agg({'amount_paid': 'mean'})

## or

department2 = data.groupby(['department'])['amount_paid'].mean()
print(department1)
print('*' * 50)
print(department2)

p = department1.plot.bar()
plt.show()

# %%
'''Histogram Plot'''

h = data['amount_paid'].plot.hist()
plt.show()

# %%
'''Line Plot'''

l = data['amount_paid'].plot.line(x='department', y='amount_paid')
plt.show()

ln = data.plot.line(x='department', y='amount_paid')
plt.show()

# %%
'''Scatter Plot'''

df = pd.DataFrame(np.random.randn(1000, 4), columns=list('ABCD'))
## print (df)
df.plot.scatter(x='A', y='B')
plt.show()
df.plot.scatter(x='A', y='B', c='C')
plt.show()
df.plot.scatter(x='A', y='B', c='blue')
plt.show()

# %%
'''Hexagonal Plot'''

df.plot.hexbin(x='A', y='B', gridsize=30)
plt.show()
df.plot.hexbin(x='A', y='B', gridsize=10)
plt.show()

# %%
'''Box Plot'''
''' Looks into outliers '''

df.plot.box()
plt.show()

# %%
'''Load Iris'''
''' Manipulate data '''

data = sns.load_dataset('iris')
print(data)

# %%
## Distribution plot- How normal a variable is distributed
sns.distplot(data['sepal_length'])
plt.show()

# %%
## Joint Plot - relationship between two variables
sns.jointplot(x='sepal_length', y='sepal_width', data=data)
plt.show()

## To change to hexagonal
sns.jointplot(x='sepal_length', y='sepal_width', data=data, kind='hex')
plt.show()

# %%
## Box Plot - Gives statistical summary of plotted features
sns.boxplot(x='species', y='sepal_length', data=data)
plt.show()

# %%
## Violin Plot - To visualize the distribution of data and its probability distribution
sns.violinplot(x='species', y='sepal_length', data=data)
plt.show()

# %%
## Pair Plot - Also known as scatterplot, shows variable pairs to see where relationships might exist. Read on this.
sns.pairplot(data=data)
plt.show()
sns.pairplot(data=data, kind='scatter', hue='species')
plt.show()

# %%
## Heatmap - Used to find correlation between different features in a dataset,
## high positive show very similar, High negative show no similarity

sns.heatmap(data.corr(), annot=True)  # annot writes the value on the heatmap
plt.show()
sns.heatmap(data.corr(), annot=True, cmap='inferno')  # annot writes the value on the heatmap
plt.show()
