import random


#simple class example
class Enemy:

    #every enemy has a hp of 200
    hp = 200

    #runs when the class is been instantiated or when the object is created
    def __init__(self, atkl, atkh):
        self.atkl = atkl
        self.atkh = atkh

    def getAtkl(self):
        print("Atack is",self.atkl)

    def getAtkh(self):
        print("Atack is",self.atkh)

    def getHp(self):
        print("Hp is",self.hp)
    
#instantiates the class 
#2 enemies with diferent attacks
enemy1 = Enemy(40,49)
enemy1.getAtkh()
enemy1.getAtkl()
enemy1.getHp()

enemy2 = Enemy(75,90)
enemy2.getAtkh()
enemy2.getAtkl()
enemy2.getHp()

playerhp = 260 #player health points
enemytkl = 60 #enemy attack low
enemytkh = 80 #enemy attack high

while playerhp > 0:
    #damage
    dmg = random.randrange(enemytkh,enemytkh) #generates a random number between the range
    playerhp = playerhp - dmg

    if playerhp <= 30:
        playerhp = 30

    print("Enemy strikes for",dmg,"point sof damage. Current HP is",playerhp)

    if playerhp == 30:
        print("You have low health. You've been transported to the nearest inn")
        break #to stop the loop, otherwise it's an infinite loop
