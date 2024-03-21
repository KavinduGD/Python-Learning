print("welcome to the rollercoaster")
h=int(input("please enter your height- "))

if h>=120:
    age=int(input("So please enter your age- "))
    if age >=18:
        print("Pay 20")
    elif age>=12:
        print("pay 16")
    elif age>=4:
        print("Pay 12")
    else:
        print("Babies can't ride this")
    
else:
    print("Your not allowed because your height is less than 120cm")


