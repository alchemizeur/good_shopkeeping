import random
from class__game_item import GameItem
from class__character import Character


# Randomized Greetings
GREETINGS = [
    "Ah {name}, you will do great things, I can just tell.",
    "An interesting name, {name}. It's suitable for a mercenary, no?",
    "What's in a name? Certainly a lot in {name}.",
    "{name}, a name that whispers of destiny.",
    "{name}, your journey begins here."]

def create_character():
    while True:
        name = input("Enter your character's name: ").strip().title()
        if len(name) > 1 and not name.isspace():
            break
        print("Name must be more than one character and cannot be empty or just spaces.")

    print(random.choice(GREETINGS).format(name=name))
    print("\n")

    print("Choose your gender expression:")
    print("1. Solar Aspect (Masculine)")
    print("2. Lunar Aspect (Feminine)")
    print("3. Ethereal Aspect (Neutral)")
    while True:
        gender_choice = input("Enter the number corresponding to your choice: ")
        genders = {"1": "Solar Aspect", "2": "Lunar Aspect", "3": "Ethereal Aspect"}
        if gender_choice in genders:
            gender_expression = genders[gender_choice]
            break
        print("Invalid choice. Please choose 1, 2, or 3.")

    print("Choose your class:")
    print("1. Merchant")
    print("2. Blacksmith")
    print("3. Alchemist")
    while True:
        class_choice = input("Enter the number corresponding to your choice: ")
        classes = {"1": "Merchant", "2": "Blacksmith", "3": "Alchemist"}
        if class_choice in classes:
            char_class = classes[class_choice]
            break
        print("Invalid choice. Please choose 1, 2, or 3.")

    while True:
        print("\nConfirm your character details:")
        print(f"Name: {name}")
        print(f"Gender Expression: {gender_expression}")
        print(f"Class: {char_class}")
        confirmation = input("Are these details correct? (yes/no): ").strip().lower()

        if confirmation == "yes":
            return Character(name=name, char_class=char_class, gender_expression=gender_expression)
        elif confirmation == "no":
            print("\nWhich detail would you like to change?")
            print("1. Name")
            print("2. Gender Expression")
            print("3. Class")
            change_choice = input("Enter the number corresponding to your choice: ").strip()

            if change_choice == "1":
                while True:
                    name = input("Enter your character's new name: ").strip()
                    if len(name) > 1 and not name.isspace():
                        break
                    print("Name must be more than one character and cannot be empty or just spaces.")

            elif change_choice == "2":
                print("Choose your gender expression:")
                print("1. Solar Aspect (Masculine)")
                print("2. Lunar Aspect (Feminine)")
                print("3. Ethereal Aspect (Neutral)")
                while True:
                    gender_choice = input("Enter the number corresponding to your choice: ")
                    if gender_choice in genders:
                        gender_expression = genders[gender_choice]
                        break
                    print("Invalid choice. Please choose 1, 2, or 3.")

            elif change_choice == "3":
                print("Choose your class:")
                print("1. Merchant")
                print("2. Blacksmith")
                print("3. Alchemist")
                while True:
                    class_choice = input("Enter the number corresponding to your choice: ")
                    if class_choice in classes:
                        char_class = classes[class_choice]
                        break
                    print("Invalid choice. Please choose 1, 2, or 3.")
        else:
            print("Invalid input. Please enter 'yes' or 'no'.")