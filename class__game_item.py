import csv

class GameItem:
    def __init__(self, name, summary, item_type, effects, slot_space, max_stack):
        self.name = name
        self.summary = summary
        self.type = item_type
        self.effects = effects
        self.slot_space = slot_space
        self.max_stack = max_stack
        self.current_stack = 0  # Default stack starts at 0

    @classmethod
    def from_dict(cls, data):
        return cls(
            name=data['name'],
            summary=data['summary'],
            item_type=data['type'],
            effects=eval(data['effects']),  # Convert JSON-like string to dictionary
            slot_space=int(data['slot_space']),
            max_stack=int(data['max_stack']),
        )

    def __repr__(self):
        return f"GameItem(name='{self.name}', type='{self.type}', slot_space={self.slot_space})"

