import sys                                      # needed for loading bar
from time import sleep                          # Allows for timing delays
import itertools                                # for supacute cycling loading animations


### FORMATTING
def rgb(self, msg, r, g, b ):
    return f'\033[38;2;{r};{g};{b}m{msg}\033[0m'
#    color = Color()
#    color.rgb("hello", 255, 0, 0)

def formatting(msg,format):
    if format == 'italics':
        format = "\033[3m"
    elif format == 'bold':
        format = '\033[1m'
    elif format == 'underline':
        format = '\033[4m'
    return f'{format}{msg}\033[0m'


### PROGRESS BAR

def progress_bar(it, prefix="", size=60, file=sys.stdout):
    count = len(it)

    def show(j):
        x = int(size * j / count)
        file.write("%s╟%s%s╢ %i/%i\r" % (prefix, "█" * x, "░" * (size - x), j, count))
        file.flush()
    show(0)
    for i, item in enumerate(it):
        yield item
        show(i + 1)
    file.write("\n")
    file.flush()

def running_print(msg):
    for char in msg:
        sleep(0.10)
        print(char, end='')
        sys.stdout.flush()
#for i in progressbar(range(15), "Loading: ", 40):
#    time.sleep(0.1)  # any calculation you need

### CLASS CLASSES

### CHARACTERS
player_name = "null"
player_values={'NAME': "DEFAULT",
               'TITLE': "",
               'IDN': "NULL",
               'HP': 10,
               'MP': 5,
               'STR': 5,
               'DEF': 5,
               'WIS': 5,
               'INT': 5,
               'CHA': 5,
               'LUC': 5,
               'GOLD': 0}
class_base_stats = {'Townie':{'TITLE':"the townsperson",'HP':10,'MP':5,'STR':5,'DEF':5, 'WIS':5, 'INT':5, 'CHA':5, 'LUC':5,'GOLD':20},
                   'Paladin':{'TITLE':"the Paladin",'HP':10,'MP':4,'STR':7,'DEF':7, 'WIS':4, 'INT':4, 'CHA':6, 'LUC':3,'GOLD':20},
                   'Battle Mage':{'TITLE':"the Battlemage",'HP':10,'MP':8,'STR':3,'DEF':4, 'WIS':4, 'INT':6, 'CHA':6, 'LUC':4,'GOLD':20},
                   'Barbarian':{'TITLE':"the Barbarian",'HP':10,'MP':2,'STR':10,'DEF':8, 'WIS':2, 'INT':5, 'CHA':2, 'LUC':5,'GOLD':20},
                   'Gunslinger':{'TITLE':"the Gunslinger",'HP':10,'MP':4,'STR':5,'DEF':5, 'WIS':3, 'INT':5, 'CHA':6, 'LUC':7,'GOLD':20}}

'''class Character:
    def __init__(self, name,idn,hp,mp,str,df,mdf):
        self.name = name
        self.idn = idn
        self.hp = hp
        self.mp = mp
        self.str = str
        self.df = df
        self.mdf = mdf

    def incapacitated(self):
        return self.hp <= 0

    def self_awareness(self,name):
        print("I am"+name".")

class Main(Character):
    def __init__(self):
        super().__init__(name="traveller", hp=10, m)

class Npc(Character):

class Beast(Character):

#### ITEMS

#### ITEM(WEAPONS)

#### ITEM(ARMOR)

#### ITEM(MISC)

    player_data = {}

    class Character:  ## capable of being attacked, being KO'ed, defending themselves, buying and selling, holding inventory
        def __init__(self, name):
            self.name = name

        def self_awareness(self, name):
            print('ok')

        def attack(self, _str, ):
            print('ok')

        def defend(self, _def, _luk):
            print('ok')

        def KO(self, _hp):
            print('ok')

        def buy(self):
            print('ok')

        def sell(self):
            print('ok')'''
shopkeeper_1 = ''
shopkeeper_names = ['Landriel', 'Kip', 'Marinas', 'Undine', 'Elgis', 'Lojnar']
name_commentary = ['You must not be from around here.', 'That has a nice ring to it.', 'That\'s a fun name.', "I believe I had a cousin by that name. An odd one.", "That name reminds me of a story I heard once.", "The name of a real warrior.", "A splendid choice for a name."]
