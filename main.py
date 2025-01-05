import os
import csv
import random
from character_confirmation import create_character
from class__game_item import GameItem

# Clear screen function
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

# Load and display title from text file
def display_title():
    clear_screen()
    try:
        with open("game_title.txt", "r") as title_file:
            print(title_file.read())
    except FileNotFoundError:
        print("game_title.txt")
    input("Press any key to continue...")
    clear_screen()

# Load Game Items from CSV
def load_game_items(filename="game_items.csv"):
    """Loads game items from a CSV file into a dictionary."""
    items = {}
    try:
        with open(filename, mode='r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                item = GameItem(
                    name=row["name"],
                    summary=row["summary"],
                    item_type=row["type"],
                    effects=eval(row["effects"]),  # Convert string to dictionary
                    slot_space=int(row["slot_space"]),
                    max_stack=int(row["max_stack"])
                )
                items[item.name] = item
    except FileNotFoundError:
        print("Game items file not found. Make sure 'game_items.csv' exists.")
    return items




# Main Game Loop
def main():
    # Load items from CSV
    display_title()

    game_items = load_game_items()
    if not game_items:
        return

    # Create character
    character = create_character()

    # Game loop
    while True:
        print("\nWhat would you like to do?")
        print("1. View Stats")
        print("2. View Inventory")
        print("3. Pick up a random item")
        print("4. Remove an item from inventory")
        print("5. Drop Item")
        print("6. Quit game")
        choice = input("Enter your choice: ")

        if choice == "1":
            # Display character stats
            character.display_stats()
        elif choice == "2":
            character.display_inventory()
        elif choice == "3":
            # Equip a random item (if game_items exists)
            if game_items:
                # Find a random item
                item = random.choice(list(game_items.values()))  # Fix for random selection
                quantity = random.randint(1, item.max_stack)
                print(f"You found {quantity} x {item.name}!")
                print({item.summary})

                # Add the item to the general inventory
                for _ in range(quantity):
                    if len(character.inventory) < character.inventory_slots:
                        character.add_to_inventory(item)
                    else:
                        print("Inventory is full! Cannot add more items.")
                        break

                # Offer to equip the item
                choice = input(f"Do you want to equip {item.name}? (yes/no): ").strip().lower()
                if choice == "yes":
                    slot = input("Which slot would you like to equip it to? (e.g., body, weapon_1, etc.): ").strip()
                    if slot in character.equipped_slots:
                        character.equip_item(slot, item)
                    else:
                        print("Invalid slot. The item remains in your inventory.")
        elif choice == "4":
            # Unequip an item
            slot = input("Enter the slot to unequip (e.g., body, weapon_1, etc.): ")
            if slot in character.equipped_slots and character.equipped_slots[slot]:
                removed_item = character.equipped_slots[slot]
                character.equipped_slots[slot] = None
                print(f"Unequipped {removed_item.name} from {slot}.")
            else:
                print("Invalid slot or no item equipped.")
        elif choice == "5":
            character.drop_item()
        elif choice == "6":
            print("Thanks for playing Good Shopkeeping!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()