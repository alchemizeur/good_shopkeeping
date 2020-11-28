#!/usr/bin/env python3
# Mad libs generator

import time

from helpers import *


def start():
    print('Welcome to the testing mad libs')
    time.sleep(1)
    print("This is going to be the first instance I test to see what I am capable of so be kind")
    time.sleep(1)
    print("So lets start with the basics...")
    time.sleep(1)

    name: str = input("What is your name? | ")
    print("Nice to meet you, " + name.title() + ". It's pretty fun to work together like this, isn't it?")
    time.sleep(1)
    name = name.title()

    print("Anyway, onto the mad lib")
    time.sleep(1)
    friend_name: str = input("Name a person you know | ")
    friend_relationship: str = input("Aaaand this person is what to you? Your... | ")
    friend_relationship = strip_identifiers(friend_relationship).title()

    friend_gender = "them"
    if "boy" in friend_relationship.lower():
        friend_gender = 'him'
    elif "girl" in friend_relationship.lower():
        friend_gender = 'her'

    return name, friend_name, friend_relationship, friend_gender


def keep_swimming(friend_name, friend_gender):
    while True:
        friends_length = input("How long did you know " + friend_gender + "? | ")
        if valid_time(friends_length):
            break
        else:
            print('What\'s that? Try giving me a known time unit. Years, Months, Days, etc. ')
    friends_length = strip_identifiers(friends_length)

    animal: str = input(
        "Cute. " + friends_length + ". got it. That's not very long for a robot, but I respect that. "
                                    "If you could be any animal what would you be? | ")
    animal = strip_identifiers(animal)

    while True:
        animal_friend: str = input("Do you think that " + friend_name.title() + " would be the same animal?  (y/n) | ")
        if animal_friend in ['y', 'n']:
            break
        else:
            print('please only respond with \'y\' or \'n\'')
    if animal_friend == 'y':
        animal_friend = animal
        print("Cute, you guys have so much in common.")
    else:
        print("lol. You guys aren't really friends if you wouldn't even be in the same animal family.")
        animal_friend: str = input("What would they be? | ")  ## need to incorporate gender better here

    return friends_length, animal_friend, animal


def think(name, friend_name, friend_relationship, friend_gender, friends_length, animal_friend, animal):
    print("Ok... let me think...")
    for _ in range(3):
        time.sleep(1)
        print('Thinking...')
    time.sleep(3)
    print(
        "So you, " + name + "... and your " + friend_relationship + ", "
        + friend_name + ", have been friends for " + friends_length + ".")

    if animal_friend == animal:
        print("Just two " + animal + "s living it up in nature. That's all there is to it.")
    else:
        print(
            "Just a " + animal + " and a " + animal_friend + ". You and " + friend_gender + ". Cool. That's all I've got.")

    print("How did I do?")


def main():
    name, friend_name, friend_relationship, friend_gender = start()
    friends_length, animal_friend, animal = keep_swimming(friend_name, friend_gender)
    think(name, friend_name, friend_relationship, friend_gender, friends_length, animal_friend, animal)


if __name__ == '__main__':
    main()
