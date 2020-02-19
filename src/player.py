# Write a class to hold player information, e.g. what room they are in
# currently.

class Player:
    def __init__(self, name, skill, room):
        self.skill = skill
        self.room = room
    
    def __str__(self):
        output = f'{self.name} on {self.room.name}'
        return output
    
    def setroom(self, room):
        self.room = room
        print(f'You are now in {self.room}!\n')

