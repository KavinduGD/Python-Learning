print("Pizza !")
size=input("Enter the size - ")

price=0
if size =="L":
    price=25
elif size =="M":
    price=20
elif size =="S":
    price=15
else :
    print("Invalid size. Exiting the app.")
    exit()

pep=input("Do you want pepperoni")    

if pep=="Y":
    if size=="L" or size =="M":
        price=price+3
    else:
        price = price +2

che=input("Do you want cheese")

if che=="Y":
    price=price+1
    
print(f"Your pricee is ${price}")
    
