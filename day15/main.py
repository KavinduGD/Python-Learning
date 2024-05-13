import data

resources=data.resources
menu=data.MENU
money=0

# TODO : function- report
def print_report():
    print(f"water :  {resources['water']}g")
    print(f"milk :  {resources['water']}g")
    print(f"coffee :  {resources['coffee']}g")
    print(f"money :  ${money}")

# TODO : function -check resources are sufficient 

def check_resources(type):
    msg=[]
    full_ingredient= menu[type]["ingredients"]
    if resources["water"]<full_ingredient["water"]:
        msg.append("Sorry there is not enough water.")
    if resources['milk']<full_ingredient["milk"]:
        msg.append("Sorry there is not enough milk.")
    if resources['coffee']<full_ingredient["coffee"]:
        msg.append("Sorry there is not enough coffee.")
    return msg
    
    
# TODO : function -check coins are sufficient 
def check_money(money_list,type):
    
    total=money_list[0]*0.25+money_list[1]*0.1+money_list[2]*0.05+money_list[3]*0.01
    
    if total<menu[type]['cost']:
        return total-menu[type]['cost']
    else:
        return total-menu[type]['cost']
    

# TODO : function - collect coins
def collect_coins():
    coins=[]
    print("Please insert coins.")
    coins.append(int(input("how many quarters?: ")))
    coins.append(int(input("how many dimes?: ")))
    coins.append(int(input("how many nickles?: ")))
    coins.append(int(input("how many pennies?: ")))
    return coins

# ToDO - Reduce resources
def reduce_resources(type):
    resources["milk"]=resources["milk"]-menu[type]["ingredients"]["milk"]
    resources["water"]=resources["water"]-menu[type]["ingredients"]["water"]
    resources["coffee"]=resources["coffee"]-menu[type]["ingredients"]["coffee"]

    
    
while True:
    key_word=input('What would you like? (espresso/latte/cappuccino): ')
    type=""
    if key_word=="espresso" or key_word=="latte" or key_word=="cappuccino":
        type=key_word
        if len(check_resources(type))==0:
            money_check=check_money(collect_coins(),type)
            print(money_check)
            if  money_check>0:
                print(f'Here is ${money_check} in change')
                print(f'Here is your {type} ☕️. Enjoy!')
                reduce_resources(type)
                money+=menu[type]['cost']
            if  money_check==0:
                print(f'Here is your {type} ☕️. Enjoy!') 
                money+=menu[type]['cost']
                reduce_resources(type)
            if  money_check<0:
                print("Sorry that's not enough money. Money refunded.") 
        else:
            for msg in check_resources(type):
                print(msg)
                
    if key_word=="off":
        break
    if key_word=="report":
        print_report()