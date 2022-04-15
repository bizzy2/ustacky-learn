First_name = 'milk'
last_name = 'card'
age = 45
full_name = First_name + " " + last_name + " " + str (age)
print (full_name)
print ('*' * 20)
# Or
fullname = "{}, {}"
fullname = fullname.format (First_name, age)
print (fullname)
