num=int(input("Enter the number "))

for i in range(2,num):
    if num%i==0:
        print("Number is not  Prime ")
        break
        
else:
    print("Number is  Prime")
    
    
if num%2==0:
    print("Number is EVEN")
    
else:
    print("Number  is ODD ")