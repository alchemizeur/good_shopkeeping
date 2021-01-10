from guts import *                              # means i don't have to use "guts."value
import sys                                      # needed for loading bar
from time import sleep                          # Allows for timing delays
import itertools                                # for super cute cycling loading animations
import random

# Start tutorial? done
# Move tutorial modules to a single universal folder
# Start introduction.
# build character name + identity
# Build character (eventually you get to randomize!)
# randomly assign shopkeepers to shopkeeper module shopkeeper1-7
# print stats
# This will be pushed into a class


def create_character_getidn(player_name):
    player_idn = input(
        " Alright,"+player_name+'. What are your preferred pronouns? Please type the corresponding number with your desired pronouns. |\n 1:He/him \n 2.She/her \n 3.They/Them \n 4.[custom]\n')
    if player_idn == "1":
        print(rgb("self", "You have selected masculine pronouns.", "92", "175", "120"))
        player_idn_poss = 'his'
        player_idn_subj = 'he'
        player_idn_verb = 'is'
        return player_idn_verb,player_idn_poss,player_idn_subj
    elif player_idn == "2":
        print(rgb("self", "You have selected feminine pronouns.", "92", "175", "120"))
        player_idn_poss = 'her'
        player_idn_subj = 'she'
        player_idn_verb = 'is'
        return player_idn_verb,player_idn_poss,player_idn_subj
    elif player_idn == "3":
        print(rgb("self", "You have selected gender neutral pronouns.", "92", "175", "120"))
        player_idn_poss = 'their'
        player_idn_subj = 'they'
        player_idn_verb = 'are'
        return player_idn_verb,player_idn_poss,player_idn_subj
    elif player_idn == "4":
        player_idn_poss = input("What pronouns do you use in place of possession? ex. (Her hat, His wand,Their gold) | ")
        if player_idn_poss == "":
            print(rgb("self", "Inputs must be included in custom pronouns. Please try again.", "255", "0", "0"))
            return (create_character_getidn(player_name))
        player_idn_subj = input("What pronouns do you use when someone refers to you? ex. (She is happy, He is working, They are dancing) | ")
        if player_idn_subj == "":
            print(rgb("self", "Inputs must be included in custom pronouns. Please try again.", "255", "0", "0"))
            return (create_character_getidn(player_name))
        player_idn_verb = input("What is the associated verb? ex. (IS,ARE) | ")
        if player_idn_verb == "":
            print(rgb("self", "Inputs must be included in custom pronouns. Please try again.", "255", "0", "0"))
            return (create_character_getidn(player_name))
        print(rgb("self", "You have selected custom pronouns.", "92", "175", "120"))
        return player_idn_verb,player_idn_poss,player_idn_subj
    else:
        print(
            "Looks like you picked a selection that was not a choice. We will work with custom pronouns. Feel free to put whatever pronouns you like.")
        player_idn_poss = input("What pronouns do you use in place of possession? ex. (Her hat, His wand,Their gold) | ")
        if player_idn_poss == "":
            print(rgb("self", "Inputs must be included in custom pronouns. Please try again.", "255", "0", "0"))
            return (create_character_getidn(player_name))
        player_idn_subj = input(
            "What pronouns do you use when someone refers to your? ex. (She is happy, He is working, They are dancing) | ")
        if player_idn_poss == "":
            print(rgb("self", "Inputs must be included in custom pronouns. Please try again.", "255", "0", "0"))
            return (create_character_getidn(player_name))
        player_idn_verb = input("What is the associated verb? ex. (IS,ARE) | ")
        if player_idn_verb == "":
            print(rgb("self", "Inputs must be included in custom pronouns. Please try again.", "255", "0", "0"))
            return (create_character_getidn(player_name))
        print(rgb("self", "You have selected custom pronouns.", "92", "175", "120"))
        return player_idn_verb,player_idn_poss,player_idn_subj


def create_character_getname():
    name_commentary = ['You must not be from around here.', 'That has a nice ring to it.', 'That\'s a fun name.',
                       "I believe I had a cousin by that name. An odd one.",
                       "That name reminds me of a story I heard once.", "The name of a real warrior.",
                       "A splendid choice for a name."]
    player_name: str = input("""What is your name?
    
    | ➤ """)

    if player_name == "":
        print("You have no name? That can't be right. Let's try again.")
        return create_character_getname()
    elif player_name.title() in shopkeeper_names:
        print(player_name.title()+"""? Is that so? Looks like you share a name with one of our very own shopkeepers of Ravine Ridge. You'llmost certainly have to visit their shop.""")
    running_print(rgb("self", "\nYou inform me that your name is "+player_name.title()+".\n", "92", "175", "120") + "\r")
    sleep(.5)
    response = input("\"Is "+player_name.title() + """ truly your name? """ + random.choice(name_commentary) + """ Please note once you select a name, you cannot change it. You can change your titles as you please." | y/N 
                                                 
    | ➤ """)
    if response.lower().startswith('y'):
        print('\nExcellent. ' + player_name.title() + " it is.")
        return player_name
    else:
        print("\nLet's try again then.")
        return create_character_getname()


