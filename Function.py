def greet():
    print ('Hello World')
    print ('*' * 100)


greet ()


def greet2():
    name = input ('What is your name? ')
    print ('Hello, ', name)
    print ('*' * 100)


greet2 ()


def add_num():
    a = int (input ('First number ->'))
    b = int (input ('First number ->'))
    sum = a + b
    print ('Your total is ', sum)
    print ('*' * 100)


add_num ()


# Using  return

def add_num():
    a = int (input ('First number ->'))
    b = int (input ('Second number ->'))
    sum = a + b
    return sum


new_num = add_num ()
print (new_num)
print ('*' * 100)

# Using  or

def add_num():
    a = int (input ('First number ->'))
    b = int (input ('Second number ->'))
    sum = a + b
    return 'Your total number is, ' + str(sum)


new_num = add_num ()
print (new_num)

