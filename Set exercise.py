a_set = {1,2,3,4,5,6,20,40,15,100,200,41}
print(max(a_set))
print('*'*200)
# Using a loop
highest_number = 0

for i in a_set:
    if i > highest_number:
        highest_number = i
print(highest_number)
