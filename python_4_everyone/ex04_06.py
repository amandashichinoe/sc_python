# Rewrite your pay computation with time-and-a-half for overtime and create a function called computepay which takes two parameters(hours and rate)

def computepay(hours, rate):
    if hours > 40:
        pay=(1.5*rate*(hours-40))+(40*rate)

    else:
        pay = hours * rate

    return pay


hours = int(input("Enter Hours: "))
rate = float(input("Enter Rate: "))

pay = computepay(hours, rate)

print("Pay: " , round(pay,2))