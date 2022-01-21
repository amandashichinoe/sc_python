# Write a program which repeatedly reads numbers until the users enters "done". Once "done" is entered, print out the total, count, and average of the numbers.
# If the user enters anything other than a number, detect their mistake using try and except and print an error message and skip to the next number.

from itertools import count


cont = 0
total = 0.0

while True:
    input_val = input('Enter a number: ')
    if input_val == 'done' :
        break
    try:
        val = float(input_val)
    except:
        print('Invalid input')
        continue

    cont = cont + 1
    total += val

print(total, cont, total/cont)