def tutorial(tut):
    if tut.lower() in ("1", "formatting", "f"):
        print(chr(27) + '[2j')
        print(rgb("self", "You want to know more about formatting in the game.", "92", "175", "120") + "\r")
        print("_" * 130)
        sleep(0.1)
        print("""𝐀𝐁𝐎𝐔𝐓 𝐅𝐎𝐑𝐌𝐀𝐓𝐓𝐈𝐍𝐆
        
Formatting has many purposes in the game, and it is important to recognize potential threats as you embark on your journey!""")
        print(rgb("self", "Your decisions that you make will be notated in a familiar seafoam, by default. But can be changed in the [settings] menu.", "92", "175", "120") + "\r"),
        print(rgb("self", "Positive status effects, relationship improvements and combat-based bonuses will be displayed in a winner's green.", "50", "205", "50") + "\r"),
        print(rgb("self", "Negative status effects, relationship deterioration, and combat-based injuries and curses will be displayed in red.", "255", "0", "0") + "\n")
        tutorial_menu()
    elif tut.lower() in ("2", "decision", "d"):
        print(chr(27) + '[2j')
        print(rgb("self", "You want to know more about how decision-making works in the game.", "92", "175", "120") + "\r")
        print("_" * 130)
        sleep(0.1)
        print("""𝐀𝐁𝐎𝐔𝐓 𝐃𝐄𝐂𝐈𝐒𝐈𝐎𝐍 𝐌𝐀𝐊𝐈𝐍𝐆
                
The decisions you make matter. They can impact your relationships with your comrades, and dictate just how easy your voyage will be.
Make friends, make enemies, make lover(s) and friend(s), but keep in mind, memory is a terrible thing to waste. Burning bridges always
come with consequences.

Decisions will appear as choices you can make, and cannot be undone. Choose wisely! A slip of the hand can make the difference between
true love and sudden death!
""")
        tutorial_menu()
    elif tut.lower() in ("3", "beasts", "b"):
        print(chr(27) + '[2j')
        print(rgb("self", "You want to know more about beasts in the game.", "92", "175", "120") + "\r")
        print("_" * 130)
        sleep(0.1)
        print("""𝐀𝐁𝐎𝐔𝐓 𝐁𝐄𝐀𝐒𝐓𝐒
        
The world of Ravine Ridge is teeming with creatures, both big and small. As an adventurer you will encounter many beasts as you continue
your quest. Beasts will need to be tamed, captured or killed, and nearly all beasts have some kind of loot that you can scavenge for and add 
to your inventory for future shopkeeping antics. Keep in mind, however, beasts are quite capable of defending themselves, and you should
always be prepared for battle when you encounter enemies. It's killed or be killed out there, traveller. 
                """)
        tutorial_menu()
    elif tut.lower() in ("4", "relationships", "r"):
        print(chr(27) + '[2j')
        print(rgb("self", "You want to know more about relationships in the game.", "92", "175", "120") + "\r")
        print("_" * 130)
        sleep(0.1)
        print("""𝐀𝐁𝐎𝐔𝐓 𝐑𝐄𝐋𝐀𝐓𝐈𝐎𝐍𝐒𝐇𝐈𝐏𝐒
        
Good Shopkeeping is a game about relationships. No matter how big and small, you are here in ravine ridge to help the merchant class get what
they need done. Each shopkeeper you encounter is going to need your help, and what you do can greatly turn the tide. Relationships are mostly 
affected by decision making in conversation, but can also be affected by external actions, such as gifts, world interactions and reputation. 

A tightly forged relationship can make all the difference in battle, but some relationships simply aren't worth keeping!
                """)
        tutorial_menu()
    elif tut.lower() in ("5", "exit", "e"):
        print(chr(27) + '[2j')
        print(rgb("self", "You have decided to exit the tutorial.\nFeel free to type 'tutorial' or 'help' to return to the tutorial page anytime.\n", "92", "175", "120") + "\r")
    else:
        tut_wrong_input: str = input("You have selected an option that is not one of the predetermined choices. Would you like to remain in the tutorial? (y/N)\n   | ➤")
        if tut_wrong_input.lower.startswith('y'):
            tutorial_menu()
        else:
            print(rgb("self", "You have decided to exit the tutorial.\nFeel free to type 'tutorial' or 'help' to return to the tutorial page anytime.\n","92", "175", "120") + "\r")


