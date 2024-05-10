def prime_check(n):
    count=0
    
    for i in range(1,n+1):
        if(n%i==0):
            count+=1
    
    if count > 2:
        print("This is not a prime number")
    else:
        print("This is a Price number")
            

prime_check(10)