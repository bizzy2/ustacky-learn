# Applying Map Method and Apply Method
## Map works on Series alone while Apply works on both Series and Dataframe
import pandas as pd

state_dict = {'Lagos': 'Ikeja',
              'Delta': 'Asaba',
              'Kaduna': 'Kaduna'}
ser1 = pd.Series (state_dict)
state = ['Lagos', 'Kaduna', 'Delta']
ser2 = pd.Series (state)
## using the map method, map each state to the corresponding capital
print (ser1)
print (ser2)
print ('*' * 50)
print (ser2.map (ser1))
print ('*' * 50)
## Note Lambda can be seen as an anonymous function, can be put into a series operation
data = [1, 40, 5, 7, 8, 9]  # We will add plus 1 to this array
ser3 = pd.Series (data)
print (ser3.map (lambda x: x + 1))
print ('*' * 50)


## Summary: Map works on applying an input to every stated value in a series
## Using the Apply Method
## Apply method makes use of functions and apply to every value in Series and Dataframe
def data_classify(data):
    if data < 30:
        return 'Teens'
    else:
        return 'Adult'


## Call the function using the apply method in a series
print (ser3.apply (data_classify))
print ('*' * 50)
## select only Teens
Teens = ser3.apply (data_classify).map(lambda x: x == 'Teens')
print (Teens)
print ('*' * 50)
## Also using the Lambda on the apply method
print (ser3.apply (lambda x: x + 1))
