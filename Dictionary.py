my_dict = {
    "Always": "at all times; on all occasions",
    "Purchase": "to acquire by the payment of money or its equivalent; buy",
    "Often": "frequently; many times.",
    "Okada": "Okada (a term used mostly in Nigeria) is a crazy small broken motorcycle"
}
print (my_dict)
# update dictionary
my_dict['New'] = 'New data type'

print ('*' * 200)

for i in my_dict:
    print (f'This are the keys -> {i}, with the corresponding values -> {my_dict[i]}')

print ('*' * 200)

# for values alone
for i in my_dict.values ():
    print (i)

print ('*' * 200)

# for keys and values
for key, value in my_dict.items ():
    print (key, value)
