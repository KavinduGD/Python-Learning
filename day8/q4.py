print("================Motivation================== \n ")

print("Do you wanner try this or not")
print("This will be hard \n  ")

want_to_continue=input("So tell me ?. Just press 'y'")

target=0

while(want_to_continue=="y"):
    target+=1
    if target==1:
        print("Ok, don't worry about others, You go your own pace")
    elif target==32:
        print("tou just really work one day be proud about your self. But go on")
    elif target==3:
        print("Ok, You are trying, It all matters")
    elif target==4:
        print("Notice any diffrent. Somethings chaing right ?")
    elif target==5:
        print("Ok, Now you knopw what to speed thing little more")
    else :
        print("You achive your gaol")
    
    if target==6:
        break
    
    want_to_continue=input("Feeling tired right? Don't give up. Just have to press 'y'")


if target<6:
    print("You suck")