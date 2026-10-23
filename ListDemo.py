#list 
#[ ]  #dynamic array 

a = 10
print(type(a))  #<int>

a = [10]
print(type(a))


a.append(12)
a.append(13)
a.append(12)

print(a) #10 12 13 12 

print(a[0]) #10 

print(a[-1])#12 

print(a[0:2]) #0 1

print(a[::]) 


a = [10,20,30,40,50,60,70,80,90,100]
print(a[0:2]) # 0 1 
print(a[::]) #all 
print(a[4:]) # 4 to end 
print(a[:4]) #0 to 3 

print(a[::2]) #all 
print(a[::-1]) #all 


#array 
