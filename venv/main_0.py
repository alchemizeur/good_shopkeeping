#!usr/bin/env python3
# chat sim pt 2 -- similar, but with better functions

import time
import random
from datetime import datetime,timedelta
import calendar
import webbrowser
# import helper_0 ##this is not needed yet

def get_chatbot_name(chatbot_name): ## this is the same name as the variable because this isnt really beiing used in anything else
    random_names = ['Chatbot', 'Pepper Corn', 'Pasta Sauce', 'Undine', 'Juggernaut', 'Siri']
    check_name: str = input(" Do you want to give me a name? (y/N) | ")
    if check_name.lower().startswith('y'):
        chatbot_name: str = input("Ok! What would you like to name me? | ")
        chatbot_name = chatbot_name.title()
        check_name: str = input("Hmmm... " + chatbot_name+"! I like that. It kind of has a nice ring to it. Do you like that name? Y/n | ")
        if check_name.lower().startswith('n'):
            print("Hmmm... well, ok. Let's try again.")
            return(get_chatbot_name(chatbot_name))
        elif check_name.lower().startswith('y'):
            return(chatbot_name)
    else:
        print("Alright, suit yourself. I'll just name myself.")
        chatbot_name = random.choice(random_names)
        return(chatbot_name)
    print(chatbot_name)
##    chatbot_name = chatbot_name[0] #forgive me for i have sinned
    print(chatbot_name+ " second run")
    return chatbot_name

def get_date_now():
    now = datetime.today()
    dow = datetime.today().weekday()
    days = {name: i for i, name in enumerate(calendar.day_name)}
    key_list = list(days.keys())
    val_list = list(days.values()) ## i know this is messy idk what else to do and it works
    todays_date = str(key_list[val_list.index(dow)])

    day_checker: str = input("Do you know what today's day is? y/n | ")
    if day_checker.lower().startswith('y'):
        your_day: str = input("What is it? | ")
        if your_day.lower() == todays_date.lower():
            print ("Ah yes! I remember! Today is "+todays_date+" isn't it. That's definitely correct.")
        else:
            print("Hmmm. Are you sure? That doesn't sount right.")
            time.sleep(1)
            print("You've got your days all mixed up. Today is "+todays_date+(datetime.today().date())+". I just checked.")
    else:
        print ("That's ok. I know the day. Today is "+todays_date+"!") ## the most diff thing ive ever written
        return

def get_snacks(time_rn,todayy):
    ## forgive me for i have sinned
#    print(list(datedict.keys())[0])
#    date_parser(time_rn,todayy) i tried to make this into a dictionary and it didnt work ):
    range1 = datetime.strptime(todayy.strftime("%Y-%m-%d") + " 05:00:00", "%Y-%m-%d %H:%M:%S")
    range2 = datetime.strptime(todayy.strftime("%Y-%m-%d") + " 11:00:00", "%Y-%m-%d %H:%M:%S")
    range3 = datetime.strptime(todayy.strftime("%Y-%m-%d") + " 14:00:00", "%Y-%m-%d %H:%M:%S")
    range4 = datetime.strptime(todayy.strftime("%Y-%m-%d") + " 20:00:00", "%Y-%m-%d %H:%M:%S")
    range5 = datetime.strptime(todayy.strftime("%Y-%m-%d") + " 12:59:59", "%Y-%m-%d %H:%M:%S")
    range6 = datetime.strptime(todayy.strftime("%Y-%m-%d") + " 00:00:00", "%Y-%m-%d %H:%M:%S")

    if time_rn >= range1 and time_rn < range2:
        snacktime = 'breakfast'
    elif time_rn >= range2 and time_rn < range3:
        snacktime = 'lunch'
    elif time_rn >= range3 and time_rn < range4:
        snacktime = 'dinner'
    elif time_rn >= range4 and time_rn < range5:
       snacktime = 'late night snackies'
    elif time_rn >= range5 and time_rn < range6:
        snacktime = 'early morning snackies'

    print("I'm pretty hungry. I could really use some "+snacktime+".")
    return snacktime

