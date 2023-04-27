dict={}
for _ in range (int(input("enter the limit:"))):
    item,space,price =input ("enter the item and price:").rpartition(" ")
    dict[item]=dict.get(item,0)+int(price)
print("total item")
for item,price in dict.items():
    print(item,price)