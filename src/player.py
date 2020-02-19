# Write a class to hold player information, e.g. what room they are in
# currently.

class Player:
    def __init__(self, name, skill, current_room):
        self.skill = skill
        self.current_room = current_room
    
    def __str__(self):
        output = f'{self.name} on {self.current_room.name}'
        ats = dir(self)
        output += ats
        return output
    
    def setroom(self, room):
        self.current_room = room
        print(f'You are now in {self.current_room}!\n')
    def look(self):
        print(f"""{self.current_room.description} """)

    