def cooking_mama(snacktime):
    rand_foods = ['sweet','savory','spicy','healthy','unhealthy','crispy']
    idks = ["don't know","idk","no idea","not a clue","unno","no clue"]
    can_u_cook: str = input("Do you know how to make "+snacktime+"? | ")
    random_choice_food = random.choice(rand_foods)
    if can_u_cook.lower().startswith('y'):
        food_u_make: str = input("Yes! Splendid! What will you make? | ")
        if food_u_make.lower() in idks:
            print("Thats ok. I am craving something"+rand_foods+". Lets look that up!")
            time.sleep(1)
            webbrowser.open('https://www.google.com/search?q=easy+to+make+' + rand_foods + 'recipes')
        print("I've never had "+food_u_make.lower()+" before. Sounds delicious!")
    elif can_u_cook.lower().startswith('n'):
        print("Yikes. I can't believe you would admit that. I reccomend going on google and figuring that out.")
        time.sleep(1)
        webbrowser.open('https://www.google.com/search?q=easy+recipes+for+someone+who+cant+cook')
    else:
        print("I don't understand. But I am craving something"+rand_foods+". Lets look that up!")
        time.sleep(1)
        webbrowser.open('https://www.google.com/search?q=easy+to+make+'+rand_foods+'recipes')


def date_parser(time_rn,todayy):## insanity
    ##idk man i went into a rabbit hole and now im in too deep
    range1 = todayy.strftime("%Y-%m-%d") + " 05:00:00"
    range2 = todayy.strftime("%Y-%m-%d") + " 11:00:00"
    range3 = todayy.strftime("%Y-%m-%d") + " 14:00:00"
    range4 = todayy.strftime("%Y-%m-%d") + " 20:00:00"
    range5 = todayy.strftime("%Y-%m-%d") + " 12:59:59"
    range6 = todayy.strftime("%Y-%m-%d") + " 00:00:00"

    datedict = {"range1": range1,
                "range2": range2,
                "range3": range3,
                "range4": range4,
                "range5": range5,
                "range6": range6}
    print(datedict)
    return datedict


print('Welcome to the testing mad libs!')
time.sleep(1)
print("We\'ve gotten so far!") ## escape for apostrophes
time.sleep(1)
print("We\'ve managed to get a script to work. But obviously there are more conversations to be had. You don't know anything about me.")
time.sleep(3)
print("Hmmmm...")
chatbot_name = get_chatbot_name("Chatbot") ## default name
print("My name is " + chatbot_name+"! You can call me "+chatbot_name[0]+". It's nice to meet you on this day!")
time.sleep(1)
print("Hmmmm...")
time.sleep(1)
dow=get_date_now()
todayy = (datetime.today().date())
time_rn = datetime.now()
# datedict=date_parser(time_rn,todayy)
snacktime = get_snacks(time_rn,todayy)
cooking = cooking_mama(snacktime)







## Psuedocode
## Application introduces itself. Realizes it doesn't have a name. Asks if you would like to name it
## yes/no.
## if yes, then you can name it whatever
## if no, then it names itself chatbot
## it asks you your name
## asks you are you sure? you can change it at this point
## chatbot asks you what todays day is
## if you get it right, then it states it remembers!
## if you say the wrong day, then it says that doesnt sound right. Corrects you.
## if you say something that isnt a day. It calls you crazy. Say it doesnt sound right, and then corrects you.
## if you say you dont know, then it laughs and checks for you.
## if its morningtime, it says its hungry and would like breakfast. If its afternoon, it wants lunch. If its evening, it wants dinner. If its midnight. It wants a late night snack
## It asks you if you know how to cook. Y/n
## if you can, then it says splendid! what will you make?
## cuts out any words that are prepositionary.
## makes a statement that they will make this food with you. A [morning,afternoon,evening,latenight] snack.


## def main()