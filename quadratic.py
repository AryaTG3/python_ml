a=int(input("enter a coefficnt for x2:"))
b=int(input("enter a coefficient for x:"))
c=int(input("enter a coefficient for x0:"))
d=((b**2)-(4*a*c))**0.51
e=(-b+d)/(2*a)
f=(-b-d)/(2*a)
print(e)
print(f)
print("the roots are",e,f)

