largest = None
smallest = None

while True:
    num = input("Enter a number: ")
    if num == "done":
        break
    try :
        fnum = float(num)
        inum = int(num)
        if largest is None :
            largest = inum
        elif inum > largest :
            largest = inum
        if smallest is None :
            smallest = inum
        elif inum < smallest :
            smallest = inum
    except :
        print("Error, please enter numerical value")


print("Maximum is", largest)
print("Minimum is", smallest)
