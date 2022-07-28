#%% md

# Import Libraries

#%%

import numpy as np
import pandas as pd
import seaborn as sns
sns.set_style("darkgrid")
import matplotlib.pyplot as plt
#%matplotlib inline
plt.style.use('fivethirtyeight')
import warnings
warnings.filterwarnings('ignore')

#%% md

# Data

#%% md

## A -  Cases from Nigeria

#%%

NigCovidurl = 'https://raw.githubusercontent.com/Ustacky-dev/Nigeria-COVID-19-Data-Analysis-Using-Python/main/covidnig.csv'
NigCovid = pd.read_csv(NigCovidurl,thousands=',')


#%% md

## B - Cases from John Hopkins Data Repository

#%%

globalconfirmedurl = 'https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_confirmed_global.csv'
globalconfirmed = pd.read_csv(globalconfirmedurl)


recoveredurl = 'https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_recovered_global.csv'
recovered = pd.read_csv(recoveredurl)


globaldeathurl = 'https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_deaths_global.csv'
globaldeath = pd.read_csv(globaldeathurl)

#%% md

#### Restructure date columns in global confirmed cases

#%%

globalconfirmedheaders = np.array(globalconfirmed.columns)[4:] # Select all date columns

globalconfirmedheadersMain = np.array(globalconfirmed.columns)[:4] # Select all none date columns

globalconfirmed_new = pd.melt(globalconfirmed,id_vars=globalconfirmedheadersMain,
                              value_vars=globalconfirmedheaders,var_name='Date',value_name='cases')\
    .groupby(by =['Province/State', 'Country/Region', 'Lat', 'Long', 'Date']).sum().reset_index() # Arrange all date columns to one column, date.



#%% md

#### Restructure date columns in global recovered cases

#%%

recoveredheaders = np.array(recovered.columns)[4:] # Select all date columns

recoveredheadersheadersMain = np.array(recovered.columns)[:4] # Select all none date columns

recovered_new = pd.melt(recovered,id_vars=recoveredheadersheadersMain,
                              value_vars=recoveredheaders,var_name='Date',value_name='cases')\
    .groupby(by =['Province/State', 'Country/Region', 'Lat', 'Long', 'Date']).sum().reset_index() # Arrange all date columns to one column, date.


#%% md

#### Restructure date columns in global recovered cases

#%%

globaldeathheaders = np.array(globaldeath.columns)[4:] # Select all date columns

globaldeathheadersMain = np.array(globaldeath.columns)[:4] # Select all none date columns

globaldeath_new = pd.melt(globaldeath,id_vars=globaldeathheadersMain,
                              value_vars=globaldeathheaders,var_name='Date',value_name='cases')\
    .groupby(by =['Province/State', 'Country/Region', 'Lat', 'Long', 'Date']).sum().reset_index() # Arrange all date columns to one column, date.



#%% md

## C - External Data

#%%

Budgetdataurl = 'https://raw.githubusercontent.com/Ustacky-dev/Nigeria-COVID-19-Data-Analysis-Using-Python/main/Budget%20data.csv'

RealGDPurl = 'https://raw.githubusercontent.com/Ustacky-dev/Nigeria-COVID-19-Data-Analysis-Using-Python/main/RealGDP.csv'

externalFileurl = 'https://raw.githubusercontent.com/Ustacky-dev/Nigeria-COVID-19-Data-Analysis-Using-Python/main/covid_external.csv'


Budgetdata = pd.read_csv(Budgetdataurl)
RealGDP = pd.read_csv(RealGDPurl)
externalFile = pd.read_csv(externalFileurl)

#%% md

## Task 2 -  View Data Properties

#%% md

#### Reviewing First Five Data Points

#%%

print(NigCovid.head())
print('*'*50,'\n')
print(globalconfirmed_new.head())
print('*'*50,'\n')
print(recovered_new.head())
print('*'*50,'\n')
print(globaldeath_new.head())
print('*'*50,'\n')
print(Budgetdata.head())
print('*'*50,'\n')
print(RealGDP.head())
print('*'*50,'\n')
print(externalFile.head())
print('*'*50,'\n')

#%% md

#### Reviewing Data info

#%%

print(NigCovid.info())
print('*'*50,'\n')
print(globalconfirmed_new.info())
print('*'*50,'\n')
print(recovered_new.info())
print('*'*50,'\n')
print(globaldeath_new.info())
print('*'*50,'\n')
print(Budgetdata.info())
print('*'*50,'\n')
print(RealGDP.info())
print('*'*50,'\n')
print(externalFile.info())
print('*'*50,'\n')

#%% md

## Task 3 - Data Cleaning and Preparation

### Convert to appropriate data type

#### converter into date types

#%%

globalconfirmed_new['Date'] = pd.to_datetime(globalconfirmed_new['Date'])

recovered_new['Date'] = pd.to_datetime(recovered_new['Date'])

globaldeath_new['Date'] = pd.to_datetime(globaldeath_new['Date'])

#%% md

#### Remove commas from scrapped data

#%%

#NigCovid[1:] = NigCovid[1:].replace(',','')
print(NigCovid.info())

#%% md

#### Rename columns in the Nigeria COVID-19 Data

#%%

Nigcovidheaders = np.array(NigCovid.columns) #
NigCovid.rename(columns = {Nigcovidheaders[0]:'States',
                    Nigcovidheaders[1]:'Confirmed',
                    Nigcovidheaders[2]:'Admissions',
                    Nigcovidheaders[3]:'Discharged',
                    Nigcovidheaders[4]: 'Deaths'}, inplace = True)

#%% md

#### Remove comma(,) in numerical data
#### Look into this

#%%

#NigCovid.astype({'Confirmed':'float','Admissions':'float','Discharged':'str','Deaths':'str'})
# list(Nigcovidheaders[1:])
#NigCovid[list(Nigcovidheaders[1:])]= NigCovid.Confirmed.astype(int)
#NigCovid['Confirmed'].replace(',',regex=True,inplace=True)
##NigCovid.Confirmed = NigCovid.Confirmed.astype(float)
##print(NigCovid.info())

#%%
## Save csv

'''

NigCovid.to_csv('NigCovid.csv')
globalconfirmed_new.to_csv('globalconfirmed_new.csv')
recovered_new.to_csv('recovered_new.csv')
globaldeath_new.to_csv('globaldeath_new.csv')
Budgetdata.to_csv('Budgetdata.csv')
RealGDP.to_csv('RealGDP.csv')
externalFile.to_csv('externalFile.csv')

'''
#%% md

#### Extract daily data for Nigeria from the Global daily cases data
#### look into countries present in the data set

#%%

print(globalconfirmed_new['Country/Region'].unique())
# no Nigeria present in the data
country = 'Nigeria'
Nigeria = globalconfirmed_new[globalconfirmed_new['Country/Region'] == country]
print(Nigeria)

#%% md

# Task 4 - Analysis
### Confirmed Covid cases by Laboratory test

#%%

#print(NigCovid)

Top_10_Confirmed = NigCovid.nlargest(10, columns=['Confirmed'])[['States','Confirmed']]
print(Top_10_Confirmed)

sns.catplot (x="States",y ='Confirmed', kind="boxen",
             palette="pastel", edgecolor=".6",
             data=Top_10_Confirmed).fig.suptitle ('Product Ratings by Customers')
plt.show ()
