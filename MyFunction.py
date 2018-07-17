

def my_function(str1, str2):
    print(str1)
    print(str2)

def my_function2(int1,int2):
    print(int1+int2)

#function with default arguments
def print_something(name = "Someone",age = "Unknown"):
    print("My name is",name,"and my age is",age)

#Keyword arguments
print_something(age = 27)
print_something(name = "Joana")

print_something("João",31)

my_function("This is arg 1","This is arg 2")
my_function("Hello","World")
my_function2(5,5)