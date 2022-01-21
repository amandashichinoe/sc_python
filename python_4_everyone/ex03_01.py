# Rewrite your pay program using try and except so that your program handles non-numeric input gracefully by printing a message and exiting the program.
try: 
    hours = int(input("Enter Hours: "))
    rate = float(input("Enter Rate: "))
    pay=rate*hours
    print("Pay: " , round((rate*hours),2))
except:
    print("Error, please enter numeric input")