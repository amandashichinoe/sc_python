# Write a program to prompt the user for hours and rate per hour to compute gross pay
hours = int(input("Enter Hours: "))
rate = float(input("Enter Rate: "))
pay=rate*hours
print("Pay: " , round((rate*hours),2))