import pandas as pd
from sqlalchemy import create_engine

# %%

''' Opening connection to database'''

## Parameters
user = 'Bismarck'
pw = 'System123'
db = 'world_x'

engine = create_engine (
    f'mysql+pymysql://{user}:{pw}@localhost/{db}')

# %%

City = pd.read_sql_table ('City', con=engine)

# %%

print (City.head ())

# %%
## Writing a query
query = '''SELECT * FROM CITY'''
# %%
query = pd.read_sql_query (query, con=engine)
# %%
print (query)
# %%
## Another sql method for querying
City2 = pd.read_sql ('City', con=engine)
# %%
## Querying
query2 = '''
select country.Code, country.name,countrylanguage.language, IsOfficial
From country
LEFT JOIN countrylanguage
on country.Code = countrylanguage.CountryCode
where country.Code = 'NGA'
'''
# %%
City3 = pd.read_sql (query2, con=engine)
print (City3)
# %%
## Writing back to the database
City3.to_sql ('nigeria_lang', con=engine, index=False)
