s_set = {'egg', 1, 'bismarck', 'this', 3, 4, 5, 6}
for i in s_set:
    print (i)

# check for items in a set

print ('egg' in s_set)

if 3 in s_set:
    print (3, 'can be found in,', s_set)
else:
    print ('Item cannot be found in', s_set)

s_set.add('butter')
print(s_set)

# discard an item
# diff between remove and discard, remove throws errors when items not found, but discard doesn't
s_set.discard('butter')
print(s_set)
s_set.remove(4)
print (s_set)
# using the pop method of deletion
item = s_set.pop()
# print deleted Item
print(s_set,item)
# to remove all items in a set you use clear method
s_set.clear()
print(s_set)
