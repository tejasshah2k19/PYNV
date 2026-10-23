#variable 
#data type
#python --> 



a = 10 # int 


a  = 20.20  # float 


a  = 'royal' #string  

b = 12 
print(b)

#a z AZ 09 _ 
#keywords 
#space special symbols 

#arithmetic
# + - / *  %  ** //   


ans = 5 / 2 
print(ans)

# int / int => int 
# 2.5 => 2 

ans = 5 // 2 
print(ans)


#comparison 
# == != > < >= <= 

#assignment 
# x = x+1 
# x +=1 

 
#logical 
#c1 and c2 
#and or not 


#membership 
#in -> element exists   ---> True 
#not in -> element does not exists -> True 

#boolean -> True  False 
#no  0 and 1 

arr = [10 ,20,30 ,40,50]  #list 

print(30 in arr) #True 
print(305 in arr) #False 
 
#identity operators 

arr = [10 ,20,30 ,40,50]  #list 
arr2 = arr 
arr3 = [10 ,20,30 ,40,50]  #list 

print(arr == arr3) #True 
print(arr is arr3) #False
print(arr is not arr3) #True
print(arr is arr2)#True 

# == 
#equals() 
#instanceof 




#if 
#if else 
#elif 

#switch 
#match 

a = 10 

if a > 0 :
    pass


if a > 0 :
    print("+")
else:
    print("-")
    
    
if a > 0 :
    print("+")
elif a < 0:
    print("-")
else:
    print("0")
    

#python 3.10 
choice =  3 

match choice:
    case 1:
        print("one")
    case 2:
        print("two")
    case _: 
        print("Default")
        

#####loops###### 

#for
#while 
 
# print("%%%%%%%%%%%%%%%%%%%%%%") 
# for i in [1,2,3,4,5]:
#     print(i) 
    
    

print("%%%%%%%%%%%%%%%%%%%%%%") 
for i in range(5):
    print(i) #0 1 2 3 4 
    
for i in range(5,11):
    print(i) #5 6 7 8 9 10


for i in range(5,11,2):
    print(i) #5 7 9 

for i in range(10,0,-1):
    print(i) #10 9 8 7 6 5 4 3 2 1    
    
    
arr = [10 ,20,30 ,40,50]  #list 

for data in arr:
    print(data) #10 20 30 40 50 


for i in range(1,6):
    print("Enter two numbers")
    n1 = int(input())
    n2 = int(input())
    ans = n1 + n2 
    print("addition : ",ans)


###############while##################

i = 1 

while i<=5:
    if i%2 == 0:
        continue 
    print(i)#1 
    i+=1  

#do we have break and continue? 
#yes 
#break will terminate the loop 
#continue will skip the current iternation.

