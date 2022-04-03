# Changing Items in a Tuple
data = ("you", "you", "family", "us", "others", "they")
# # change to list
NewList = list (data)
print (type (NewList))
# # Change data
NewList[2] = "Bismarck"
# # add items
NewList.append ("Everybody")
print (NewList)
# # convert to tuple
data = tuple (NewList)
print (data)
print (type (data))

# checking key words
for i in data:
    if "others" in i:
        print ("It exists")
        break
    else:
        print ("It does not exists")

print ("others" in data)

# or
if "red" in data:
    print ("Others exists in our tuple")
elif "Bismarck" in data:
    print ("Bismarck exists in our tuple")
else:
    print ("They don't exists in our tuple")
print('*'*20)
# personal challenge
data2 = ("Bismarck", "others")
if data2 in data:
    print (f'{data2} exists in our tuple')
else:
    print('none exists in our tuples')
