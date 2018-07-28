from Classes.game import Person, bcolors

#list of dictionaries whit the attacks name, cost and damage
magic = [{"name":"Fire","cost":10,"dmg":60},
         {"name":"Thunder","cost":10,"dmg":80},
         {"name":"Blizzard","cost":10,"dmg":60}
         ]

#one player instantiated whit health points, magic points, attack points, defense power and magic spells       
player = Person(460,65,60,34,magic)

enemy = Person(1200,65,45,25,magic)

running = True
i = 0

print(bcolors.FAIL + bcolors.BOLD + "AN ENEMY ATTACKS!" +bcolors.ENDC)

while running:
    print("===================================")
    player.choose_action()
    choice = input("Choose Action :")
    index = int(choice)-1 #to get the correct action in the list

    if index == 0:
        dmg = player.generate_damage()
        enemy.take_damage(dmg)
        print("You attacked for", dmg, "points of damage. Enemy HP :",enemy.get_hp())
    
    enemy_choice = 1

    enemy_dmg = enemy.generate_damage()
    player.take_damage(enemy_dmg)
    print("Enemy attacks for", enemy_dmg, "points of damage. Player HP :",player.get_hp())

    if enemy.get_hp() == 0:
        print(bcolors.OKGREEN + "You Win!" + bcolors.ENDC)
        running = False
    elif player.get_hp() == 0:
        print(bcolors.FAIL + "You Lose!" + bcolors.ENDC)
        running = False

