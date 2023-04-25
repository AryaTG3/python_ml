
def cap(a):
    k = ""
    for i in a:

        if i.isupper():

            k+=i.lower()
        else:
            k+=i.upper()


    return k

a=input("enter a name:")
e=cap(a)
print(e)
