import os
from active_statuses import get_active_status


def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")


class Character:
    def __init__(self, name, char_class, gender_expression, inventory_slots=15):
        self.name = name
        self.char_class = char_class
        self.gender_expression = gender_expression

        # Core Stats
        self.vitality = 10
        self.max_vitality = 10  # Vitality (HP)
        self.grit = 10      # Grit (Stamina)
        self.brawn = 5      # Brawn (Strength)
        self.wit = 5        # Wit (Intelligence)
        self.finesse = 5    # Finesse (Dexterity)
        self.whimsy = 5     # Whimsy (Luck)
        self.charm = 5      # Charm (Charisma)
        self.fortune = 100  # Fortune (Gold)

        # Additional Stats
        self.title = None  # Title (default null)
        self.active_status = None  # Active status (default null)
        self.passive_status = None  # Passive status (default null)

        # Equipped items and general inventory
        self.equipped_slots = {
            "body": None,
            "shoes": None,
            "weapon_1": None,
            "weapon_2": None,
            "hat": None,
            "accessory_1": None,
            "accessory_2": None,
            "back": None,
            "gloves": None,
            "belt": None,
            "pet": None
        }
        self.inventory = []  # General inventory for unequipped items
        self.inventory_slots = inventory_slots  # Limit for general inventory


    def display_stats(self):
        clear_screen()  # Clear the screen before displaying stats

        # Use functions from passive_statuses.py
        self.active_status = get_active_status(self)

        print(f"\n\n{self.name}'s Stats:")
        print(f"Class: {self.char_class}")
        print(f"Gender Expression: {self.gender_expression}")
        print(f"Vitality (HP): {self.vitality}")
        print(f"Grit (Stamina): {self.grit}")
        print(f"Brawn (Strength): {self.brawn}")
        print(f"Wit (Intelligence): {self.wit}")
        print(f"Finesse (Dexterity): {self.finesse}")
        print(f"Whimsy (Luck): {self.whimsy}")
        print(f"Charm (Charisma): {self.charm}")
        print(f"Fortune (Gold): {self.fortune}")
        print(f"Title: {self.title if self.title else 'None'}")
        print(f"Active Status: {self.active_status if self.active_status else 'None'}")
        print(f"Passive Status: {self.passive_status if self.passive_status else 'None'}")
        print("Equipped Items:")
        for slot, item in self.equipped_slots.items():
            print(f"  {slot}: {item.name if item else 'None'}")
        print()

    def add_to_inventory(self, item):
        if len(self.inventory) < self.inventory_slots:
            self.inventory.append(item)
            print(f"Added {item.name} to inventory.")
        else:
            print("Inventory is full.")

    def remove_item(self, item_name):
        # Check general inventory
        for i, item in enumerate(self.inventory):
            if item.name == item_name:
                print(f"Found {item_name} in general inventory.")
                choice = input("Would you like to (1) Drop and Destroy or (2) Keep in Inventory? ").strip()
                if choice == "1":
                    del self.inventory[i]
                    print(f"{item_name} dropped and destroyed.")
                    return
                elif choice == "2":
                    print(f"{item_name} remains in your inventory.")
                    return
                else:
                    print("Invalid choice.")
                    return

        # Check equipped slots
        for slot, item in self.equipped_slots.items():
            if item and item.name == item_name:
                print(f"Found {item_name} equipped in {slot}.")
                choice = input("Would you like to (1) Unequip to Inventory, (2) Drop and Destroy? ").strip()
                if choice == "1":
                    self.unequip_item(slot)
                    return
                elif choice == "2":
                    self.equipped_slots[slot] = None
                    print(f"{item_name} dropped and destroyed.")
                    return
                else:
                    print("Invalid choice.")
                    return

        print(f"Item {item_name} not found.")

    def equip_item(self, slot, item):
        clear_screen()  # Clear the screen before equipping an item
        if slot in self.equipped_slots:
            if self.equipped_slots[slot] is None:  # Only show summary if slot was empty
                print(f"{item.name}: {item.summary}")  # Display item summary
            self.equipped_slots[slot] = item
            print(f"Equipped {item.name} to {slot}.")
        else:
            print("Invalid slot.")

    def unequip_item(self, slot):
        if slot in self.equipped_slots and self.equipped_slots[slot]:
            item = self.equipped_slots[slot]
            self.equipped_slots[slot] = None
            self.add_to_inventory(item)
            print(f"Unequipped {item.name} from {slot}.")
        else:
            print("No item to unequip or invalid slot.")

    def drop_item(self, item_name):
        for i, item in enumerate(self.inventory):
            if item.name == item_name:
                del self.inventory[i]
                print(f"Dropped {item_name}.")
                return
        print(f"Item {item_name} not found in inventory.")

    def display_inventory(self):
        clear_screen()  # Clear the screen before displaying inventory
        print("\nInventory Overview:")

        # Display Equipped Items
        print("Equipped Items:")
        for slot, item in self.equipped_slots.items():
            print(f"  {slot}: {item.name if item else 'None'}")

        # Display General Inventory
        print("\nGeneral Inventory:")
        if self.inventory:
            for idx, item in enumerate(self.inventory, 1):
                print(f"{idx}. {item.name} ({item.type})")
        else:
            print("Inventory is empty.")
        print(f"Available Slots: {self.inventory_slots - len(self.inventory)}\n")

        # Write inventory to file
        with open(f"{self.name}_inventory.txt", "w") as file:
            file.write("Equipped Items:\n")
            for slot, item in self.equipped_slots.items():
                file.write(f"{slot}: {item.name if item else 'None'}\n")
            file.write("\nGeneral Inventory:\n")
            for item in self.inventory:
                file.write(f"{item.name} ({item.type})\n")
        print(f"Inventory written to {self.name}_inventory.txt")

    def equip_from_inventory(self):
        clear_screen()  # Clear the screen for readability
        if not self.inventory:
            print("Your inventory is empty. Nothing to equip.")
            return

        print("Select an item to equip:")
        for idx, item in enumerate(self.inventory, 1):
            print(f"{idx}. {item.name} ({item.type})")

        choice = input("Enter the number of the item to equip: ")
        try:
            index = int(choice) - 1
            if 0 <= index < len(self.inventory):
                item = self.inventory.pop(index)
                slot = input("Enter the slot to equip this item to: ")
                if slot in self.equipped_slots:
                    self.equipped_slots[slot] = item
                    print(f"Equipped {item.name} to {slot}.")
                else:
                    print("Invalid slot. Returning item to inventory.")
                    self.add_to_inventory(item)
            else:
                print("Invalid choice.")
        except ValueError:
            print("Please enter a valid number.")

    def consume_food(self):
        clear_screen()  # Clear the screen for readability
        food_items = [item for item in self.inventory if item.type == "Food"]

        if not food_items:
            print("You have no food items in your inventory.")
            return

        print("Select a food item to consume:")
        for idx, item in enumerate(food_items, 1):
            print(f"{idx}. {item.name} ({item.type}) - Effects: {item.effects}")

        choice = input("Enter the number of the food item to consume: ")
        try:
            index = int(choice) - 1
            if 0 <= index < len(food_items):
                item = food_items[index]
                self.vitality += item.effects.get("HP", 0)  # Apply healing effect
                self.vitality = min(self.vitality, self.max_vitality)  # Cap at max vitality
                self.inventory.remove(item)
                print(f"Consumed {item.name}. Vitality is now {self.vitality}/{self.max_vitality}.")
            else:
                print("Invalid choice.")
        except ValueError:
            print("Please enter a valid number.")
