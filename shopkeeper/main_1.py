#!usr/bin/env python3
#shopkeeper.py
#introduces prompt script which askes your name, your preferred pronouns and your age.
# get player data needs to be slip eventually between name and gender, so if yo umake a mistake you dont have to start over

import sys
import random
import helper_1 as helper
import csv
from time import sleep

def get_player_data(shopkeeper_name,SHPKPR,color):
    shopkeeper_names = ['Landriel', 'Kip', 'Marinas', 'Undine', 'Elgis', 'Lojnar']
    shopkeeper_commentary = ['You must not be from around here.','It has a nice ring to it.','That\'s a fun name.',"I believe I had a cousin by that name. An odd one.","It reminds me of a story I heard once.","The name of a real warrior."]
    if shopkeeper_name == 'NULL':
        shopkeeper_name=random.choice(shopkeeper_names)
    print("My name is "+shopkeeper_name+". Before I introduce you to the shop, I shall ask you a number of clarifying questions.")
    player_name = input("To start, what is your name? | ")
    response = input(player_name.title()+" is it? Is that correct? | y/N | ")
    if response.lower().startswith('y'):
        if player_name.lower() == shopkeeper_name.lower():
            print("Is that so! Looks like we have the same name. Would you look at that!")
            helper.SHPKPR = SHPKPR + 1
            print(color.GREEN + 'Your relationship has increased, with '+shopkeeper_name+' but only a little!' + color.END)
            return(player_name)
        else:
            print(player_name.title()+". "+random.choice(shopkeeper_commentary))
    else:
        print("Let's try again then.")
        return(get_player_data(shopkeeper_name, SHPKPR, color))
    sleep(2)
def get_player_identity(color):
    player_pn = input('What are your preferred pronouns? Please type the corresponding number with your desired pronouns. |\n 1:He/him \n 2.She/her \n 3.They/Them \n 4.[custom]\n')
    if player_pn == "1":

        print(color.CYAN + 'You have selected masculine pronouns' + color.END)
        player_pn_poss= 'his'
        player_pn_subj= 'he'
        player_pn_verb= 'is'
    elif player_pn == "2":
        print(color.CYAN + 'You have selected feminine pronouns' + color.END)
        player_pn_poss= 'her'
        player_pn_subj= 'she'
        player_pn_verb= 'is'
    elif player_pn == "3":
        print(color.CYAN + 'You have selected gender neutral pronouns' + color.END)
        player_pn_poss= 'their'
        player_pn_subj= 'they'
        player_pn_verb= 'are'
    elif player_pn == "4":
        player_pn_poss=input("What pronouns do you use in place of possession? ex. (Her hat, His wand,Their gold) | ")
        player_pn_subj=input("What pronouns do you use when someone refers to your? ex. (She is happy, He is working, They are dancing) | ")
        player_pn_verb=input("What is the associated verb? ex. (IS,ARE) | ")
        print(color.CYAN + 'You have selected custom pronouns' + color.END)
        return(player_pn_poss,player_pn_subj,player_pn_verb)

def tutorial():
    print(color.DARKCYAN + shopkeeper_name+" nods and suddenly dips behind the counter in search of something. As you stand and watch, t" + color.END)

introduction_1 = "WELCOME TO SHOPKEEPER.PY"
for char in introduction_1:
    sleep(0.1)
    sys.stderr.write(char)
    sys.stdout.flush()  #flushes out the intro
print(" ")

print("Welcome to the shop, traveller.")
sleep(2)
print("We've spent quite a bit of time together, haven't we? As you can see, we've rebranded quite a bit.")
sleep(2)
get_player_data(helper.shopkeeper_name, helper.SHPKPR, helper.color)
get_player_identity(helper.color)
tutorial_start= input("Wonderful. That looks like we have all the information to start. Would you like to begin the tutorial, "+get_player_data.player_name+"? y/N | ")
if tutorial_start.lower().startswith('y'):
    tutorial()
if SHPKPR == 0:
    print(color.DARKCYAN + shopkeeper_name+" leans over the counter, and drums their fingers impatiently." + color.END)
if SHPKPR == 1:
    print(color.DARKCYAN + shopkeeper_name+" leans over the counter, tilting head in curiosity." + color.END)
input('1. THIS IS A TEST')
