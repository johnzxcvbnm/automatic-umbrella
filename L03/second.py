h = float(input("Enter Hours:"))
r = float(input("Enter rate:"))
pay = h * r

if h > 40 :
    pay += (h - 40) * (0.5 * r)

print(pay)
