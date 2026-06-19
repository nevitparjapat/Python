#WAP to find the 3 greatest Number enterd by user

a=int(input("Enter a 1st Number : "))
b=int(input("Enter a 2nd Number : "))
c=int(input("Enter a 3rd Number : "))

#if(a>b and a>c):
#    print(" A is greater",a)
#elif (b>a and b>c):
#    print("B is greater",b)
#elif(c>a and c>b):
#    print("C is greater",c)      
  
if(a>b):
    if(a>c):
        print("a is greater")
    else:
        print("c is greater")
else:
 if(b>c):
    print("b is Greater")
 else:
    print("c is Greater")