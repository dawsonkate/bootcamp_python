# Create a program that will tell you whether your input is a text or a number.
# If it's a number the program must indicate whether it is even or odd.
# If it's a text the program must specify its length.

var = input('I will let you know whether you have typed a text or a number.\nGo ahead and type it now. ')

if var.isdigit():
    var = int(var)
    if int(var) % 2:
        print(f'{var} is a number. It\'s odd.')
    else:
        print(f'{var} is a number. It\'s even.')
else:
    print(f'"{var}" is a text. It\'s {len(var)} characters long.')
