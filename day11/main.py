import random

def deal_card():
    """returns a random card from the deck"""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    return random.choice(cards)

def calculate_score(cards):
    """take a list of card and return the sum"""
    if sum(cards)==21 and len(cards)==2:
        return 0
    if 11 in cards and sum(cards)>21:
        cards.remove(11)
        cards.append(1)  
    return sum(cards)

def compare(user_score,computer_score):
    if user_score == computer_score:
        return "Draw "
    elif computer_score==0:
        return "Lose, opponent has Backjack"
    elif user_score==0:
        return "Win with a Blackjack"
    elif user_score>21:
        return "You want over 21, You loose"
    elif computer_score>21:
        return "Computer went over, You win"
    elif user_score > computer_score:
        return "You win by over"
    else:
        return "You loose you low"
    
user_cards = []
computer_cards = []
is_game_over=False

for _ in range(2):
    user_cards.append(deal_card())
    computer_cards.append(deal_card())


while is_game_over==False:
    user_score=calculate_score(user_cards)
    computer_score=calculate_score(computer_cards)

    print(f"Your cards {user_cards}, current score {user_score}")
    print(f"computer's first card [{computer_cards[0]}]")

    if user_score ==0 or computer_score==0 or user_score>21:
        is_game_over=True
    else:
        if input("Type 'y' to get another card Type 'n' to pass - " ) =="y":
            user_cards.append(deal_card())
        else:
            is_game_over=True
            
while computer_score!=0 and computer_score < 17:
    computer_cards.append(deal_card())   
    computer_score=calculate_score(computer_cards)

print(compare(user_score,computer_score))