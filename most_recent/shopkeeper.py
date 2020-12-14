# !usr/bin/env python3
# shopkeeper.py
# introduces prompt script which askes your name, your preferred pronouns and your age.

import sys
import random
import shopkeeper_stats
import csv
from time import sleep


def get_player_data (shopkeeper_name, SHPKPR, color):
    shopkeeper_names = ['Landriel', 'Kip', 'Marinas', 'Undine', 'Elgis', 'Lojnar']
    shopkeeper_commentary = ['You must not be from around here.', 'That has a nice ring to it.', 'That\'s a fun name.', "I believe I had a cousin by that name. An odd one.", "That name reminds me of a story I heard once.", "The name of a real warrior.", "A splendid choice for a name."]
    if not shopkeeper_name: # can use this in place of == 'NULL' which is better!
        shopkeeper_name=random.choice(shopkeeper_names)
    print("My name is "+shopkeeper_name+". Before I introduce you to the shop, I shall ask you a number of clarifying questions.")
    player_name = input("To start, what is your name? | ")
    if player_name == "":
        print("You have no name? That can't be right. Let's try again.")
        return(get_player_data(shopkeeper_name, SHPKPR, color))
    response = input(player_name.title()+" is it? Is that correct? | y/N | ")
    if response.lower().startswith('y'):
        if player_name.lower() == shopkeeper_name.lower():
            print("Is that so! Looks like we have the same name. Would you look at that!")
            shopkeeper_stats.SHPKPR = SHPKPR + 1
            print(color.GREEN + 'Your relationship has increased with the shopkeeper '+shopkeeper_name+', but only by a little!' + color.END)
            return player_name,shopkeeper_name
        else:
            print(player_name.title()+". "+random.choice(shopkeeper_commentary))
            return player_name,shopkeeper_name
    else:
        print("Let's try again then.")
        return(get_player_data(shopkeeper_name, SHPKPR, color))
def get_player_identity(color):
    player_pn = input('What are your preferred pronouns? Please type the corresponding number with your desired pronouns. |\n 1:He/him \n 2.She/her \n 3.They/Them \n 4.[custom]\n')
    if player_pn == "1":

        print(color.CYAN + 'You have selected masculine pronouns.' + color.END)
        player_pn_poss= 'his'
        player_pn_subj= 'he'
        player_pn_verb= 'is'
    elif player_pn == "2":
        print(color.CYAN + 'You have selected feminine pronouns.' + color.END)
        player_pn_poss= 'her'
        player_pn_subj= 'she'
        player_pn_verb= 'is'
    elif player_pn == "3":
        print(color.CYAN + 'You have selected gender neutral pronouns.' + color.END)
        player_pn_poss= 'their'
        player_pn_subj= 'they'
        player_pn_verb= 'are'
    elif  player_pn == "4":
        player_pn_poss = input("What pronouns do you use in place of possession? ex. (Her hat, His wand,Their gold) | ")
        player_pn_subj = input("What pronouns do you use when someone refers to you? ex. (She is happy, He is working, They are dancing) | ")
        player_pn_verb = input("What is the associated verb? ex. (IS,ARE) | ")
        print(color.CYAN + 'You have selected custom pronouns.' + color.END)
    else:
        print("Looks like you picked a selection that was not a choice. We will work with custom pronouns. Feel free to put whatever pronouns you like.")
        player_pn_poss=input("What pronouns do you use in place of possession? ex. (Her hat, His wand,Their gold) | ")
        if player_pn_poss == "":
            print(color.RED + 'Inputs must be included in custom pronouns. Please try again.' + color.END)
            return(get_player_identity(color))
        player_pn_subj=input("What pronouns do you use when someone refers to your? ex. (She is happy, He is working, They are dancing) | ")
        if player_pn_poss == "":
            print(color.RED + 'Inputs must be included in custom pronouns. Please try again.' + color.END)
            return(get_player_identity(color))
        player_pn_verb=input("What is the associated verb? ex. (IS,ARE) | ")
        if player_pn_verb == "":
            print(color.RED + 'Inputs must be included in custom pronouns. Please try again.' + color.END)
            return(get_player_identity(color))
        print(color.CYAN + 'You have selected custom pronouns.' + color.END)
    return player_pn_poss, player_pn_subj, player_pn_verb

