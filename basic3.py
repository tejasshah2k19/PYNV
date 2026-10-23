
def add():
    print("add")
#positional argment     
def sub(a,b):
    print(a-b)

def add(a,b):
    print(a+b)
    
#default argument     
def mul(a=5,b=5):
    print(a*b)
    
mul(9,6) # 9*6
mul(9) #   9*5
mul() #5*5 


# def div(a=5,b):
#     print(a/b)

def div(a,b,c=10,d=5,e=10):
    pass 


# add()
mul(10,2)
mul(10)

#return 

def sqr(num):
    return num*num

print(sqr(5))

#python can return multiple values 

def calculate(a,b):
    return a+b,a-b,a*b
    

add,sub,mul = calculate(10,5)
print(add)
print(sub)
print(mul)

#keyword argument 
def calc(a,b,c):
    print(a) #10
    print(b) #5
    print(c) #4
    print(a+b+c)

#positional argment 
calc(10,5,4) # 14 

#keyword / name  arg  
calc(a=10,c=5,b=9)


x = 100
y = 1000 
def myFun():
    x = 500
    print(x) #500 
    print(y) #1000 

myFun()


#global 
#self 
