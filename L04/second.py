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

print(computepay(getHours(), getRate()))
