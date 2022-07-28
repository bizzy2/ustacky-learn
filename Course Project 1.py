""" Library Imports """
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

## %matplotlib inline
plt.style.use('fivethirtyeight')
import warnings

warnings.filterwarnings('ignore')

# %%
''' Step 1'''

''' Loading Datasets '''

## Add url
abujaurl = 'https://raw.githubusercontent.com/Ustacky-dev/Pandas-Analytics-Project/main/Abuja_Branch.csv'
lagosurl = 'https://raw.githubusercontent.com/Ustacky-dev/Pandas-Analytics-Project/main/Lagos_Branch.csv'
phurl = 'https://raw.githubusercontent.com/Ustacky-dev/Pandas-Analytics-Project/main/Port_Harcourt_Branch.csv'

## Convert to csv
abujadata = pd.read_csv(abujaurl)
lagosdata = pd.read_csv(lagosurl)
phdata = pd.read_csv(phurl)

data = pd.concat([abujadata, lagosdata, phdata])
print(data.info())
print('*' * 100)

# %%
''' Step 2'''

''' Data Exploration '''

## Head Display
print(data.head())
print('*' * 100)

## Number of rows and columns
print(f'Number of rows: {data.shape[0]} and Number of columns {data.shape[1]}')
print('*' * 100)

## Head Display
print(data.columns)
print('*' * 100)

## Data Description
print(data.describe())
print('*' * 100)

## Findings from summary
print("The total transactions made : " + str(data['Unit price'].describe().get('count')))
print("The maximum unit price sold is : " + str(data['Unit price'].describe().get('max')))
print("The average unit price sold is : " + str(data['Unit price'].describe().get('mean')))
print("The maximum quantity sold is : " + str(data['Quantity'].describe().get('max')))
print("The average quantity sold is : " + str(data['Quantity'].describe().get('mean')))
print("The biggest income gotten is : " + str(data['gross income'].describe().get('max')))
print('*' * 100)

## Has na
print(data.isnull().sum())
print('*' * 100)

## Data information
print(data.info())
print('*' * 100)

# %%
''' Step 3'''

''' Dealing with DateTime Features '''

data['Date'] = pd.to_datetime(data['Date'] + ' ' + data['Time'])

## Drop time so that datetime can be complete

data.drop('Time', inplace=True, axis=1)

## Check Datetime type implemented

print(data.info())
print('*' * 100)

## Get Year, Month, Day, Hours

data['Year'] = data['Date'].dt.year
data['Month'] = data['Date'].dt.month
data['Day'] = data['Date'].dt.day
data['Hours'] = data['Date'].dt.hour

## Get Unique number of hours

Hours = data['Hours'].unique()
print(f'Unique sales hours are => {Hours} ')
print('*' * 100)

# %%
''' Step 4'''

''' Unique Values in Columns '''

## Get category column


category_columns = [col for col in data.columns if data[col].dtype == 'object']
print(category_columns)
print('*' * 100)

## return category values values in category

for col in data.columns:
    if col == 'Invoice ID':
        continue
    if data[col].dtype == 'object':
        print(f'The unique values in  {col} Column are : {format(data[col].unique().tolist())}')

print('*' * 100)

## return category values in category

for col in data.columns:
    if col == 'Invoice ID':
        continue
    if data[col].dtype == 'object':
        print(f'Total Number of unique values in the {col} Column : {len(data[col].unique().tolist())}')

print('*' * 100)

## return category values using value_counts()
print(data['City'].value_counts())
print('*' * 100)

# %%
''' Step 5'''

''' Aggregation with GroupBy '''

## Group by city

## Sum ,Mean, Gross income of each city and highest pay
City = data.groupby('City')
print(City.agg({
    'Total': ['sum', 'mean'],
    'gross income': ['sum', 'max'],
    'Unit price': ['max', 'min'],
    'Quantity': ['sum', 'mean']
}))

# %%
''' Step 6'''

''' Data Visualization '''

## Countplot for Branch

sns.countplot(x='Branch', hue='Branch', data=data).set_title('Branch')

plt.show()

## Countplot for Payment Channel used the most
sns.countplot(x='Payment', hue='Payment', data=data).set_title('Payment Channel')
plt.show()

## Countplot for city with most sales
sns.countplot(x='City', hue='City', data=data).set_title('Most sales by City')
plt.show()

## Countplot for product line analysis
sns.countplot(y='Product line', hue='Product line', data=data).set_title('Product Line Analysis')
plt.show()

## Countplot for Payment method on product line
sns.countplot(y='Product line', hue='Payment', data=data).set_title('Payment Method by Product Line')
plt.show()

## Countplot for Payment method for each branch
sns.countplot(x='Payment', hue='Branch', data=data).set_title('Payment Method by Branch')
plt.show()

## Box plot for Branch with the lowest rating
sns.boxplot(x='Branch', y='Rating', hue='Branch', data=data).set_title('Rating by Branch')
plt.show()

print('Branch B has the lowest rating')

## Product type purchased by gender
sns.catplot(x='Product line', y='Quantity', hue='Gender', data=data, aspect=4).set_title('Purchases by Gender')
plt.show()

## Total sales by gender
## sns.catplot (x='Total', y='Quantity', hue='Gender', data=data, aspect=4).set_title('Total Sales to Gender')
## plt.show ()

## Unit price per product
sns.catplot(x='Unit price', y='Product line', data=data, kind='point').set_title('Unit Price per product')
plt.show()

## Product type per quantity
sns.catplot(x='Product line', y='Quantity', data=data, kind='point').set_title('Purchases by Product line')
plt.show()

# %%
''' Step 7'''

''' StandOut Section '''

''' Summary '''
# Approach
## Month Name = Addition of month name to the dataframe in other to carryout analysis on monthly patterns
## Gender Analysis = Carryout some analysis on purchases/transactions made by both male and female
## Ratings = Analyze ratings based on specific assigned categories

# Methods
## Month Name : by extracting the month name from the date column using the method .dt.month_name ().str[:3]
## I can be able to plot # average gross income

## Gender Analysis: Using the catplot, gender is categorized into male and female and gross income gotten as a result
## of sales # to both gender can be analyzed
## Ratings : Ratings were categorized into Good,Average and Bad, analyzing the occurrences is done by using the catplot

## Profit from gender purchase of products

sns.catplot(x="Gender", y="gross income", order=["Female", "Male"], data=data)
plt.show()

## Tag Ratings

data['Status'] = ['Bad' if col < 5 else 'Good' if col > 7 else 'Average' for col in data['Rating']]

## Sales performance by status

sns.catplot(x="Status", kind="count",
            palette="pastel", edgecolor=".6",
            data=data)
plt.show()

## Month name for time series

data['Month Name'] = data['Date'].dt.month_name().str[:3]
print(data)
## Sales performance by Month

Mdata = data.groupby(['Month Name', 'Year', 'Month'])['gross income'].mean().reset_index()
Mdata = Mdata.sort_values('Month', ascending=True)
print(Mdata)

sns.lineplot(data=Mdata, x="Month Name", y='gross income')
plt.show()

## Number of transactions by Gender

sns.catplot(x="Gender", col="Month Name", col_wrap=4,
            data=data,
            kind="count", height=5.5, aspect=.8).set_titles()
plt.show()

## For some reasons I can't set titles in my plotting above