def tutorial(color,shopkeeper_name,SHPKPR):
    print(color.DARKCYAN + "Shopkeeper "+shopkeeper_name+" nods and suddenly dips behind the counter in search of something. As you stand around, you can't help but shake the feeling that you are being watched." + color.END)
    sleep(0.1)
    print(color.DARKCYAN + "After a few moments of rummaging, "+shopkeeper_name+" pulls a large tome from behind the counter. They place it in front of you." + color.END)
    sleep(0.1)
    print("\nThis is the tutorial for Shopkeeper.py. The instructions are simple.\n You are an adventurer on a small quest given by me.\n I will send you out to slay a number of beasts.\n A beast may drop items that you may sell to me, or chose not to.\n I have my own inventory that you may buy from to aid you in your quest, or chose not to.\n You have an inventory, a series of interactions and a relationship system that you will need to keep tabs on.\n Nothing too crazy for now, but something to keep in mind for the future.\n")
    sleep(0.2)
    tutorial_cont= input("Would you like to hear about formatting? | y/N | ")
    if tutorial_cont.lower().startswith('y'):
        print("Formatting is as follows:\n")
        print(color.DARKCYAN + " Actions and decisions will be notated in dark cyan." + color.END)
        print(color.GREEN + " Positive status effects, Relationship effects and combat-based bonuses will be displayed in green." + color.END)
        print(color.RED + " Negative status effects, relationship effects and combat-based bonuses will be displayed in red.\n" + color.END)
    tutorial_cont = input("Would you like to hear about decisions? | y/N | ")
    if tutorial_cont.lower().startswith('y'):
        print("Occasionally, in the story, you will have an opportunity to make decsions which impact your outcomes.\n Decisions to perform actions/say things will be listed as numbers 1-5 which you will be able to select.")
        print("Please note that if you select a number that is not a decision listed, the game will assume you did not say anything and move on with the prompt.")
    sleep(1)
    print("This concludes the tutorial")
    sleep(1)
    input("Press Enter to continue...")
    print("Exiting tutorial...\n")
    sleep(1)

