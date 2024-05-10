
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def encrypt(test,shift):
    encrypt_alphabet=alphabet[shift:]+alphabet[0:shift]
    
    new_test=""
    for letter in test:
        new_test += encrypt_alphabet[alphabet.index(letter)]
    return new_test

def decrypt(test,shift):
    decrypt_alphabet=alphabet[shift:]+alphabet[0:shift]
    
    new_test=""
    for letter in test:
        new_test += alphabet[decrypt_alphabet.index(letter)]
    return new_test


again=True

while again:
    type=input("Type 'encode' to encrypt, type 'decode' to decrypt : ")
    test=input("Type your message : ").lower()
    shift=int(input("Type the shift number : "))
    
    if type=="encode":
        print(f"Encrypted text is {encrypt(test,shift)}")
    elif type=="decode":
         print(f"Decrypted text is {decrypt(test,shift)}")
    else:
        print("wrong input")
        break
        
    want_continue=input("Do you want to continue")
    
    if want_continue=="No":
        again:False
        
            
        







