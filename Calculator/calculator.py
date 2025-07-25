# Author: Devashy Patel
a = int(input("Enter first number: "))
print("first number is: ", a)
b = int(input("Enter second number: "))
print("second number is: ", b)


c = int(input(""" 
write number according to the desired task:

1-addition
2-subtraction
3-multiplication
4-division
 
"""))
if c==1:
    print(a+b)
elif c==2:
    print(a-b)
elif c==3:
    print(a*b)
elif c==4:
    print(a/b)