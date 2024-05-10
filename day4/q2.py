import random

friends_string=input("Enter the name - ")

names=friends_string.split(",")





print(f"Oh unluck! You should pay the whole price {names[random.randint(0,len(names)-1)]}")