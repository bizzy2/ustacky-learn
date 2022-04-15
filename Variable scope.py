var = 10
print (var)
var = 20


def change_var():
    print (var)


def change_var2():
    var = 20
    print (var)


# global call tells the function that the outer variable is same as internal, hover and see response

def change_var3():
    global var
    var = 20
    print (var)


change_var3 ()
