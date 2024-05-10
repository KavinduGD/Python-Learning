print("============= Welcome to the Auction ================\n")

auction={}

while(True):
    name=input("inter the name of the person - ")
    price=int(input("Enter the price - "))
    auction[name]=price
    
    if input("Do you want to add another name? 'y' or  'n' - ").lower() =="n":
        break


max=0
name=""

for key in auction:
    if max<auction[key]:
        max=auction[key]
        name=key



print(f"{name} with ${max} win the auction ")

    
    
