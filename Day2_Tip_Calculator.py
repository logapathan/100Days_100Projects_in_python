total=float(input("Please Enter the total cost of the bill:\n$" ))
tip=int(input("Enter how much percentage of the bill you want to tip: Like 10,12,15\n"))
nums=int(input("Enter number of members among who you want to split the bill\n"))
bill=total*(1+(tip/100))
per_person=bill/nums
print(f"Amount each member have to pay is ${per_person}")