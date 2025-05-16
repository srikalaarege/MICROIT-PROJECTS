def add(a,b):
    return a+b
def sub(a,b):
    return a-b
def mul(a,b):
    return a*b
def div(a,b):
    return a/b
def mod(a,b):
    return a%b
print("plese select the operation\n"
      "1.ADD\n"
      "2.SUBTRACTION\n"
      "3.MULTIPLICATION\n"
      "4.DIVISION\n"
      "5.MODULUS")
operation=int(input("enter the operation number:"))
a=float(input("enter the first number:"))
b=float(input("enter the second number:"))
if operation==1:
    print(f"{a}+{b}=",a+b)
elif operation==2:
    print(f"{a}-{b}=",a-b)
elif operation==3:
    print(f"{a}*{b}=",a*b)
elif operation==4:
    print(f"{a}/{b}=",a/b)
if operation==5:
    print(f"{a}%{b}=",a%b)
    
 

