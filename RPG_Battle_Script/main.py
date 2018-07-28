from Classes.game import Person, bcolors

#list of dictionaries whit the attacks name, cost and damage
magic = [{"name":"Fire","cost":10,"dmg":100},
         {"name":"Thunder","cost":12,"dmg":124},
         {"name":"Blizzard","cost":10,"dmg":100}
         ]

#one player instantiated whit health points, magic points, attack points, defense power and magic spells       
player = Person(460,65,60,34,magic)

enemy = Person(1200,65,45,25,magic)

running = True
i = 0

print(bcolors.FAIL + bcolors.BOLD + "AN ENEMY ATTACKS!" +bcolors.ENDC)

while running:
    print("============================================")
    player.choose_action()
    choice = int(input("Choose Action :")) - 1  #to get the correct action in the list we have to subtract 1

    if choice == 0:
        dmg = player.generate_damage()
        enemy.take_damage(dmg)
        print("You attacked for", dmg, "points of Damage")
    elif choice == 1:
        player.chose_spell()
        magic_choice = int(input("Chose Magic : ")) - 1
        magic_dmg = player.generate_spell_damage(magic_choice)
        spell = player.get_spell_name(magic_choice)
        cost = player.get_spell_mp_cost(magic_choice)

        current_mp = player.get_mp()

        if cost > current_mp:
            print(bcolors.FAIL +"\nNot enough MP \n" +bcolors.ENDC)
            continue
        player.reduce_mp(cost)
        enemy.take_damage(magic_dmg)
        print(bcolors.OKBLUE+"\n"+ spell+" deals "+str(magic_dmg),"points of Damage"+bcolors.ENDC)


    enemy_choice = 1

    enemy_dmg = enemy.generate_damage()
    player.take_damage(enemy_dmg)
    print("Enemy attacks for", enemy_dmg, "points of Damage.")

    print("============================================")
    print("Enemy HP : " + bcolors.FAIL+str(enemy.get_hp())+"/"+str(enemy.get_max_hp())+bcolors.ENDC+"\n")
    print("Your HP : " + bcolors.OKGREEN+str(player.get_hp())+"/"+str(player.get_max_hp())+bcolors.ENDC+"\n")
    print("Your MP : " + bcolors.OKBLUE+str(player.get_mp())+"/"+str(player.get_max_mp())+bcolors.ENDC+"\n")




    if enemy.get_hp() == 0:
        print(bcolors.OKGREEN + "You Win!" + bcolors.ENDC)
        running = False
    elif player.get_hp() == 0:
        print(bcolors.FAIL + "Your enemy has defeated you!" + bcolors.ENDC)
        running = False

