import re

print("Magical Calculator")
print("Type 'quit' to exit\n")

previous = 0
run = True

def performMath():
    global run #to get the value of the global variable run
    global previous
    equation = ""
    if previous == 0:
        previous = input("Enter Equation: ")
    else:
        equation = input(str(previous))
    if(equation == 'quit'):
        print("Goodbye, human!")
        run = False
    else:
        equation = re.sub('[a-zA-Z,.:()" "]','',equation)
        if previous == 0:
            previous = eval(equation)
        else:
            previous = eval(str(previous)+equation)
        

while run:
    performMath()