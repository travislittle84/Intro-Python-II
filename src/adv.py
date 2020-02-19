from room import Room
from player import Player

# Declare all the rooms

room = {
    'parking_lot': Room("Parking Lot", 
                        """You're in the parking lot of your home course. The skies are clear and deep blue, 
winds are calm, about 70f. Perfect day for disc golf!

There are not many trees at this course, but there are some fairly long holes and tricky out of bounds.
The course is on a city open area park which is basically an unused field, if you end up off the fairway,
you will be contending with prickly bushes and high grass.

To the south of you is the entrance to the course.""", 0, 0),

    'hole1':  Room("Hole 1",
                     """Wide open shot with a guardian tree in front of the basket.
An out of bounds path runs along the right side of the fairway.""", 80, 354),

    'hole2':    Room("Hole 2", 
                        """Another wide open shot, slightly down hill. Guardian tree
in front of and slightly left. There is not much of a fairway, the terrain is rough 
until you reach circle 2. There is an OB path in front of the teepad but it's close 
enough to not worry about (hopefully)""", 60, 285),

    'hole3': Room("Hole 3",
                    """Looks are deceiving on this one. Easily the hardest hole 
on this course. Wide open, no trees. Elevation rise of a few feet, about 20ft in front of 
the teepad. OB creek long, extending the entire backside of the hole, all the way to cirlce 1. An OB and beyond 
path to the right of the entire hole. The path starts very far from the fairway, 
but it creeps up to the cirlce. Your approach shot and putt could be very dangerous.""", 50, 100),

    'hole4':   Room("Hole 4", """The narrow passage bends here from west
to north. The smell of gold permeates the air.""", 50, 100),

    'hole5': Room("Hole 5", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south.""", 50, 100),

    'hole6': Room("Hole 6", """Hole 6 Description """, 50, 100)
}


# Link rooms together

# Parking Lot
room['parking_lot'].s_to = room['hole1']
room['parking_lot'].w_to = room['hole6']
room['parking_lot'].n_to = None
room['parking_lot'].e_to = None

# Hole 1
room['hole1'].n_to = room['parking_lot']
room['hole1'].e_to = room['hole2']
room['hole1'].w_to = None
room['hole1'].s_to = room['hole6']

# Hole 2
room['hole2'].e_to = room['hole3']
room['hole2'].w_to = room['hole1']
room['hole2'].n_to = None
room['hole2'].s_to = room['hole5']

# Hole 3
room['hole3'].s_to = room['hole4']
room['hole3'].w_to = room['hole2']
room['hole3'].n_to = None
room['hole3'].e_to = None

# Hole 4
room['hole4'].w_to = room['hole5']
room['hole4'].n_to = room['hole3']
room['hole4'].e_to = None
room['hole4'].s_to = None

# Hole 5
room['hole5'].w_to = room['hole6']
room['hole5'].e_to = room['hole4']
room['hole5'].n_to = room['hole2']
room['hole5'].s_to = None


# Hole 6
room['hole6'].n_to = room['hole1']
room['hole6'].e_to = room['hole5']
room['hole6'].w_to = room['parking_lot']
room['hole6'].s_to = None

# Message Globals
CANNOT_MOVE_MESSAGE = 'It would not be courteous to the course or other players for you to go this way.'

#
# Main
#

# Make a new player object that is currently in the 'outside' (parking_lot) room.
player = Player('Joe Discgolfer', 50, room['parking_lot'])

# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.


# print('test\n',player.room.s_to)
print("""Welcome to pyDiscgolf!\n""")

# check if player is in the parking lot - if so don't display the hole info
if player.room.name != 'Parking Lot':
    print(player.room)
else:
    print(f'Room: {player.room.name}\nWhat do you see?:\n{player.room.description}')

choice = 0
while choice != 'q':
    choice = input('\nWhere would you like to go? (n: north, e: east, s: south, w: west, q: quit): ')
    
    # choice options
    if choice == 'n':
        if player.room.n_to != None:
            print(f'You move to the north!\n')
            player.setroom(player.room.n_to)
        else:
            print(CANNOT_MOVE_MESSAGE)
    elif choice == 's':
        if player.room.s_to != None:
            print(f'You move to the south!\n')
            player.setroom(player.room.s_to)
        else:
            print(CANNOT_MOVE_MESSAGE)
    elif choice == 'e':
        if player.room.e_to != None:
            print(f'You move to the east!\n')
            player.setroom(player.room.e_to)
        else:
            print(CANNOT_MOVE_MESSAGE)
    elif choice == 'w':
        if player.room.w_to != None:
            print(f'You move to the west!\n')
            player.setroom(player.room.w_to)
        else:
            print(CANNOT_MOVE_MESSAGE)  

    else:
        print(f'{choice} is an invalid option')
        

print('Thanks for playing!')

