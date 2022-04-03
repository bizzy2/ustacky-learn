# sum up all items in the following tuple: data = (10,20,30,40,50)

data = (10, 20, 30, 40, 50)
print(sum(data))
print('*'*20)
# or
Contain = 0
app = []
for i in data:
    Contain = Contain + i
    app.append(Contain)
    print(Contain)
print('*'*20)
print(Contain)
print(app)