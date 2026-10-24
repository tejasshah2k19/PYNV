list = []  #ordered 

tuple = () #ordered 

a = (10,20,30,40,50)
#mix data types 

#index 
print(a[0])

#slicing 
print(a[0:3])

#tuple is immutable 
#you can not change , add or remove any single element from tuple after creation. 

#count()
#index()
#len()
#max()
#min()


###set###
#collection of unique elements. 
#does not support indexing. 

set = {}
odd = {1,3,5,7,9,1}

print(odd) #1 3 5 7 9  -> order is not guaranteed 

list = [13,15,17]

odd.add(11)
odd.update(list) #1 3 5 7 9 11 13 15 17 

odd.remove(11) #if 11 not present then you will get exception -> KeyError 
odd.discard(10) #if present remove it if not do nothing 


### set operations ### 

A = {1,2,3,4,5}
B = {3,4,5,6}

#union 
print(A.union(B)) # 1 2 3 4 5 6 
#intersection 
print(A.intersection(B)) #3 4 

#difference 
print(A.difference(B)) #A-B 1 2 

#symmetric difference 
print(A.symmetric_difference(B))#1 2 5 6 



#add
#update 
#remove-> KeyError 
#discard -> 
#union
#intersection
#difference 
#symmertricdifference
#issubset

print(A.issubset(B)) #False 
print(A.issuperset(B)) #False 
A.clear()



#disctionary 
# key:value

student = {
    "name":"rock",
    "age":35,
    "salary":152432
}

print(student)
print(student.get("name"))
print(student["name"])  #raises a KeyError 
print(student.get("name1")) #None 
print(student.get("name1","Not Found"))

student["city"] = "LA"

student.pop("city")

# student.clear()

print(student.keys())
print(student.values())
print(student.items())





students = {
    
    101:{
    "name":"rock",
    "age":35,
    "salary":152432
    },
    102:{
        "name":"jack",
        "age":21,
        "salary":15000
    }
}


print(student.get(101))






