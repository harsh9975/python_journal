nterms=int(input("how many terms do u need ?"))
n1=0
n2=1
count=2
if nterms <=0:
    print("please enter a positive integer")
elif nterms==1:
   print("fibonasi sequence:")
   print(n1)
else:
       print("fibonacci sequence:")
       print(n1,",",n2,end=',')
       while count < nterms:
           nth=n1+n2
           print(nth,end=',')
           n1=n2
           n2=nth
           count+=1