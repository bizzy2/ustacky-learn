data = [-100,2,3,4,10,16,26,25,33,44,55,56]
maxNumber = 0
numberIndex = 0
subjects = 0

#Get Index of the maximum Number
for i in range(len(data)):
    if data[i] == max(data):
        maxNumber = data[i]
        numberIndex = i
print(maxNumber)
print(numberIndex)
print('*'*20)

for i in data:
    if i == max(data):
        for j in range(len(data)):
            if i >= 2*data[j]:
                subjects = data[j]
                index = j
                print (f'At position {index}, the subject is {data[j]}')

print('*'*20)
#Does not Satisfy we use below:
counter = 0
for number in data:
    if number == maxNumber:
        continue
    if maxNumber >= 2 * number:
        counter += 1

# now we verify
if counter == len(data) -1:
    print (numberIndex)
else:
    print(-1)


