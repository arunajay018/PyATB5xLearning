#cannot return anything
#no return type and no paramaters

def greet():
    print("hello")

greet()

#no return type but with argument

def greet(name):
    print("hello", name)

greet("arun")

# no return type with default argument

def greet(name="ARUN"):
    print("name is ",name.lower())

greet()
greet("PRAMOD")

#we can multiple arguments also

def greet(name="ARUN",age=27):
    print("name is ",name.lower(),"with age",age)

greet()
greet("aRuN",40)
greet("pramod")
greet(age=33)

#Argument with return type

def sum(a,b):
    return a+b

result = sum(3,4)
print(result)

def sum1(a=7,b=8):
    return a+b

result = sum1()
result1 = sum1(11,22)
print(result)
print(result1)


#

