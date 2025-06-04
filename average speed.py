a=int(input("enter the number:"))
b=int(input("enter the number2:"))
c=int(input("enter the number3:"))
average=(a+b+c)/3
print("the average is",average)
if a>=average and b>=average and c>=average:
    print("%d is greater than %d,%d and %d" %(average,a,b,c))
else:
    print("invalid input")