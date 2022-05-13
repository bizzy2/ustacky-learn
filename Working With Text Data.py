import pandas as pd

detail1 = {
    'Name': ['Ibrahim Musa', 'Emeka Ike', 'Emmanuel Nnamdi', 'Nnamdi John'],
    'Age': [24, 27, 25, 30],
    'Sport': ['Football', 'Swimming', 'Volleyball', 'Basketball'],
    'Course': ['Physics', 'Statistics', 'Mathematics', 'Chemistry'],
    'Amount': ['$4000', '$14000', '$5000', '$10000']
}
print (detail1)
print ('*' * 70)
data = pd.DataFrame (detail1)
print (data)
print ('*' * 70)

'''Convert to lower and upper cases'''

print (data['Name'].str.lower ())
print ('*' * 70)
print (data['Name'].str.upper ())
print ('*' * 70)
print (data['Name'].str.swapcase ())  # Converts lower to upper and upper to lower
print ('*' * 70)

'''check case type'''

print (data['Name'].str.islower ())
print ('*' * 70)
print (data['Name'].str.isupper ())
print ('*' * 70)
print (data['Amount'].str.isnumeric ())
print ('*' * 70)

''''Count characters'''

print (data['Course'].str.len ())
print ('*' * 70)

''''Split and replace'''

## cat - Concatenate the series/index elements with given separator
print (data['Name'].str.cat (sep='_'))
print ('*' * 70)

## split - splits each string with the given pattern
print ("we are learning pandas".split (" "))
print ('*' * 70)
print (data['Name'].str.split (" "))
print ('*' * 70)
print (data['Name'].str.split (" ").str.get (0))
print ('*' * 70)

## Setting to different columns
data[['First Name', 'Last Name']] = data['Name'].str.split (" ", expand=True)
print (data)
print ('*' * 70)

'''Working with numeric values'''

## replace/remove  the dollar sign so its numeric
data['Amount'] = data['Amount'].str.replace ('$', '', regex=True).astype (float)
print (data)
print ('*' * 70)
print (data['Amount'].sum ())
print ('*' * 70)
## removing white spaces
print (data['Name'].str.lower ().str.strip())

''' Checking for pattern s'''
## Count - Returns count of appearance of pattern in each element
print (data['Name'].str.lower ().str.count ('e'))
print ('*' * 70)
print (data['Name'].str.lower ().str.count ('m'))
print ('*' * 70)

## Startwith - Returns true if the element in the series/index starts with the pattern
print (data['Name'].str.lower ().str.startswith ('e'))
print ('*' * 70)
print (data['Name'].str.lower ().str.startswith ('i'))
print ('*' * 70)
print (data['Name'].str.lower ().str.endswith ('e'))
print ('*' * 70)
print (data['Name'].str.lower ().str.endswith ('e'))
print ('*' * 70)

## Find - Returns the first positions of the first occurrence of the pattern.
print (data['Name'].str.lower ().str.find ('m'))
print ('*' * 70)
## Find - Returns all characters/occurrence of the pattern.
print (data['Name'].str.lower ().str.findall ('m'))
print ('*' * 70)

