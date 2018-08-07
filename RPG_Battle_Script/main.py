from Classes.game import Person, bcolors
from Classes.magic import Spell
from Classes.inventory import Item
import random


def battle_status(num_enemies_defeated, num_players_defeated):
    running = True
    # check if player won
    if num_enemies_defeated == 2:
        print("\n"+separator+"\n")
        print(bcolors.OKGREEN + "You Win!" + bcolors.ENDC)
        running = False
        print("\n"+separator+"\n")
        return running
    # check if enemy won
    elif num_players_defeated == 2:
        print("\n"+separator+"\n")
        print(bcolors.FAIL + "Your enemies have defeated you!" + bcolors.ENDC)
        running = False
        print("\n"+separator+"\n")
        return running
    else:
        return running



# Black Magic
fire = Spell("Fire", 10, 100, "black")
thunder = Spell("Thunder", 10, 100, "black")
blizzard = Spell("Blizzard", 10, 100, "black")
quake = Spell("Quake", 12, 120, "black")
meteor = Spell("Meteor", 20, 200, "black")

# White Magic
cure = Spell("Cure", 12, 120, "white")
cura = Spell("Cura", 18, 200, "white")
curaga = Spell("Curaga", 50, 6000, "white")

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
enemy_spells = [fire, meteor, cure, curaga]
player_items = [{"item": potion, "quantity": 15},
                {"item": hipotion, "quantity": 5},
                {"item":  superpotion, "quantity": 5},
                {"item": elixir, "quantity": 5},
                {"item": megaelixir, "quantity": 5},
                {"item": grenade, "quantity": 5}
                ]

# Players instantiated with health points, magic points, attack points, defense power and magic spells
player1 = Person("Player 1", 3400, 150, 60, 34, player_spells, player_items)
player2 = Person("Player 2", 4000, 170, 60, 34, player_spells, player_items)
player3 = Person("Player 3", 3200, 120, 60, 34, player_spells, player_items)

players = [player1, player2, player3]

enemy1 = Person("CPU-1", 10000, 130, 560, 325, enemy_spells, [])
enemy2 = Person("CPU-2", 20000, 250, 450, 25, enemy_spells, [])
enemy3 = Person("CPU-3", 5000, 330, 450, 25, enemy_spells, [])

enemies = [enemy1, enemy2, enemy3]

defeated_enemies = 0
defeated_players = 0
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
    for enemy in enemies:
        enemy.get_enemy_stats()
    for player in players:
        print("\n")
        player.get_player_stats()
        player.choose_action()
        # to get the correct action in the list we have to subtract 1
        choice = int(input("Choose Action :")) - 1

        if choice == 0:
            dmg = player.generate_damage()
            target_choice = player.choose_target(enemies)
            enemies[target_choice].take_damage(dmg)
            print("You attacked " +
                  enemies[target_choice].name + " for", dmg, "points of Damage")
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
                target_choice = player.choose_target(enemies)
                enemies[target_choice].take_damage(magic_dmg)
                print(bcolors.OKBLUE+"\n" + spell.name + " deals " +
                      str(magic_dmg), "points of Damage to " + enemies[target_choice].name + bcolors.ENDC)
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
                target_choice = player.choose_target(enemies)
                enemies[target_choice].take_damage(item.prop)
                print(bcolors.FAIL+"\n" + item.name + " deals  " +
                      str(item.prop), " points of damage to "+enemies[target_choice].name+"." + bcolors.ENDC)
        if enemies[target_choice].get_hp() == 0:
            print("Your enemy " +
                  enemies[target_choice].name + " has died.")
            del enemies[target_choice]
            defeated_enemies += 1

    # check if battle is over
    running = battle_status(defeated_enemies, defeated_players)

    print("\n"+separator)
    print("Enemies Turn")
    print(separator)

    # enemy turn
    for enemy in enemies:
        enemy_choice = random.randrange(0, 2)
        # enemy attack
        if enemy_choice == 0:
            target = random.randrange(0, len(players))
            enemy_dmg = enemy.generate_damage()
            players[target].take_damage(enemy_dmg)
            print("Enemy "+enemy.name+" attacks "+players[target].name+" for",
                  enemy_dmg, "points of Damage.")
        elif enemy_choice == 1:
            enemy_spell, enemy_dmg = enemy.choose_enemy_spell()
            enemy.reduce_mp(enemy_spell.cost)
            if enemy_spell.type == "white":
                enemy.heal(enemy_dmg)
                print(bcolors.OKBLUE + enemy_spell.name +
                      " heals " + enemy.name + " for "+str(enemy_dmg), "HP."+bcolors.ENDC)
            elif enemy_spell.type == "black":
                target = random.randrange(0, len(players))
                players[target].take_damage(enemy_dmg)
                print(bcolors.OKBLUE+"\n" + enemy.name + "'s " + enemy_spell.name + " deals " +
                      str(enemy_dmg), "points of Damage to " + players[target].name + bcolors.ENDC)
        if players[target].get_hp() == 0:
            print("Player " +
                  players[target].name + " has died!")
            del players[target]
            defeated_players += 1
    running = battle_status(defeated_enemies, defeated_players)
