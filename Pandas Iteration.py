import pandas as pd
import numpy as np
import time

''' Iterate over rows '''
##  Creating PD from Excel or CSV
data = pd.read_excel ('students.xlsx', sheet_name='students')
print (data.head ())
print ('*' * 50)
## Take out a section to run as the data is much for the testing
df = data.iloc[0:5, 0:3]
print (df)
print ('*' * 50)
## iterate
for row_lable, row in df.iterrows ():
    print (row_lable, row)
print ('*' * 50)
## Because the above presentation is not nice we add spacing
for row_lable, row in df.iterrows ():
    print (row_lable, row, sep='\n', end='\n')
print ('*' * 50)
## determine the time it took for the code to run
start_time = time.time ()
for row_lable, row in df.iterrows ():
    print (row_lable, row, sep='\n', end='\n')
print ('Total time is {}'.format (time.time () - start_time))
print ('*' * 50)
## using tuple for faster run time
start_time = time.time ()
for row in df.itertuples ():
    print (row, sep='\n', end='\n')
print ('Total time is {}'.format (time.time () - start_time))
print ('*' * 50)
''' Iterate over columns '''
start_time = time.time ()
for column_lable, column in df.iteritems ():
    print (column_lable, column, sep='\n', end='\n')
print ('Total time is {}'.format (time.time () - start_time))
print ('*' * 50)
## Using Items alone
start_time = time.time ()
for column_lable, column in df.items():
    print (column_lable, column, sep='\n', end='\n')
print ('Total time is {}'.format (time.time () - start_time))
print ('*' * 50)