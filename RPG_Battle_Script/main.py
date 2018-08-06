from Classes.game import Person, bcolors
from Classes.magic import Spell
from Classes.inventory import Item
import random


"""
player_name = input("Insert your Name :")
if len(player_name) > 10111:
    while len(player_name)>10:
        player_name = input("Insert your Name :")
white_space = " "
"""


# Black Magic
fire = Spell("Fire", 10, 100, "black")
thunder = Spell("Thunder", 10, 100, "black")
blizzard = Spell("Blizzard", 10, 100, "black")
quake = Spell("Quake", 12, 120, "black")
meteor = Spell("Meteor", 20, 200, "black")

# White Magic
cure = Spell("Cure", 12, 120, "white")
cura = Spell("Cura", 18, 200, "white")

'''
#Old Logic
#list of dictionaries whit the attacks name, cost and damage
magic = [{"name":"Fire","cost":10,"dmg":100},
         {"name":"Thunder","cost":12,"dmg":124},
         {"name":"Blizzard","cost":10,"dmg":100}
         ]
'''

# Create some Items
potion = Item("Potion", "potion", "Heals 50 HP.", 50)
hipotion = Item("Hi-Potion", "potion", "Heals 100 HP.", 100)
superpotion = Item("Super Potion", "potion", "Heals 500 HP.", 500)
elixir = Item("Elixir", "elixir",
              "Fully restores HP/MP of one party member.", 9999)
megaelixir = Item("Mega Elixir", "elixir",
                  "Fully restores party's HP/MP.", 9999)

grenade = Item("Grenade", "attack", "Deals 500 damage HP.", 500)

player_spells = [fire, thunder, blizzard, meteor, cure, cura]
player_items = [{"item": potion, "quantity": 15}, {"item": hipotion, "quantity": 5},
                {"item":  superpotion, "quantity": 5}, {
                    "item": elixir, "quantity": 5},
                {"item": megaelixir, "quantity": 5}, {"item": grenade, "quantity": 5}]

# Players instantiated whit health points, magic points, attack points, defense power and magic spells
player1 = Person("PL1", 3400, 150, 60, 34, player_spells, player_items)
player2 = Person("PL2", 4000, 170, 60, 34, player_spells, player_items)
player3 = Person("PL3", 3200, 120, 60, 34, player_spells, player_items)

players = [player1, player2, player3]

enemy = Person("CPU-1", 11000, 250, 450, 25, [], [])

running = True
i = 0

separator = "="*70

print(bcolors.FAIL + bcolors.BOLD + "AN ENEMY ATTACKS!" + bcolors.ENDC)

while running:
    print(separator)
    for player in players:
        print("\n")
        player.get_player_stats()
    print("\n")
    enemy.get_enemy_stats()
    for player in players:
        print("\n")
        player.get_player_stats()
        player.choose_action()
        # to get the correct action in the list we have to subtract 1
        choice = int(input("Choose Action :")) - 1

        if choice == 0:
            dmg = player.generate_damage()
            enemy.take_damage(dmg)
            print("You attacked for", dmg, "points of Damage")
        elif choice == 1:
            player.choose_magic()
            magic_choice = int(input("Chose Magic : ")) - 1
            if magic_choice == -1:
                continue

            spell = player.magic[magic_choice]
            magic_dmg = spell.generate_damage()

            current_mp = player.get_mp()

            if spell.cost > current_mp:
                print(bcolors.FAIL + "\nNot enough MP \n" + bcolors.ENDC)
                continue
            player.reduce_mp(spell.cost)

            if spell.type == "white":
                player.heal(magic_dmg)
                print(bcolors.OKBLUE+"\n" + spell.name +
                      " heals for "+str(magic_dmg), "HP."+bcolors.ENDC)
            elif spell.type == "black":
                enemy.take_damage(magic_dmg)
                print(bcolors.OKBLUE+"\n" + spell.name + " deals " +
                      str(magic_dmg), "points of Damage"+bcolors.ENDC)
        elif choice == 2:
            player.choose_items()
            item_choice = int(input("Chose Item : ")) - 1
            if item_choice == -1:
                continue

            item = player_items[item_choice]["item"]
            if player_items[item_choice]["quantity"] == 0:
                print(bcolors.FAIL+"\n" + " None Left...  " +
                      bcolors.ENDC)
                continue
            player_items[item_choice]["quantity"] -= 1

            if item.type == "potion":
                player.heal(item.prop)
                print(bcolors.OKGREEN+"\n" + item.name +
                      " heals for "+str(item.prop), " HP."+bcolors.ENDC)
            elif item.type == "elixir":
                if item.name == "megaelixir":
                    for player in players:
                        player.hp = player.maxhp
                        player.mp = player.maxmp
                else:
                    player.hp = player.maxhp
                    player.mp = player.maxmp
                print(bcolors.OKGREEN+"\n" + item.name +
                      " Fully Restored HP/MP  " + bcolors.ENDC)
            elif item.type == "attack":
                player.take_damage(item.prop)
                print(bcolors.FAIL+"\n" + item.name + " deals  " +
                      str(item.prop), " points of damage." + bcolors.ENDC)

    enemy_choice = 1
    target = random.randrange(0, 3)

    enemy_dmg = enemy.generate_damage()
    players[target].take_damage(enemy_dmg)
    print("Enemy attacks for", enemy_dmg, "points of Damage.")

    print(separator+"\n")

    if enemy.get_hp() == 0:
        print(bcolors.OKGREEN + "You Win!" + bcolors.ENDC)
        running = False
    elif player.get_hp() == 0:
        print(bcolors.FAIL + "Your enemy has defeated you!" + bcolors.ENDC)
        running = False
    print("\n"+separator+"\n")
