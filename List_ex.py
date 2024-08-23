# Create 2 lists from a given list where
# 1st list will contain all the odd numbers from the original list and
# the 2nd one will contain all the even numbers

'''

lst1=[]
lst2=[]
num=int(input("Enter the range do you went number "))

for i in range(num+1):
    if i%2==0:
        lst1.append(i)
        
    else:
        lst2.append(i)
        
num2=int(input("what do list are print  1=odd  and 2=even"))

if num2==1:
    for i in lst2:
        print(i)
        
else:
    for i in lst1:
        print(i)
'''


# How to take list as input from user

'''
lst=[]

num=int(input("Enter the size of list "))
print("enter the values")
for i in range(num):
    lst.append(int(input()))
    
print(lst)

'''


# Write a program to merge 2 list without using the + operator
# L1 = [1,2,3,4]
# L2 = [5,6,7,8]


'''
L1 = [1,2,3,4]
L2 = [5,6,7,8]

L3=L1+L2

print(L3)
'''

# Write a program to replace an item with a different item if found in the list
# L = [1,2,3,4,5,3]
# replace 3 with 300
'''

L = [1,2,3,4,5,3]

for i in L:
    if i==3:
        x=L.index(i)
        L[x]=300
print(L)
        
        '''
        
# Write a program that can convert a 2D list to 1D list
'''
lst=[[2,23,35,32],
     [2,65,24,55]
     ]

lst1=[]

for i in range(2):
    for j in range(4):
        lst1.append(lst[i][j])

print(lst1)
'''

# Write a program to remove duplicate items from a list
'''L = [1,2,1,2,3,4,5,3,4]


for i in range(len(L)):
    for j in range(len(L)-1):
        if i==j:
            
            L.pop(L[i])
            break
        
print(L)'''


# Write a program to check if a list is in ascending order or not


lst=[1,5,6,2,4,9,1,6,11,61,20]
    
if lst==lst.sort():
    print("list is ascending order")
    
else:
    print("list is not  ascending order")
    
           

