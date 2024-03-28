import os

def addtion(n1,n2):
    
    return n1+n2

def subtraction(n1,n2):
    return (n1-n2)

def mutipication(n1,n2):
    return n1*n2

def division(n1,n2):
    return n1/n2

print("===============Calculator==============\n")

fist_number=None

while True:
    if fist_number==None:
        fist_number=int(input("enter the first number - "))
    else:
        operator=input("What is the operator - ")
        another_number=int(input("Enter another number - "))
        
        if operator=="+":
            fist_number=addtion(fist_number,another_number)
        elif operator=="-":
            fist_number=subtraction(fist_number,another_number)
        elif operator=="*":
            fist_number=mutipication(fist_number*another_number)
        else :
            fist_number=division(fist_number,another_number)
                
        print(f"Here is the result {fist_number}")
        
        again=input("Do you want to continue - ")
        
        if again=="n":
            fist_number=None
            os.system('cls' if os.name == 'nt' else 'clear')
            
            
    
