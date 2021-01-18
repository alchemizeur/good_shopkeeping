from guts import *                              # means i don't have to use "guts."value
import sys                                      # needed for loading bar
from time import sleep                          # Allows for timing delays
import itertools                                # for super cute cycling loading animations
import random
import atexit
import termios

# Start tutorial? done
# Move tutorial modules to a single universal folder
# Start introduction.
# build character name + identity
# Build character (eventually you get to randomize!)
# randomly assign shopkeepers to shopkeeper module shopkeeper1-7
# print stats
# This will be pushed into a class

def compile_character (player_name,player_idn_poss,player_idn_subj,player_idn_verb,player_class):
    print('this is where the character info will be compiled into a singular thing...need classes to be complete')
def create_character_class(player_name):
    print("_" * 130)
    running_print(rgb("self","Please select one of the following classes:","125", "88", "245"))

    player_class = input("""\n
    | ➤ 1: [🛡️️] [𝐒]𝐖𝐎𝐑𝐃 𝐎𝐅 𝐑𝐄 (Warrior, Paladin or Antipaladin path)   
   
    Trained well in the swordwielding arts, the Swords of Re are devout members of blade and light, and gain strength
    through their deity Solregarc, bringer of light, manifestation and truth. Few can match a proficient swordsman blade-to-blade,
    and their unshakeable stance can easily leave heaps of enemies. A paladin has already devoted themselves to the path of light,
    shining hope and prosperity to the land. True heroes. A warrior walks the same path, yet to devote themselves to the sun god,
    while a small subset of swords turn away from their path of righteousness.
    
    + Adept at all weaponry, including [very heavy weapons] through raw strength and discipline.
    + Capable of fast recovery in religious establishments.
    + Unmatched ability to sense motivations and see through deceit-- and nearly impervious to emotional disarray.
    + Heavy stances are capable of blocking most projectiles with blades
    
    HP ➤ [█████████░░] 8/10        MAGIC ➤ [███████░░░░] 6/10       SPEED ➤ [███░░░░░░░░] 4/10      STRENGTH ➤ [██████████░] 9/10
    
------------------------------------------------------------------------------------------------------------------------
    
    | ➤ 2: [📜] [𝐓]𝐄𝐂𝐇𝐍𝐎𝐌𝐀𝐆𝐔𝐒 (battlemage, necromancer, or artificer path)
    
    The technomagus is a scientist; a student of arcana and arithmetic. Hailing from PRIMA OCULMATIS, the elite school of 
    magic, the technomagus has honed their skill in preservation in battle. The lines of good and evil are murky for these intellectualae,
    but I can trust that you will do the right thing, can't I?
    
    + Powerful queueing ability allows for strategic chain-casts and predicting enemy attacks before they happen.
    + Capable of learning new abilities within tomes, and repurposing their own knowledge for powerful spells
    + Warding magic keeps them light on their feet while still able to block combat
    + Masters of status effects, both internal and environmental
    
    HP ➤ [███████░░░░] 6/10        MAGIC ➤ [██████████░] 9/10       SPEED ➤ [████████░░░] 7/10      STRENGTH ➤ [████░░░░░░░] 4/10
    
------------------------------------------------------------------------------------------------------------------------
    
    | ➤ 3: [🌳] [𝐅]𝐄𝐑𝐀𝐋𝐈𝐍𝐆 (druid, monk or barbarian path)
    
    The feraling is a child of nature. This bustling seaport city may not be it's singular choice for a home, 
    but the intimate knowlege of nature's secrets makes the feraling attuned to what most of the folks of Ravine Ridge
    can not. Powers of nature and beast allow them an undeniable edge in natural domains, and famiiar knowledge which
    prevents them from being caught off-guard.
    
    + Natureborne allows them immunity to many natural poisons, traps and larger stats boosts to natural potions.
    + Capable of training wild animals
    + Stat and knowledge boosts in natural environments
    + Heightened looting efficiency for extracting more from fallen beasts
    
    HP ➤ [███████░░░░] 6/10        MAGIC ➤ [█████████░░] 8/10       SPEED ➤ [██████░░░░░] 5/10      STRENGTH ➤ [████████░░░] 7/10

------------------------------------------------------------------------------------------------------------------------
    
    |➤ 4: [🌑] [𝐂]𝐎𝐍𝐓𝐑𝐀𝐂𝐓𝐄𝐄𝐑 (gunslinger, ninja or rogue path)
    
    The contracteer is no stranger to being hired, and this is certainly not the first time they have been enlisted
    to kill. The Contracteer is the supreme class for taking on jobs, forged in the shadow factions of the continent. 
    When you know, you know-- and the contracteer knows all. Lightning reflexes make expert assassins, allowing for 
    quick bounding fights that are over before the opponent even realizes they began...
    
    + Natural stealth abilities mean extraordinary extrasensory perception
    + Quickest reflexes means lessened chance to be caught prone, even when retreating
    + Intimidating leer means that most contracteers can extract information simply by their demeanor
    + Acrobatics proficiency means the contracteer (almost) always lands on their feet.
    
    HP ➤ [█████████░░] 8/10        MAGIC ➤ [████░░░░░░░] 4/10       SPEED ➤ [██████████░] 9/10      STRENGTH ➤ [████████░░░] 7/10
    
------------------------------------------------------------------------------------------------------------------------
  
    | ➤ """)
    if player_class.lower() in ('1','s','sword of re','sword','paladin','warrior','antipaladin'):
        player_class = 'Sword of Re'
    elif player_class.lower() in ('2','t','technomagus','mage','magus','battlemage','battle mage','necromancer','artificer'):
        player_class = 'Technomagus'
    elif player_class.lower() in ('3','f','feraling','monk','druid','barbarian'):
        player_class = 'Feraling'
    elif player_class.lower() in ('4','c','contracteer','contracter','contractor','gunslinger','ninja','rouge'):
        player_class = 'Contracteer'
    else:
        print('You have selected a class that has not been specified. Please enter the number, first letter or class name of the class you desire.')
        return player_class
        create_character_class(player_name)
    print('You have selected '+ player_class+' as your path class. As story progresses, you will be able to refine your class further.')
    return player_class

