# Given list of integers, determine the number of occurrences of each item in the list and print out the item and each
# occurrence.

# Example, given a list [2,2,3,5,2,3,1,0,5].

data = [2, 2, 3, 5, 2, 3, 1, 1, 0, 5, 5, 5, 0, 1 ]
dic = {}
for i in data:
    if i in dic:
        count = dic[i]
    else:
        count = 0
    # update the dictionary
    dic[i] = count + 1
print (dic)

for key, value in dic.items ():
    print (key, value)
