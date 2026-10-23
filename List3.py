a = [10,20]
b = [30,40]
c = a + b  #concatenation 
print(c)

a = [1,2]
b = a*3 
print(b)

a = [10,20]
b = [30,40]
c = [10,20]

print(a == b)
print(a == c)

#is 


#matrix 
#list inside list 

arr = [
    [10,20,30],
    [40,50,60],
    [70,80,90]  
] 
print(arr)

print(arr[0]) # 10 20 30 
print(arr[0][0]) # 10 

for row in arr:
    for col in row: 
        print(col,end=" ")
    print("")
    

list = [1,2,3,4,5]

#1 4 9 16 25 

sqr = []
for n in list:
    sqr.append(n*n)
print(sqr)


sqr = [n * n for n in list]


#linear search 
#[10 20 30 40 50] : 5   
#[10 20 30 40 50 55 66 33 11 99 ] : 10 
#input size -> n 
#O(n)

#n=5
#O(n*n) #25 


#list[3] 4 1 10 ==> O(1) constant 
#update by index : O(1)
#append  => O(1)
#insert at beginning => O(n)
#removing beg => O(n)
#search => O(n)
#count  => O(n)


