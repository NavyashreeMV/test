a=int(input("enter 1st the number:"))
b=int(input("enter the second number:"))
c=int(input("enter the third number:"))

def largest(a,b,c):
    if a>=b and a>=c:
        print(a,"is largest")
        largest2(b,c)
    elif b>=c:
        print(b,"is largest")
        largest2(a,c)
    else:
        print(c,"is largest")
        largest2(a,b)

def largest2(x,y):
    if x>=y:
        print(x,"is second largest")
    else:
        print(y,"is second largest")

largest(a,b,c) 