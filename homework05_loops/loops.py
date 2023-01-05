# 1. Create a program that will prompt the user to enter a text and then
# output information for each of the typed characters within that text:
#     - this is a number  + whether its even or odd
#     - this is a letter + whether its uppercase or lowercase
#     - this is a symbol


text = input('Enter something here: ')

for letter in text:

    if letter.isdigit():
        letter = int(letter)
        if letter % 2 == 0:
            print(f'{letter} is an even number')
        else:
            print(f'{letter} is an odd number')
    elif letter.isupper():
        print(f'{letter} is an uppercase letter')
    elif letter.islower():
        print(f'{letter} is a lowercase letter')
    else:
        print(f'{letter} is a symbol')

# 2. Create a program that will print “I love Python” every 4.2 seconds
# until its execution is manually interrupted.

# import time
#
# x = 'I love Python'
#
# while True:
#     print(x)
#     time.sleep(4.2)
