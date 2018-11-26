def computepay(h, r):
    pay = h * r
    if(h > 40):
        pay += (h - 40) * (r * .5)
    return pay

try:
    hours = float(input("Enter in hours: "))
except:
    print("Error, you get no hours!")
    hours = 0

try:
    rate = float(input("Enter in rate: "))
except:
    print("Error, you now work for free")
    rate = 0

print(computepay(hours, rate))
