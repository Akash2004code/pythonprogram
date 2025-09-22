def findgreat(a,b,c):
    if a>=b and a>=c:
        return a
    elif b>=a and b>=c:
        return b
    else:
        return c
a=int(input ("enter a number :"))
b=int(input ("enter a scend number :"))
c=int(input ("enter 3rdnum :"))
greatest =findgreat(a,b,c)
print(f"the {greatest} is greatest")
