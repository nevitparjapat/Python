a=int(input("Enter a number"))
b=int(input("Enter a number"))
c=int(input("Enter a number"))
d=int(input("Enter a number"))

if(a>b):
    if(a>c):
        if(a>d):
            print("a is greater")
        else:
            print("d is Greater")
else:
 if(b>c):
    if(b>d):
        print("b is greater")
    else:
        print("d is Greater")
 else:
  if(c>d):
    print("c is greater")
  else:
    print("d is greater")

  