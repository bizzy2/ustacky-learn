string = 'I AM A BILLIONAIRE'
print (string.upper ())
print (string.lower ())
print (string.title ())
print (string.swapcase ())
# strip trailing characters, confirm by introducing len function to count the strings
string = ' I  AM    A    BILLIONAIRE '
print (string.isspace())
print (string.lstrip())
print (string.rstrip())
print (string.strip())
# Strip by special character
string = 'I  AM    A    BILLIONAIRE'
print (string.strip("E"))
# Checking if white space
string = '    '
print (string.isspace())
# counting characters
string = ' I  AM    A    BILLIONAIRE '
print (string.count('I'))
# finding characters
string = 'I  AM    A    BILLIONAIRE '
print (string.find('I'))
