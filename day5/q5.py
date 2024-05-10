import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

if nr_letters<nr_numbers+nr_symbols:
    print("Two many sysmbols and numbers than whole passwords")

numbers_list=[]
if nr_letters>0:
    for  item in random.sample(range(0,len(numbers)),nr_numbers):
        numbers_list.append(numbers[item])

symbols_list=[]
if nr_symbols>0:
    for item in random.sample(range(0,len(symbols)),nr_symbols):
         symbols_list.append(symbols[item])


letters_list=[]
if nr_letters!=nr_symbols+nr_numbers:
    for item in random.sample(range(0,len(letters)),nr_letters-(nr_symbols+nr_numbers)):
        letters_list.append(letters[item])
        


end_list=numbers_list+symbols_list+letters_list

mix_order=random.sample(range(0,nr_letters),nr_letters)

result=[None]*nr_letters

for index,item in enumerate(mix_order):
    result[item]=end_list[index]
    
    
last_pass=''.join(result)
print(last_pass)




    
