a=int(input("enter the no."))
fact=1
if a<0:
    print("fact. dosen't exist")
elif a==0:
    print("the fact of 0 is 1")
else:
    for i in range(1,a+1):
        fact=fact*i
    print("the factorial of",a,"is",fact)