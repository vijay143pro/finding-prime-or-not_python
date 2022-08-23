num=int(input("Enter the number"))
flag=False
if(num>=1):
    for i in range(2,num):
        if(num%i==0):
            flag=True
            

if(flag==True):
    print(num,"The given number is not prime")
else:
    print(num,"The given number is prime")
