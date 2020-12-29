## Create Class stats
## Create function to get initial character data to feed into class
## Create Classes for the corresponding bases

from time import sleep

## will be moved to a stats.py eventually

## FORMATTING
class color:
  PURPLE = '\033[95m'
  CYAN = '\033[96m'
  DARKCYAN = '\033[36m'
  BLUE = '\033[94m'
  GREEN = '\033[92m'
  YELLOW = '\033[93m'
  RED = '\033[91m'
  BOLD = '\033[1m'
  UNDERLINE = '\033[4m'
  END = '\033[0m'

class br:
   BREAKER = "___________________________________________________________________________________________________________"
   print(BREAKER)

class_base_stats = {'Default':{'HP':10,'MP':5,'STR':5,'DEF':5, 'WIS':5, 'INT':5, 'CHA':5, 'LUC':5,'GOLD':20},
                   'Paladin':{'HP':10,'MP':4,'STR':7,'DEF':7, 'WIS':4, 'INT':4, 'CHA':6, 'LUC':3,'GOLD':20},
                   'Battle Mage':{'HP':10,'MP':8,'STR':3,'DEF':4, 'WIS':4, 'INT':6, 'CHA':6, 'LUC':4,'GOLD':20},
                   'Barbarian':{'HP':10,'MP':2,'STR':10,'DEF':8, 'WIS':2, 'INT':5, 'CHA':2, 'LUC':5,'GOLD':20},
                   'Gunslinger':{'HP':10,'MP':4,'STR':5,'DEF':5, 'WIS':3, 'INT':5, 'CHA':6, 'LUC':7,'GOLD':20}}

class Character: ## capable of being attacked, being KO'ed, defending themselves, buying and selling, holding inventory
   def __init__(self,name):
       self.name = name

   def self_awareness(self,name):
       print('ok')
   def attack(self,_str,):
       print('ok')
   def defend(self,_def,_luk):
       print('ok')
   def KO(self,_hp):
       print('ok')
   def buy(self):
       print('ok')
   def sell(self):
       print('ok')

shopkeeper_name_list = ('Landriel', 'Kip', 'Marinas', 'Undine', 'Elgis', 'Lojnar')

def start_tutorial():
   sleep(0.1)
   tutorial: str = input("Would you like to begin the tutorial? (y/N) | ➤ ")
   br.breaker
   if tutorial.lower().startswith('y'):
       print(color.DARKCYAN + "You have accepted the tutorial." + color.END)
       br.breaker

       sleep(0.1)
       print(color.BOLD + '𝐆𝐎𝐎𝐃 𝐒𝐇𝐎𝐏𝐊𝐄𝐄𝐏𝐈𝐍𝐆 𝐓𝐔𝐓𝐎𝐑𝐈𝐀𝐋' + color.END)
   tutorial: str = input("""Welcome to Good Shopkeeping, Traveller!
The instructions are simple.
You are an adventurer travelling the beautiful merchant city of [RAVINE RIDGE], a city famous for its goods and services which provide mystical items of all types across the mainland.
You will be hired by a number of Merchants to go on a range of riveting quests, from scavenging for magical goods, to slaying beasts to saving sultry damsels, dreamy himbos and everyone in between!
Improve your combat, relationships and collections as you gain reputation, power and capital throughout this bustling city!

You can input either number, OR type the [bracketed words] to select a decision below:

   ➤ 1. | Tell Me About Formatting Instructions
   ➤ 2. | Tell Me About Decision Impacts
   ➤ 3. | Tell Me About Beasts
   ➤ 4. | Tell Me About Relationships

➤""")

   input("Press Enter To Continue | ➤ ")
   print("""exiting tutorial...
___________________________________________________________________________________________________________""")
   br.BREAKER

   return start_tutorial

def get_character_info():
   print("this is the tart")

introduction_1 = "𝐖𝐄𝐋𝐂𝐎𝐌𝐄 𝐓𝐎 𝐆𝐎𝐎𝐃 𝐒𝐇𝐎𝐏𝐊𝐄𝐄𝐏𝐈𝐍𝐆.𝐏𝐘\n"
for char in introduction_1:
   sleep(0.1)
   print(char, end='')
start_tutorial = start_tutorial()
print(start_tutorial)
