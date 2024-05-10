stages = [r'''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', r'''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', r'''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', r'''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', r'''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', r'''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', r'''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

logo = r''' 
 _                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/   
'''
                   
import random as rm
import os

def clear_console():
    # For Windows
    if os.name == 'nt':
        _ = os.system('cls')
    # For Unix/Linux/MacOS
    else:
        _ = os.system('clear')
        
        
word_list = ["aardvark", "baboon", "camel"]
selected_word=word_list[rm.randint(0,len(word_list)-1)]


lives=6
right=len(selected_word)
right_gueses=7
display_word=[]      

for letter in selected_word:
    display_word.append("_")

print(logo)
print(" ".join(display_word) )

while(lives>0 and right_gueses<right):
    
    letter=input("Enter a Letter - ").lower()
    clear_console()
    has_letter=False
    
    letter_in_here=False
    index=0
    
    for item in selected_word:
        if item==letter:
            display_word[index]=letter+" " 
            letter_in_here=True   
            right_gueses+=1
        index +=1
    
    if not letter_in_here  :
        lives-=1
    
    print(" ".join(display_word))  
    print(stages[lives+1])     
    
if(lives==0):
    print("You Loose")

if right==right_gueses:
    print("You save me cunt")
