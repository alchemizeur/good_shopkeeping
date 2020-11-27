## Mad libs generator

import time

tps = ['year', 'minute', 'second', 'hour', 'decade', 'week', 'day', 'month', 'decade', 'centur', 'eons', 'forever', 'millen']

def start():
    print('welcome to the testing mad libs')
    time.sleep(1)
    print("This is going to be the first instance I test to see what I am capable of so be kind")
    time.sleep(3)
    print("So lets start with the basics...")
    time.sleep(1)
    name: str=input("What is your name? | ")
    print("Nice to meet you, "+name.title()+". It's pretty fun to work together like this, isn't it?")
    time.sleep(1)
    name: name.title() ## why wont this work?
    print(name)
    print("Anyway, onto the mad lib")
    time.sleep(1)
    friend_name: str=input("Name a person you know | ")
    friend_relationship: str=input("Aaaand this person is what to you? Your... | ")
    friend_gender: str = "them"
    if "boy" in friend_relationship.lower():
        friend_gender = 'him'
    elif "girl" in friend_relationship.lower():
        friend_gender = 'her'
    keep_swimming(name, friend_name, friend_relationship, friend_gender)

def keep_swimming(name,friend_name,friend_relationship,friend_gender):
    friends_length: str=input("How long did you know "+friend_gender+"? | ")
    if tps not in friends_length:
        friends_length: str=input(friends_length+"? What's that? Try giving me a more common time period.")
        keep_swimming(name,friend_name,friend_relationship,friend_gender)
    animal: str=input("Cute. "+friends_length+". got it. That's not very long for a robot, but I respect that. If you could be any animal what would you be? | ")
    if "a " in animal:
        animal = animal.replace('a ',"")
    animal_friend: str=input("Do you think that "+friend_name+" would be the same animal? | ")
    if animal_friend.lower().startswith('y'):
        animal_friend = animal
        print("Cute, you guys have so much in common.")
    else:
        print("lol. You guys aren't really friends if you wouldn't even be in the same animal family.")
        animal_friend: str = input("What would they be?")
        think(name,friend_name,friend_relationship,friend_gender,friends_length,animal_friend)

def think(name,friend_name,friend_relationship,friend_gender,friends_length,animal_friend):
    print("Ok... let me think...")
    time.sleep(1)
    print("Thinking...")
    time.sleep(1)
    print("Thinking...")
    time.sleep(1)
    print("Thinking...")
    time.sleep(3)
    print("So you, "+name+"... and your "+friend_relationship+", "+friend_name+", have been friends for "+friends_length+".")

    if animal_friend == animal:
        print ("Just two "+animal+ "s living it up in nature. That's all there is to it.")
    else:
        print ("Just a "+animal+" and a "+animal_friend+". You and "+friend+gender+". Cool. That's all I've got.")

    print("How did I do?")

start()
##    print("Great," + myName + '!')
##--else:
##  print ("Sorry for asking...")
