fname = "../mbox-short.txt" #input("Enter file name: ")
if len(fname) < 1 : fname = "mbox-short.txt"

fh = open(fname)
count = 0

for line in fh:
    x = line.split()
    #print("From" in x)
    if ("From" in x):
        print(x[1])
        count += 1
#    print(x)
#    print(x[1])
#    count += 1

print("There were", count, "lines in the file with From as the first word")
