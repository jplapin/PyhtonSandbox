import random
import colorama
from .magic import Spell


# needed to add color to the terminal in VSCode
colorama.init()

# assigns variables to colors in terminal


class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNiNG = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'  # needed to end the color code
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


class Person:
    def __init__(self, name, hp, mp, atk, df, magic, items):
        self.maxhp = hp
        self.hp = hp
        self.maxmp = mp
        self.mp = mp
        self.atkh = atk + 10
        self.atkl = atk - 10
        self.df = df
        self.magic = magic
        self.items = items
        self.name = name
        self.actions = ["Attack", "Magic", "Items"]

    def generate_damage(self):
        return random.randrange(self.atkl, self.atkh)

    def take_damage(self, dmg):
        self.hp -= dmg
        if self.hp < 0:
            self.hp = 0
        return self.hp

    def heal(self, dmg):
        self.hp += dmg
        if self.hp > self.maxhp:
            self.hp = self.maxhp

    def get_hp(self):
        return self.hp

    def get_max_hp(self):
        return self.maxhp

    def get_mp(self):
        return self.mp

    def get_max_mp(self):
        return self.maxmp

    def reduce_mp(self, cost):
        self.mp -= cost

    def choose_action(self):
        i = 1
        print("\n"+bcolors.BOLD + self.name + bcolors.ENDC)
        print(bcolors.OKBLUE + bcolors.BOLD + "Actions" + bcolors.ENDC)
        for item in self.actions:
            print("    "+str(i) + ":", item)
            i += 1

    def choose_magic(self):
        i = 1
        print("\n"+bcolors.OKBLUE + bcolors.BOLD + "Magic" + bcolors.ENDC)
        for spell in self.magic:
            print("    "+str(i) + ":", spell.name,
                  "(cost:", str(spell.cost)+")")
            i += 1

    def choose_items(self):
        i = 1
        print("\n"+bcolors.OKGREEN + bcolors.BOLD + "Items" + bcolors.ENDC)
        for item in self.items:
            print("    "+str(i) + ":", item["item"].name,
                  " - ", item["item"].description, " (x" + str(item["quantity"])+")")
            i += 1

    def choose_target(self, enemies):
        i = 1
        print("\n"+bcolors.FAIL + bcolors.BOLD + "Target:" + bcolors.ENDC)
        for enemy in enemies:
            if enemy.get_hp() != 0:
                print("    "+str(i) + ".", enemy.name)
                i += 1
        choice = int(input("Choose your target: "))-1
        return choice

    def fill_up_bar(self, bar_lenght, current_points, max_points):
        bar = ""
        bar_points = (current_points/max_points)*100/(100/bar_lenght)
        while bar_points > 0:
            bar += "█"
            bar_points -= 1
        while len(bar) < bar_lenght:
            bar += " "
        return bar

    def leading_spaces_bar(self, points_str, points_size):
        current_spaces = ""
        if len(points_str) < points_size:
            decreased_mp = points_size - len(points_str)
            while decreased_mp > 0:
                current_spaces += " "
                decreased_mp -= 1
            current_spaces += points_str
        else:
            current_spaces = points_str
        return current_spaces

    def get_player_stats(self):
        hp_bar = self.fill_up_bar(20, self.hp, self.maxhp)
        mp_bar = self.fill_up_bar(10, self.mp, self.maxmp)

        hp_string = str(self.hp)+"/"+str(self.maxhp)
        mp_string = str(self.mp)+"/" + str(self.maxmp)

        current_hp = self.leading_spaces_bar(hp_string, 9)
        current_mp = self.leading_spaces_bar(mp_string, 7)

        print("NAME                             HP                             MP")
        print("                         ____________________               __________")
        print(bcolors.BOLD + self.name + ":     " + current_hp + " |" +
              bcolors.OKGREEN+hp_bar+bcolors.ENDC+bcolors.BOLD + "|     " +
              current_mp + " |"+bcolors.OKBLUE+mp_bar+bcolors.ENDC+bcolors.BOLD+"|"+bcolors.ENDC)

    def get_enemy_stats(self):
        hp_enemy_bar = self.fill_up_bar(45, self.hp, self.maxhp)
        hp__enemy_string = str(self.hp)+"/"+str(self.maxhp)
        current_hp_enemy = self.leading_spaces_bar(hp__enemy_string, 11)
        print("NAME                                      HP                     ")
        print("                    _____________________________________________")
        print(bcolors.BOLD + self.name + ": " + current_hp_enemy + " |" +
              bcolors.FAIL+hp_enemy_bar+bcolors.ENDC+bcolors.BOLD + "|" + bcolors.ENDC)

    def choose_enemy_spell(self):
        running = True
        while running:
            magic_choice = random.randrange(0, len(self.magic))
            spell = self.magic[magic_choice]
            magic_dmg = spell.generate_damage()
            health_percentage = self.hp / self.maxhp * 100
            if self.mp < spell.cost or spell.type == "white" and health_percentage > 50:
                pass
            else:
                return spell, magic_dmg
