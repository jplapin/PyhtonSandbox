

def my_function(str1, str2):
    print(str1)
    print(str2)

my_function("This is arg 1","This is arg 2")
my_function("Hello","World")

def my_function2(int1,int2):
    print(int1+int2)

my_function2(5,5)

#function with default arguments
def print_something(name = "Someone",age = "Unknown"):
    print("My name is",name,"and my age is",age)

#passing all args
print_something("João",31)

#Keyword arguments
print_something(age = 27)
print_something(name = "Joana")

#infinite (or flexible) arguments
def print_people(*people):
    for person in people:
        print("This person is",person)

print_people("João","Joana","Maria","Manuel","Fernando")

#Return a value in a function
def do_math(num1,num2):
    return num1+num2

math1 = do_math(5,7)
math2 = do_math(11,34)

print("First sum is", math1,"and the second sum is",math2)
