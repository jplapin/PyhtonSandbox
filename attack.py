import random


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
