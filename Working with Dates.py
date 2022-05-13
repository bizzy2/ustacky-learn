import pandas as pd
import datetime as dt
from datetime import timedelta

''''Data input'''

data3 = pd.read_csv ('studentsdata.csv')
print (data3)
print ('*' * 50)

'''' How date works'''
date = dt.date (2022, 1, 20)
print (date)
print ('*' * 50)
datetime = dt.datetime (2022, 1, 20, 12, 54, 43)
print (datetime)
print ('*' * 50)

## Extracting from date

print (datetime.year)
print (datetime.month)
print (datetime.day)
print (datetime.hour)
print (datetime.minute)
print (datetime.second)
print ('*' * 50)

## parsing date for proper date correction

datetime_pd = pd.to_datetime ('11th of January, 2019')
print (datetime_pd)
print (pd.to_datetime ('2019/01/11 3:23:10 PM'))
print (pd.to_datetime (dt.date (2022, 1, 20)))
print ('*' * 50)

'''' Date working using dict '''

df = pd.DataFrame ({'date1': ['4/06/2019 19:21:34', '5/07/2019 17:32:12', '6/08/2019 16:22:23'],
                    'date2': ['4/09/2019 19:28:45', '5/10/2019 15:43:12', '6/11/2019 19:23:19'],
                    'value': [4, 6, 9]})
print (df)
print ('*' * 50)
print (df.info ())
print ('*' * 50)
## converts date above

df['date1'] = pd.to_datetime (df['date1'])
df['date2'] = pd.to_datetime (df['date2'])
print (df.info ())
print ('*' * 50)
print (df)
## Add year
df['year 1'] = df['date1'].dt.year
df['year 2'] = df['date2'].dt.year
df['month 1'] = df['date1'].dt.month
df['month 2'] = df['date2'].dt.month
df['day 1'] = df['date1'].dt.day
df['day 2'] = df['date2'].dt.day
print (df.info ())
print ('*' * 50)
print (df)
print ('*' * 50)

## Manipulations
df['day diff'] = df['day 2'] - df['day 1']
df['duration'] = df['date2'] - df['date1']
print (df.info ())
print ('*' * 50)
print (df)

## Manipulation of duration for proper format
df['Duration Days'] = df['duration'] / timedelta (days=1)  # converts to days
print (df.info ())
print ('*' * 50)
print (df)
print ('*' * 50)
df['Duration Hours'] = df['duration'] / timedelta (hours=1)  # converts to hours
print (df.info ())
print ('*' * 50)
print (df)
print ('*' * 50)

'''using date as index, set date as index'''
df.index = df['date1'].dt.date
print (df)
print ('*' * 50)

