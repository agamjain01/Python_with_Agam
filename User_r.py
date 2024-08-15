# Create a program to describe. A human in nested if 
# Example 
# If boy 
#    If 18+
#     If job 
#       Print u known your responsibility and doing good for your future 
#     Else 
#      U should job 

#   Else u should study  hard for your future
# Elif girl  If 18+
#     If job 
#       Print u known your responsibility and doing good for your future 
#     Else 
#      U should job 

#   Else 
# u should study  hard for your future


print("Enter your details ")

Gen=str(input("Enter  your Gander"))

Age=int(input("Enter  your Age"))

Job=str(input("you have a job or not"))


if Gen=="Boy":
    if Age ==18:
        if Job=="yes":
            print("YOu known your responsibility and doing good for your future ")
        
        else:
            print("You Should Job")
        
    else:
         print("You should study  hard for your future")
else:
    if Age==18:
        if Job=="yes":
            print("YOu known your responsibility and doing good for your future ")
        else:
            print("You Should Job")
            
    else:
         print("You should study  hard for your future")
            
     
        
