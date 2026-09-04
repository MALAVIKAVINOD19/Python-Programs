num = (int(input("Enter a number: ")))
prime = True
if num<=1:
     print("Not a prime number.")  
else:
    print("A prime number.")
    for i in range(2,num):
        if (num % i) == 0:
            prime=False 
            break
    if prime:
        print("Prime number")
    else:
        print("Not a prime number.")