def start_quest(SHPKPR,color,shopkeeper_name):
    shpkpr_store_intro = ["Tips tricks and oddities at your service!","My potions turn tricks so you don\'t have to!","The finest magic shop in all of town!","The best mage in name and in shop.","The magic shop with all your enchanting delights.","The only magic shop worth going to in this economy!","The best shop for magicks, mysticicm and enchantments."]
    beast_log = ['Lesser Wisp','Small Imp','Feral Rat','Gremlin']
    start_quest_beast = random.choice(beast_log)
    if SHPKPR == 0:
        print(color.DARKCYAN + shopkeeper_name+" leans over the counter, drumming their fingers impatiently." + color.END)
    if SHPKPR == 1:
        print(color.DARKCYAN + shopkeeper_name+" leans over the counter, tilting their head in curiosity." + color.END)
    sleep(0.)
    print("Welcome to shop "+shopkeeper_name+". "+random.choice(shpkpr_store_intro)+" You must be the mercenary I've requested!\n")
    dialogue = input("1. That's me. I'm the merc.\n2. Indeed. \n3. It's so nice to meet you! Here to be of service.\n4. What of it?\n5. READY TO KILL ON COMMAND MY MASTER\n")
    if dialogue == '1':
        shopkeeper_stats.SHPKPR = SHPKPR + 1
        print(color.GREEN+shopkeeper_name+" likes your tone. Your relationship improves a bit."+ color.END)
        print("Good. Well then-- I'll get right to it. Having the best shop in town means that I need to obtain the best ingredients in town. Unfortunately, the "+start_quest_beast+"s have been wreaking havoc on the caves that I scour to collect my ingredients...")
        shopkeeper_stats.dialogger.append(dialogue)
    elif dialogue =='2':
        print(color.GREEN+" A very serious mercenary. "+shopkeeper_name+" nods in approval."+ color.END)
        print("I can tell you are eager to start. I have hired you to do a bit of 'spring cleaning'. Unfortunately, the "+start_quest_beast+"s have been wreaking havoc on the caves that I scour to collect my ingredients...")
        shopkeeper_stats.dialogger.append(dialogue)
    elif dialogue =='3':
        shopkeeper_stats.SHPKPR = SHPKPR + 2
        print(color.GREEN + "Your sweetness does not go unnoticed. " + shopkeeper_name + " beams. You can already see they are warming up to you.."+ color.END)
        print("Splendid! Happy to hear it, comrade! I've hired you because as passionate as I am about my job as a shopkeeper, the "+start_quest_beast+"s outside of the town have infested the caves that I scour to collect my ingredients...")
        shopkeeper_stats.dialogger.append(dialogue)
    elif dialogue =='4':
        shopkeeper_stats.SHPKPR = SHPKPR - 1
        print(color.GREEN + " Rude! " + shopkeeper_name + " frowns at your reaction."+ color.END)
        print("I can tell you are eager to start. I've hired you to manage the recent infestation of " + start_quest_beast + "s that have been seen in the area. They've been wreaking havoc on the caves that I scour to collect my ingredients...")
        shopkeeper_stats.dialogger.append(dialogue)
    elif dialogue =='5':
        shopkeeper_stats.SHPKPR = SHPKPR + 4
        print(color.GREEN + "Ok, weird. Lucky for you, the shopkeeper " + shopkeeper_name + " is very much into that kind of devotion. You can tell they like it, and they like you alot."+ color.END)
        print("Oho, alright then. Well, that's great to hear. I've hired you because of the recent uptick in " + start_quest_beast + "s that have been seen in the area. They've been wreaking havoc on the caves that I scour to collect my ingredients I prepare for the shop...")
        shopkeeper_stats.dialogger.append(dialogue)
    else:
        shopkeeper_stats.dialogger.append(0)
        print(color.DARKCYAN + "You did not select a choice that was provided. You stand there, petrified and glassy-eyed. You look quite disturbing."+ color.END)
        print("Al-right... well, I uh... I've hired you because of the recent uptick in " + start_quest_beast + "s that have been seen in the area. They've been swarming the caves that I scour to collect my ingredients I prepare for the shop...")
    dialogue = input("1. And I take it you want me to get rid of them?\n2. Ugh... \n3.W-wait, " + start_quest_beast +"??? Nobody said anything about those. I am terrified of them!\n4. I am sworn to the protection of the land. You need not worry.\n5."+start_quest_beast.upper()+"S! THE MERCENARY SCHOOL DID NOT INFORM ME I WOULD BE FIGHTING SOMETHING SO PUNY.\n")
    if dialogue == '1':
        print(color.DARKCYAN + shopkeeper_name+" nods. They wave their hand vaguely in the direction of the door."+ color.END)
        print("That's right. I may be a mage, but fighting isn't exactly my style, you see. I figure it' better to hire someone for the job than to get my own hands dirty. You understand, don't you?")
        shopkeeper_stats.dialogger.append(dialogue)
    elif dialogue == '2':
        shopkeeper_stats.SHPKPR = SHPKPR -2
        print(color.DARKCYAN + shopkeeper_name+" blinks. Did you just groan at the shopkeeper?"+ color.END)
        print(color.RED + " Rude. You can tell the shopkeeper does not like your tone."+ color.END)
        print("If hunting monsters is not your preference, then perhaps you should not label yourself as a mercenary. Eitherway, you've already been hired for the job, so there's no use trying to back out of it now.")
        shopkeeper_stats.dialogger.append(dialogue)
    elif dialogue == '3':
        shopkeeper_stats.SHPKPR = SHPKPR +1
        print("Fear? Mercenaries have fears? Why be a mercenary if you have fears? I certainly hope its to help the less fortunate and not soley for coin, because then this job is most definitely not worth it.")
        shopkeeper_stats.dialogger.append(dialogue)
    elif dialogue == '4':
        shopkeeper_stats.SHPKPR = SHPKPR +2
        print(color.GREEN + shopkeeper_name + " smiles widely. There's approval in their tone."+ color.END)
        print("Isn't that lovely. Alright then. It's rare to see such a pure-hearted mercenary these days. Most mercs are after coin and don't care at all who they're helping or hurting. I'm pleased to have met you, adventurer.")
        shopkeeper_stats.dialogger.append(dialogue)
    elif dialogue == '5':
        shopkeeper_stats.SHPKPR = SHPKPR +5
        print(color.GREEN + " Slow down speed racer, you're flustering the shopkeeper with those big strong words. "+ shopkeeper_name + " appears to be stammering over their words. An embarrassed blush crosses their face. " + color.END)
        print("Oh-oh. Well alright. If you're that confident, then we should get started with preparing you for the trip...")
        shopkeeper_stats.dialogger.append(dialogue)
    else:
        shopkeeper_stats.dialogger.append(0)
        shopkeeper_stats.SHPKPR = SHPKPR -1
        print(color.RED + "You stare awkwardly at eachother."+ color.END)
        print("Erm... alright. I assume from your silence that you do not object to the terms of the quest.")
    return start_quest_beast

