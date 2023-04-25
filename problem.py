
a=str(input("enter a name:"))
def cap(a):
    for i in a:
        if i.isupper():
            k = ""
            k+=i.lower()
        else:
            k+=i.upper()
    print(k)
    return()

cap(a)

