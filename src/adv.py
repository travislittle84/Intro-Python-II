from room import Room
from player import Player
import sys

# Declare all the rooms

room = {
    'parking_lot': Room("Parking Lot", 
                        """You're in the parking lot of your home course. The skies are clear and deep blue, 
winds are calm, about 70f. Perfect day for disc golf!

There are not many trees at this course, but there are some fairly long holes and tricky out of bounds.
The course is on a city open area park which is basically an unused field, if you end up off the fairway,
you will be contending with prickly bushes and high grass.

To the south of you is the entrance to the course.""", 0),

    'hole1':  Room("Hole 1",
                     """Wide open shot with a guardian tree in front of the basket.
An out of bounds path runs along the right side of the fairway.

To the east is hole 2""", 354),

    'hole2':    Room("Hole 2", 
                        """Another wide open shot, slightly down hill. Guardian tree
in front of and slightly left. There is not much of a fairway, the terrain is rough 
until you reach circle 2. There is an OB path in front of the teepad but it's close 
enough to not worry about (hopefully).

There is a path to the east to Hole 3""", 285),

    'hole3': Room("Hole 3",
                    """Looks are deceiving on this one. Easily the hardest hole 
on this course. Wide open, no trees. Elevation rise of a few feet, about 20ft in front of 
the teepad. OB creek long, extending the entire backside of the hole, all the way to cirlce 1. An OB and beyond 
path to the right of the entire hole. The path starts very far from the fairway, 
but it creeps up to the cirlce. Your approach shot and putt could be very dangerous.

The path to Hole 4 is to the south""", 100),

    'hole4':   Room("Hole 4", """Hole 4 Description.

Next hole is to the west""", 100),

    'hole5': Room("Hole 5", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south.

Hole 5 is off to the west""", 100),

    'hole6': Room("Hole 6", """Hole 6 Description
    
The parking lot is is just to the west""", 100)
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
COURSE_ACTION_PROMPT = """What would you like to do?
[ n: north, e: east, s: south, w: west, p: play hole, q: quit game ]: """
HOLE_ACTION_PROMPT = """What disc do you want to throw?
[ p: putter, d: driver, mid: midrange || stop: stop hole - back to course navigation, q: quit game ]: """
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
if player.current_room.name != 'Parking Lot':
    print(player.current_room)
else:
    print(f'Room: {player.current_room.name}\nWhat do you see?:\n{player.current_room.description}')

choice = 0
playing_hole = False

while choice != 'q':

    ## HOLE LOOP
    while playing_hole == True:
        current_feet_to_pin = player.current_room.feet

        while current_feet_to_pin != 0:
            choice = input(HOLE_ACTION_PROMPT)
            if choice == 'stop':
                print('\n - You decide to stop playing this hole.')
                playing_hole = False
                break
            elif choice == 'p':
                print('\n - You bust out your putter and throw it 150ft! Wow it went in too!')
                current_feet_to_pin = 0
                playing_hole = False
            elif choice == 'd':
                print('\n - You bust out the driver and throw it 350ft! AND IT WENT IN')
                current_feet_to_pin = 0
                playing_hole = False
            elif choice == 'm':
                print('\n - You bust out the mid range and throw it 250ft! Into the basket!')
                current_feet_to_pin = 0
                playing_hole = False
            elif choice == 'l':
                print('\n - You take a look around')
                player.look()
                

            
            elif choice == 'q':
                check_quit = input('Are you sure you want to quit the pyDiscgolf before finishing your round? [ y=yes n=no ]: ' )
                if check_quit == 'y':
                    sys.exit() # try this - does it actually exit the program?
                elif check_quit == 'n':
                    choice = input(HOLE_ACTION_PROMPT)

    ## COURSE LOOP
    choice = input(COURSE_ACTION_PROMPT)
    # choice options
    if choice == 'n':
        if player.current_room.n_to != None:
            print(f'You move to the north!\n')
            player.setroom(player.current_room.n_to)
        else:
            print(CANNOT_MOVE_MESSAGE)
    elif choice == 's':
        if player.current_room.s_to != None:
            print(f'You move to the south!\n')
            player.setroom(player.current_room.s_to)
        else:
            print(CANNOT_MOVE_MESSAGE)
    elif choice == 'e':
        if player.current_room.e_to != None:
            print(f'You move to the east!\n')
            player.setroom(player.current_room.e_to)
        else:
            print(CANNOT_MOVE_MESSAGE)
    elif choice == 'w':
        if player.current_room.w_to != None:
            print(f'You move to the west!\n')
            player.setroom(player.current_room.w_to)
        else:
            print(CANNOT_MOVE_MESSAGE)
    elif choice == 'p':
        print('Lets throw a disc!')
        playing_hole = True
    else:
        if choice != 'q':
            print(f'{choice} is an invalid option')
        

print('Thanks for playing!')