def start_quest_prep(SHPKPR,color,shopkeeper_name,GOLD):
    print("It appears that you have "+ str(GOLD) +" gold in your inventory. Ask me how I know? Magic. I have a few things in my inventory I could potentially.... sell to you, to make your quest go alot easier. What do you say?")
    dialogue = input(
        '''1. I'm trying to help you and you are trying to sell me something?
        2.Yes please!
        3.No thankyou, I have all that I need.\n4.What do you have?\n''')
    if dialogue == '1':
        print ("Well, I AM a shopkeeper. I do what I can, and I keep the shop. These bills certainly do not pay themselves.")
        show_wares(color)
    elif dialogue == '2':
        print ("Fantastic. Let me show you my wares!")
        SHPKPR = SHPKPR + 1
        return SHPKPR
        show_wares()
    elif dialogue == '3':
        print ("Oh, are you sure? That seems like a foolish thing to do. But you ARE a mercenary, and this certainly is not your first boss fight EVER. That would be silly. You know what you're doing.")
        start_questline()
    elif dialogue == '4':
        print("Potions, armor, magicks... let me show you my wares.")
        show_wares()
    else:
        print(color.RED + "You stare at the shopkeeper "+ shopkeeper_name +". They frown deeper at your lack of response."+ color.END)
        print("Well... let me show you my wares, so that you might see something that you like.")
        show_wares()

def show_wares():
    print(color.DARKCYAN + " The shopkeeper raises a hand to show the shelves behind them, filled with magical paraphenalia." + color.END)

def start_questline():
    print("Start questline")

introduction_1 = "WELCOME TO SHOPKEEPER.PY"
for char in introduction_1:
    sleep(0.1)
    print(char, end='') # do not need to flush here, can just print characters with associated sleep timer
    # sys.stderr.write(char)
    # sys.stdout.flush()
print(" ")
print("Welcome to the shop, traveller.")
sleep(2)
print("We've spent quite a bit of time together, haven't we? As you can see, we've rebranded quite a bit.")
sleep(2)

player_name, shopkeeper_name= get_player_data(shopkeeper_stats.shopkeeper_name, shopkeeper_stats.SHPKPR, shopkeeper_stats.color)
player_pn_poss, player_pn_verb, player_pn_subj = get_player_identity(shopkeeper_stats.color)
tutorial_start = input("Wonderful. That looks like we have all the information to start. Would you like to begin the tutorial, "+player_name.title()+"? Or are you already fluent? | y/N | ")
if tutorial_start.lower().startswith('y'):
    print(shopkeeper_stats.color.DARKCYAN + "You inform shopkeeper " + shopkeeper_name + " that you would like the tutorial.\n" + shopkeeper_stats.color.END)
    tutorial(shopkeeper_stats.color, shopkeeper_name, shopkeeper_stats.SHPKPR)
else:
    print(shopkeeper_stats.color.DARKCYAN + "You inform shopkeeper " + shopkeeper_name + " that you do not require any tutorial.\n" + shopkeeper_stats.color.END)
start_quest_beast = start_quest(shopkeeper_stats.SHPKPR, shopkeeper_stats.color, shopkeeper_name)
shopkeeper_stats.SHPKPR = start_quest_prep(shopkeeper_stats.SHPKPR, shopkeeper_stats.color, shopkeeper_name, shopkeeper_stats.GOLD)
print(shopkeeper_stats.dialogger)
print(shopkeeper_stats.SHPKPR)
