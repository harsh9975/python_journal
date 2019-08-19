nterm=int(input("how many no."))
n1=0
n2=1
count=2
if nterm<=0:
    print("plese enter a positive integer")
elif nterm==1:
    print("fibnocci sequence")
    print(n1)
else:
    print("fibonacci sequence:")
    print(n1,",",n2,end=',')
    
while count<nterm:
    nth=n1+n2
    print(nth,end=',')
    n1=n2
    n2=nth
    count+=1