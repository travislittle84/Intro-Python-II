# Implement a class to hold room information. This should have name and
# description attributes.

class Room:
    def __init__(self, name, description, difficulty, feet):
        self.name = name
        self.description = description
        self.difficulty = difficulty
        self.feet = feet
    
    def __str__(self):
        output = f'Room: {self.name}\n'
        output += f'Feet to Pin: {self.feet}\n'
        output += f'Difficulty: {self.difficulty}\n'
        output += f'What do you see?:\n{self.description}'
        return output
