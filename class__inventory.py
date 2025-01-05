import csv

class Inventory:
    def __init__(self):
        self.items = []

    def add(self, item, quantity=1):
        for _ in range(quantity):
            self.items.append(item)

    def remove(self, item_name, quantity=1):
        removed = 0
        for i in range(len(self.items) - 1, -1, -1):
            if self.items[i].name == item_name:
                removed += 1
                del self.items[i]
                if removed == quantity:
                    break

    def display(self):
        if self.items:
            inventory_summary = {}
            for item in self.items:
                if item.name in inventory_summary:
                    inventory_summary[item.name] += 1
                else:
                    inventory_summary[item.name] = 1

            for idx, (item_name, quantity) in enumerate(inventory_summary.items(), 1):
                print(f"{idx}. {item_name} x{quantity}")
        else:
            print("Inventory is empty.")

    def __iter__(self):
        return iter(self.items)

    def save_to_csv(self, file_path):
        with open(file_path, mode='w', newline='') as file:
            fieldnames = ["name", "summary", "type", "effects", "slot_space", "max_stack", "quantity"]
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()

            inventory_summary = {}
            for item in self.items:
                if item.name in inventory_summary:
                    inventory_summary[item.name]["quantity"] += 1
                else:
                    inventory_summary[item.name] = {
                        "name": item.name,
                        "summary": item.summary,
                        "type": item.type,
                        "effects": str(item.effects),
                        "slot_space": item.slot_space,
                        "max_stack": item.max_stack,
                        "quantity": 1
                    }

            for item_data in inventory_summary.values():
                writer.writerow(item_data)

    def load_from_csv(self, file_path, game_items):
        try:
            with open(file_path, mode='r') as file:
                reader = csv.DictReader(file)
                for row in reader:
                    item_name = row["name"]
                    quantity = int(row["quantity"])
                    if item_name in game_items:
                        item = game_items[item_name]
                        self.add(item, quantity)
        except FileNotFoundError:
            print(f"No inventory file found at {file_path}. Starting with an empty inventory.")