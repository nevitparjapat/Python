#WAP to check if a number enter by user is odd or even 

num=int(input("Enter the Number : "))

if(num%2==0):# " % " is used to get reminder  :" % " is modulus
    print("The Number is Even")
else:
    print("The Number is Odd")
