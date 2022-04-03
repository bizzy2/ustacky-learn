data = [5, 7, 12, 9, -5, 10]

for i in data:
    print (i)

print ('*' * 20)

###print max number

for i in data:
    if i == max (data):
        print (f'This is the Max Number :- {i}');

print ('*' * 20)
###print min number

for i in data:
    if i == min (data):
        print (f'This is the Min Number :- {i}');
print ('*' * 20)
### Assign a variable to the max number

for i in data:
    if i == max (data):
        maxNumber = i
print (f'This is the Max Number : {maxNumber }');

##or
maxNumber = data[0]
for number in data:
    if number > maxNumber:
        maxNumber = number

print(maxNumber)

