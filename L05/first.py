def runMe():
    min = None
    max = None
    while( True ):
        myInput = input("Integer or 'done': ")
        if( myInput == "done"):
            break
        try:
            myNum = int(myInput)
        except:
            print("Invalid input")
            continue
        if(min == None):
            min = myNum
            max = myNum
        elif(min > myNum):
            min = myNum
        elif(max < myNum):
            max = myNum
    print("Max number:", max)
    print("Min number:", min)

runMe()
