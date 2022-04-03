Number =int( input("Please Guess a number: "))
Guess = 8
while Number != Guess:
    if Number == Guess:
        print (f' You guessed {Number}, you got it')
    else:
        print(f' You guessed {Number}, guess again')
    Number =int( input("Please Guess a number: "))
print("you got it")
