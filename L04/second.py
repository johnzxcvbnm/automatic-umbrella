def computepay(h, r):
    pay = h * r
    if(h > 40):
        pay += (h - 40) * (r * .5)
    return pay

def getHours():
    myHours = -1
    while(myHours < 0):
        try:
            myHours = float(input("Enter in hours: "))
        except:
            print("Invalid number")
    return myHours

def getRate():
    while( True ):
        try:
            myRate = float(input("Enter rate: "))
            if(myRate >= 0):
                return myRate
            else:
                print("Invalid number")
        except:
            print("Invalid number")

# try:
#     hours = float(input("Enter in hours: "))
# except:
#     print("Error, you get no hours!")
#     hours = 0

# hours = getHours()

# try:
#     rate = float(input("Enter in rate: "))
# except:
#     print("Error, you now work for free")
#     rate = 0

print(computepay(getHours(), getRate()))