def create_character_getidn(player_name):
    player_idn = input(
        "\nExcellent. Alright, "+player_name.title()+""". What are your preferred pronouns? Please type the corresponding number with your desired pronouns.
        
    | ➤ 1:He/him
    | ➤ 2.She/her
    | ➤ 3.They/Them
    | ➤ 4.[custom]
    
    | ➤   """)
    if player_idn == "1":
        print(rgb("self", "\nYou have selected masculine pronouns.\n", "125", "88", "245"))
        player_idn_poss = 'his'
        player_idn_subj = 'he'
        player_idn_verb = 'is'
        return player_idn_verb,player_idn_poss,player_idn_subj
    elif player_idn == "2":
        print(rgb("self", "\nYou have selected feminine pronouns.\n", "125", "88", "245"))
        player_idn_poss = 'her'
        player_idn_subj = 'she'
        player_idn_verb = 'is'
        return player_idn_verb,player_idn_poss,player_idn_subj
    elif player_idn == "3":
        print(rgb("self", "\nYou have selected gender neutral pronouns.\n", "125", "88", "245"))
        player_idn_poss = 'their'
        player_idn_subj = 'they'
        player_idn_verb = 'are'
        return player_idn_verb,player_idn_poss,player_idn_subj
    elif player_idn in ('4','custom'):
        player_idn_poss = input("\nWhat pronouns do you use in place of possession? ex. (Her hat, His wand,Their gold) | ")
        if player_idn_poss == "":
            print(rgb("self", "\nInputs must be included in custom pronouns. Please try again.", "255", "0", "0"))
            return (create_character_getidn(player_name))
        player_idn_subj = input("\nWhat pronouns do you use when someone refers to you? ex. (She is happy, He is working, They are dancing) | ")
        if player_idn_subj == "":
            print(rgb("self", "\nInputs must be included in custom pronouns. Please try again.", "255", "0", "0"))
            return (create_character_getidn(player_name))
        player_idn_verb = input("\nWhat is the associated verb? ex. (IS,ARE) | ")
        if player_idn_verb == "":
            print(rgb("self", "\nInputs must be included in custom pronouns. Please try again.", "255", "0", "0"))
            return (create_character_getidn(player_name))
        print(rgb("self", "\nYou have selected custom pronouns.", "125", "88", "245"))
        return player_idn_verb,player_idn_poss,player_idn_subj
    else:
        print(
"\nLooks like you picked a selection that was not a choice. We will work with custom pronouns. Feel free to put whatever pronouns you like.")
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
        print(rgb("self", "You have selected custom pronouns.", "125", "88", "245"))
        return player_idn_verb,player_idn_poss,player_idn_subj


