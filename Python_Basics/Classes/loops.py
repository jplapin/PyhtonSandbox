numbers = [1,2,3,4,5]
pessoas = ["joao","joana","Maria","Manuel"]

for item in numbers:
    print(item)


for pessoa in pessoas:
    print(pessoa)

run = True
current = 1

while run:
    if current ==100:
        run = False
    else:
        print(current)
        current +=1