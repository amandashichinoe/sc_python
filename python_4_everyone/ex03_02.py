# Rewrite your pay computation to give the employee 1.5 times the hourly rate for hours worked above 40 hours
try:
    hours = int(input("Enter Hours: "))
    rate = float(input("Enter Rate: "))
except:
    print("Error, please enter numeric input")
    quit()

if hours > 40:
    pay=(1.5*rate*(hours-40))+(40*rate)
else:
    pay=rate*hours

print("Pay: " , round((pay),2))