def create_character_getname():
    name_commentary = ['You must not be from around here.', 'That has a splendid ring to it.', 'That\'s a fun name.',
                       "I believe I had a cousin by that name. An odd one.",
                       "That name reminds me of a story I heard once.", "The name of a real warrior.",
                       "A splendid choice for a name.","A name worth envying.","A name filled with potential and pizazz."]
    player_name: str = input("""What is your name?
    
    | ➤ """)

    if player_name == "":
        print("\nYou have no name? That can't be right. Let's try again.\n")
        return create_character_getname()
    elif player_name.title() in shopkeeper_names:
        print(player_name.title()+"""? Is that so? Looks like you share a name with one of our very own shopkeepers of Ravine Ridge. You'llmost certainly have to visit their shop.""")
    running_print(rgb("self", "\nYou inform me that your name is "+player_name.title()+".\n", "125", "88", "245") + "\r\n")
    sleep(.5)
    response = input("\"Is "+player_name.title() + """ truly your name? """ + random.choice(name_commentary) + """ Please note once you select a name, you cannot change it. You can change your titles as you please." | y/N 
                                                 
    | ➤ """)
    if response.lower().startswith('y'):
        running_print(rgb("self", "\nYou nod. You are happy with the name " + player_name.title() + ".\n", "125", "88",
                          "245") + "\r\n")
        return player_name
    else:
        running_print(rgb("self", "\nYou shake your head. You are not happy with the name.", "125", "88",
                          "245") + "\n")
        print('\n"Let\'s try again then."')
        return create_character_getname()


def tutorial(tut):
    if tut.lower() in ("1", "formatting", "f"):
        print(chr(27) + '[2j')
        print(rgb("self", "You want to know more about formatting in the game.", "125", "88", "245") + "\r")
        print("_" * 130)
        sleep(0.1)
        print("""𝐀𝐁𝐎𝐔𝐓 𝐅𝐎𝐑𝐌𝐀𝐓𝐓𝐈𝐍𝐆
        
Formatting has many purposes in the game, and it is important to recognize potential threats as you embark on your journey!""")
        print(rgb("self", "Your decisions that you make will be notated in purple, by default. But can be changed in the [settings] menu.", "125", "88", "245") + "\r"),
        print(rgb("self", "Positive status effects, relationship improvements and combat-based bonuses will be displayed in a winner's green.", "50", "205", "50") + "\r"),
        print(rgb("self", "Negative status effects, relationship deterioration, and combat-based injuries and curses will be displayed in red.", "255", "0", "0") + "\n")
        tutorial_menu()
    elif tut.lower() in ("2", "decision", "d"):
        print(chr(27) + '[2j')
        print(rgb("self", "You want to know more about how decision-making works in the game.", "125", "88", "245") + "\r")
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
        print(rgb("self", "You want to know more about beasts in the game.", "125", "88", "245") + "\r")
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
        print(rgb("self", "You want to know more about relationships in the game.", "125", "88", "245") + "\r")
        print("_" * 130)
        sleep(0.1)
        print("""𝐀𝐁𝐎𝐔𝐓 𝐑𝐄𝐋𝐀𝐓𝐈𝐎𝐍𝐒𝐇𝐈𝐏𝐒
        
Good Shopkeeping is a game about relationships. No matter how big and small, you are here in ravine ridge to help the merchant class get what
they need done. Each shopkeeper you encounter is going to need your help, and what you do can greatly turn the tide. Relationships are mostly 
affected by decision making in conversation, but can also be affected by external actions, such as gifts, world interactions and reputation. 

A tightly forged relationship can make all the difference in battle, but some relationships simply aren't worth keeping!
                """)
        tutorial_menu()
    elif tut.lower() in ("5", "items", "i"):
        print(chr(27) + '[2j')
        print(rgb("self", "You want to know more about inventory and items in the game.", "125", "88", "245") + "\r")
        print("_" * 130)
        sleep(0.1)
        print("""𝐈𝐍𝐕𝐄𝐍𝐓𝐎𝐑𝐘 𝐀𝐍𝐃 𝐈𝐓𝐄𝐌𝐒

There are many types of items in good shopkeeping, and while you don't have tho collect them all by any means, knowing the different types will be
critical to succeeding in battle and adventure. There are currently (5) types of items to note:

    𝐂𝐎𝐍𝐒𝐔𝐌𝐀𝐁𝐋𝐄:
    Items which can be used up and impact stats | Potions, food, beverages, traps, scrolls, first aid, torches
    
    𝐀𝐑𝐌𝐎𝐑:
    Wearable items which impact stats and can increase defense | 
    
    𝐖𝐄𝐀𝐏𝐎𝐍
    Wearable items which impact attack + casting capabilities. | Swords, staffs and Bows, Guns, Hammers and wands! 
    
    𝐀𝐌𝐌𝐔𝐍𝐈𝐓𝐈𝐎𝐍:
    Consumable ammunition for certain weapons, such as bows and guns.
    
    𝐆𝐈𝐅𝐓:
    Items that can be gifted or used as props, to increase pizzazz or relationships.
    
    𝐏𝐄𝐓 (pending):
    Autonomous types that can defend you in battle and look cute doing it.
    
    Each item has a distinct usage, and can influence the story in a myriad of ways, so be careful! """)
        tutorial_menu()
    elif tut.lower() in ("6", "exit", "e"):
        print(chr(27) + '[2j')
        print(rgb("self", "You have decided to exit the tutorial.","125", "88", "245")+"\n\nnFeel free to type 'tutorial' or 'help' to return to the tutorial page anytime.\n\r")
    else:
        tut_wrong_input: str = input("\nYou have selected an option that is not one of the predetermined choices. Would you like to remain in the tutorial? (y/N)\n\n   | ➤")
        if tut_wrong_input.lower().startswith('y'):
            tutorial_menu()
        else:
            print(chr(27) + '[2j')
            print(rgb("self", "You have decided to exit the tutorial.", "125", "88",
                      "245") + "\n\nFeel free to type 'tutorial' or 'help' to return to the tutorial page anytime.\n\r")


