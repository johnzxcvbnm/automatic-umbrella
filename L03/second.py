try:
    h = float(input("Enter Hours: "))
except:
    print("Error!  You get no hours!")
    h = 0

try:
    r = float(input("Enter rate: "))
except:
    print("Error! You work for free!")
    r = 0

pay = h * r

if h > 40 :
    pay += (h - 40) * (0.5 * r)

print("Pay:", pay)
