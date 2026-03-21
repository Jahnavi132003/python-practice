n1=int(input("enter first number:"))
n2=int(input("enter second number:"))
op=input("enter operator(+,-,*,/,%):")
if op=="+":
    print(n1+n2)
elif op=="-":
    print(n1-n2)
elif op=="*":
    print(n1*n2)
elif op=="/":
    print(n1/n2)
elif op=="%":
    print(n1%n2)
else:
    print("invalid operator")                    