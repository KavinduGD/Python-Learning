import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

user_input=int(input("enter a input"))

user=""

if user_input==0:
    user="R"
    print(rock)
elif user_input==1:
    print(paper)
    user="P"
else :
    print(scissors)
    user="C"

pc_input=random.randint(0,2)

pc=""

if pc_input==0:
    pc="R"
    print(rock)
elif pc_input==1:
    print(paper)
    pc="P"
else :
    print(scissors)
    pc="C"


win_list=["RC","PR","CP"]
loss_list=["RP","PC","CR"]

check=user+pc

print(check)

if check in win_list:
    print("You win")


if check in loss_list:
    print("You loose")
