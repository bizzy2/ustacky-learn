data = ("me", "you", "family", "us", "others", "they")
for i in data:
    print (i)
print('*'*150)
# getting indexes
items = []
indexes = 0
for i in range(len(data)):
    items = data[i]
    indexes = i
    print(f'At position {indexes}, the item is {items}')
print('*'*150)
# or
for x in data:
    items = x
    indexes = data.index(x)
    print(f'At position {indexes}, the item is {items}')
