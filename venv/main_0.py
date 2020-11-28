#!usr/bin/env python3
# chat sim pt 2 -- similar, but with better functions

import time
from datetime import datetime
# import helper_0

def get_chatbot_name(chatbot_name): ## this is the same name as the variable because this isnt really beiing used in anything else
    check_name: str = input(" Do you want to give me a name? (y/N)| ")
    if check_name.lower().startswith('y'):
        chatbot_name: str = input("Ok! What would you like to name me? | ")
        chatbot_name = chatbot_name.title()
        check_name: str = input("My name is " + chatbot_name+"! Do you like that name? Y/n")
        if check_name.lower().startswith('n'):
            get_chatbot_name(chatbot_name)
        elif check_name.lower().startswith('y'):
            return(chatbot_name) # AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA WHAT THE FUCK
    else:
        print("Alright, suit yourself. I'll just name myself.")
    print(chatbot_name)
##    chatbot_name = chatbot_name[0] #forgive me for i have sinned
    print(chatbot_name+ " second run")
    return chatbot_name

print('Welcome to the testing mad libs!')
time.sleep(1)
print("We\'ve gotten so far!") ## escape for apostrophes
time.sleep(1)
print("We\'ve managed to get a script to work. But obviously there are more conversations to be had. You don't know anything about me.")
time.sleep(3)
print("Hmmmm...")
chatbot_name = get_chatbot_name("Chatbot") ## default name
print("My name is " + chatbot_name+"! You can call me "+chatbot_name[0]+". It's nice to meet you!")
time.sleep(1)
now = datetime.today()
dow = datetime.today().weekday()
print("Today's date:", now)
print("Today's date:", dow)






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