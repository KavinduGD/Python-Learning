import random
import gamedata
import os

#clean the screen
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')


#fuction to generate random item  in the   list
def random_item():
    return random.choice(gamedata.data)

#function to generate a random item other than provided parameter
def random_item_without_selected_item (selected_dic):
    while True:
        new_dic=random.choice(gamedata.data)
        if new_dic != selected_dic:
            return new_dic


def play_game():  
    first_item=random_item()
    correct_answer_count=0

    while True:
    
        if correct_answer_count>0:
            first_item= second_item
            print(f'you got {correct_answer_count} answers right')
            
            
        second_item=random_item_without_selected_item(first_item)
        
        print(f"Compare A:{first_item['name']}, a {first_item['description']} , from {first_item['country']}")
        print('vs')
        print(f"Compare B:{second_item['name']}, a {second_item['description']} , from {second_item['country']}")
        answer=input('Who has more followers? Type "A" or "B": ').lower()
        
        if first_item['follower_count']>second_item['follower_count']:
            correct_answer = 'a'
        else:
            correct_answer="b"
        
        print(answer,correct_answer)
        
        if correct_answer==answer:
            correct_answer_count+=1
            clear_screen()
        else:
            clear_screen()
            break


    print(f'you got {correct_answer_count} answers right')


        
play_again=True        
while play_again:
    play_game()
    answer=input('do you want to play again : "Y" ot "N": ').lower()
    if answer=='n':
        play_again=False
    clear_screen()
   
         
        