def tutorial_menu():
    tut: str = input("""
   ➤ 1. | Tell Me About [Formatting] Instructions
   ➤ 2. | Tell Me About [Decision] Impacts
   ➤ 3. | Tell Me About [Beasts]
   ➤ 4. | Tell Me About [Relationships]
   ➤ 5. | Tell Me about [Items] 
   ➤ 6. | [Exit] Tutorial
   
   | ➤ """)
    tutorial(tut)


def start_tutorial():
    sleep(0.1)
    tutorial: str = input("""Would you like to begin the tutorial? (y/N) 
    | ➤ """)

    if tutorial.lower().startswith('y'):
        print(chr(27) + '[2j')
        print(rgb("self", "You have accepted the tutorial.", "125", "88", "245") + "\r")
        print("_" * 130)
        print(
'''┌┬┐┬ ┬┌┬┐┌─┐┬─┐┬┌─┐┬  
 │ │ │ │ │ │├┬┘│├─┤│  
 ┴ └─┘ ┴ └─┘┴└─┴┴ ┴┴─┘''')
        sleep(0.1)
        print("""𝐆𝐎𝐎𝐃 𝐒𝐇𝐎𝐏𝐊𝐄𝐄𝐏𝐈𝐍𝐆 𝐓𝐔𝐓𝐎𝐑𝐈𝐀𝐋
        """)
        print("Welcome to Good Shopkeeping," + rgb("self", "[Traveller!]", "125", "88", "245") + """
The instructions are simple.

You are an adventurer travelling the beautiful merchant city of""" + rgb("", " [RAVINE RIDGE]", "125", "88", "245") + """, a city famous for its goods and services which provide mystical items
of all types across the mainland. You will be hired by a number of Merchants to go on a range of riveting quests, from scavenging for magical goods,
to slaying beasts to saving sultry damsels, dreamy himbos and everyone in between!

Improve your combat, relationships and collections as you gain reputation, power and capital throughout this bustling city and everchanging world!

You can input either number, OR type the [bracketed words] OR type the first letter of the bracketed words to select a decision below:""")
        tutorial_menu()

def main():
    print('\033[2J', end='')
    print('\033[2;f', end='')  # set cursor at row 2, column 1
    print('')
    running_print("✨ 𝐖𝐄𝐋𝐂𝐎𝐌𝐄 𝐓𝐎 𝐆𝐎𝐎𝐃 𝐒𝐇𝐎𝐏𝐊𝐄𝐄𝐏𝐈𝐍𝐆 ✨\n\n\n")
    # print('\033[6;80f', end='')
    input("Press Enter To Continue | ➤ ")
    print('\033[2J', end='')
    print('\033[2;f', end='')  # set cursor at row 2, column 1
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
    print(chr(27) + '[2j')
    print(rgb("self", "Looks like you're ready to go! Let's begin!", "125", "88", "245") + "\r")
    print("_" * 130)
    sleep(0.1)
    running_print("\n✨ 𝐓𝐎𝐃𝐀𝐘 𝐒𝐔𝐑𝐄 𝐈𝐒 𝐀 𝐆𝐑𝐄𝐀𝐓 𝐃𝐀𝐘 𝐅𝐎𝐑 𝐀𝐍 𝐀𝐃𝐕𝐄𝐍𝐓𝐔𝐑𝐄 ✨\n\n")
    print("""And a very busy time for a mercenary. Looks like Ravine Ridge has been seeing some pretty awful beast activity as of
    late, and has outsourced help from the neighboring cities to seek some help. Lucky for them, they got you.
    
    The first shop that you have been hired for is owned by a shopkeeper by the name of """+shopkeeper_1+""".  So as you settle in,
    it's time to think about who you are in this new place.
    
    A name is a fitting place to start. \n""")
    player_name= create_character_getname()
    player_idn_poss, player_idn_subj, player_idn_verb = create_character_getidn(player_name)
    """player_values.update({'NAME': ch_name})
    player_values.update({'IDN': ch_idn})"""
    player_class = create_character_class(player_name)
    print(player_values)
    print(player_class)
    compile_character(player_name,player_idn_poss,player_idn_subj,player_idn_verb,player_class)
    print("CHAPTER ONE:"+shopkeeper_1.upper())

if __name__ == '__main__':
    main()



