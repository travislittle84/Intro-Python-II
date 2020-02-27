# Implement a class to hold room information. This should have name and
# description attributes.

class Room:
    def __init__(self, name, description, feet, items = {}):
        self.name = name
        self.description = description
        self.feet = feet
        self.items = items
    
    def __str__(self):
        output = f'Room: {self.name}\n'
        output += f'Feet to Pin: {self.feet}\n'
        output += f'What do you see?:\n  {self.description}'
        return output
    def room_inventory(self):
        if len(self.items) == 0:
            print('You have no discs on the ground.')
        for item in self.items:
            print(f'You have a {self.items[item].name} on the ground')

    def get_room_inventory_list(self):
        list = [item for item in self.items]
        return list