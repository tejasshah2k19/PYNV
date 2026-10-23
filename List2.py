#list 
#ordered mutable collection 
#maintain position 
#duplicate allowed 
#mixed data type 

list = [10,4,52,63,9] #0 1 2 3 4  #sort:asc desc #random 

print(list) #10 4 52 63 9 

list.insert(2,600) #10 4 600 52 63 9 
print(list)


# x = []
# list()




list = [10,4,52,63,9] #0 1 2 3 4 #order:position  #sort:asc desc #random 
list[0] = 1000
print(list) #1000 4 52 63 9 

#slicing [start:stop:step]


#append(50) #add the new element at the end of the list  -- single item 

#extend() 
list2 = [66,99,88]

list.extend(list2)
print(list)


#add the item at given index 
list.insert(2,2000)


#remove by value 
list.remove(2000)

#remove by index and return that value pop()
ans = list.pop(0) #0th index will remove and return 
ans = list.pop()  #it will remove last 

#del list 

list.clear() #remove all the items from the list 


print(5000 in list)


#time complexity 
#O(n)


fruits = ["Apple","Banana","Mango"]

print(fruits)


for fruit in fruits:
    print(fruit)

for i in range(0,len(fruits)):
    print(fruits[i])



# print(min(list))
#max sum len 


list = [23,45,67,87,65]
print(list)
list.sort()
print(list)



list = [23,45,67,87,65]
print(list)
list.sort(reverse=True)
print(list)

#new list => sort and return new list 

list = [23,45,67,87,65]

sorted_list = sorted(list)

print(list) #23 45 67 87 65 
print(sorted_list) #23 45 65 67 87


list = [23,45,67,87,65]
list.reverse()
print(list)

list = [23,45,67,87,65,23]

print(list.count(23))# 2 
print(list.count(230))# 0 

#return index 
print(list.index(23))
print(list.index(230)) #ValueError 