def tutorial_menu():
    tut: str = input("""
   ➤ 1. | Tell Me About [Formatting] Instructions
   ➤ 2. | Tell Me About [Decision] Impacts
   ➤ 3. | Tell Me About [Beasts]
   ➤ 4. | Tell Me About [Relationships]
   ➤ 5. | [Exit] Tutorial
   
   | ➤ """)
    tutorial(tut)


def start_tutorial():
    sleep(0.1)
    tutorial: str = input("""Would you like to begin the tutorial? (y/N) 
    | ➤ """)

    if tutorial.lower().startswith('y'):
        print(chr(27) + '[2j')
        print(rgb("self", "You have accepted the tutorial.", "92", "175", "120") + "\r")
        print("_" * 130)
        sleep(0.1)
        print("""𝐆𝐎𝐎𝐃 𝐒𝐇𝐎𝐏𝐊𝐄𝐄𝐏𝐈𝐍𝐆 𝐓𝐔𝐓𝐎𝐑𝐈𝐀𝐋
        """)
        print("Welcome to Good Shopkeeping," + rgb("self", "[Traveller!]", "92", "175", "120") + """
The instructions are simple.

You are an adventurer travelling the beautiful merchant city of""" + rgb("", " [RAVINE RIDGE]", "92", "175", "120") + """, a city famous for its goods and services which provide mystical items
of all types across the mainland. You will be hired by a number of Merchants to go on a range of riveting quests, from scavenging for magical goods,
to slaying beasts to saving sultry damsels, dreamy himbos and everyone in between!

Improve your combat, relationships and collections as you gain reputation, power and capital throughout this bustling city and everchanging world!

You can input either number, OR type the [bracketed words] OR type the first letter of the bracketed words to select a decision below:""")
        tutorial_menu()


running_print("✨ 𝐖𝐄𝐋𝐂𝐎𝐌𝐄 𝐓𝐎 𝐆𝐎𝐎𝐃 𝐒𝐇𝐎𝐏𝐊𝐄𝐄𝐏𝐈𝐍𝐆 ✨\n")
input("Press Enter To Continue | ➤ ")
start_tutorial()
"""c = itertools.cycle(['|', '\\', '-', '/'])
import math
for i in range(100):
    bar = next(c)*(math.ceil(abs(math.cos(i/(100/(6*math.pi))))*.5*i) + math.ceil(.5*i))
    after = ' '*(100-len(bar))
    print(f"{bar}{after}", end='\r')
    sys.stdout.flush()
    sleep(.1)                           # my command line is broken... both loading bar and itertools ):
for i in range(90):
    sleep(.1/((i+20)/20))
    if i % 3 == 0:
        sys.stdout.write('✨'*50 + '\r')
    else:
        sys.stdout.write(' '*100 + '\r')
    sys.stdout.flush()
print('')
for i in progress_bar(range(15), "Loading: ", 40):
    sleep(0.1)  # any calculation you need"""
if not shopkeeper_1: # can use this in place of == 'NULL' which is better!
    shopkeeper_1 = random.choice(shopkeeper_names)
print(shopkeeper_1)
print(chr(27) + '[2j')
print(rgb("self", "Looks like you're ready to go! Let's begin!", "92", "175", "120") + "\r")
print("_" * 130)
sleep(0.1)
running_print("𝐓𝐎𝐃𝐀𝐘 𝐒𝐔𝐑𝐄 𝐈𝐒 𝐀 𝐆𝐑𝐄𝐀𝐓 𝐃𝐀𝐘 𝐅𝐎𝐑 𝐀𝐍 𝐀𝐃𝐕𝐄𝐍𝐓𝐔𝐑𝐄.\n\n")
print("""And a very busy time for a mercenary. Looks like Ravine Ridge has been seeing some pretty awful beast activity as of
late, and has outsourced help from the neighboring cities to seek some help. Lucky for them, they got you.

The first shop that you have been hired for is owned by a shopkeeper by the name of """+shopkeeper_1+""".  So as you settle in,
it's time to think about who you are in this new place.

A name is a fitting place to start. \n""")
player_name= create_character_getname()
player_idn_poss, player_idn_subj, player_idn_verb = create_character_getidn(player_name)
"""player_values.update({'NAME': ch_name})
player_values.update({'IDN': ch_idn})"""
print(player_values)





