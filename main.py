print('Zachery Danny Lundberg IT 140 Text Based Game: The Time Loop\n')

# House Layout
rooms = {
    'coat room': {'name': 'coat room', 'north': 'living room', 'item': 'nothing'},  # Starting Room
    'living room': {'name': 'living room', 'north': 'den', 'south': 'coat room',
                    'west': 'bedroom', 'east': 'reception room',
                    'item': 'nothing'},  # Main Room
    'den': {'name': 'den', 'item': 'Politician'},  # Villain Room
    'bedroom': {'name': 'bedroom', 'east': 'living room', 'north': 'closet',
                'south': 'restroom', 'item': 'hourglass'},  # Hourglass
    'closet': {'name': 'closet', 'south': 'bedroom', 'item': 'watch'},  # Pocket Watch
    'restroom': {'name': 'restroom', 'north': 'bedroom', 'item': 'rag'},  # Polishing Rag
    'reception room': {'name': 'reception room', 'west': 'living room',
                       'south': 'kitchen', 'item': 'codex'},  # Codex
    'kitchen': {'name': 'kitchen', 'north': 'reception room', 'south': 'dining room',
                'item': 'amulet'},  # Amulet of Lifting
    'dining room': {'name': 'dining room', 'north': 'kitchen',
                    'item': 'clock'}  # Big Ben Hour Hand
}
# global vars for file
compass = ('north', 'south', 'east', 'west')
playerInv = []
location = rooms['coat room']
roomItem = location['item']


# Classes for Game

def instructions():  # how to play game, and why.
    playerInstructions = \
        ["The Time Loop",
         "Collect the 6 items to break the time loop, or risk the Politician stopping you.",
         "Move commands: go south, go north, go east, go west",
         "To add inventory: grab 'item name'.",
         "-------------"]
    print('\n'.join(playerInstructions))


def roomInventory():  # what's in the room?
    if roomItem != 'nothing':
        print(f"This room has the {roomItem} in it.")
    else:
        print(f'There is {roomItem} in this room')


def playerPocket():  # player inventory print command
    if len(playerInv) == 0:
        print('Inventory is empty.')
    else:
        print('inventory:', ', '.join(playerInv))


def show_status():  # player status, location, inventory, etc
    print('-------------')
    print(f"You are in the {location['name']}.")
    roomInventory()
    playerPocket()
    print('-------------\n')
    if location == rooms['den']:
        if len(playerInv) != 6:
            print('You lost the game! The politician adjusted the time loop.')
            exit()
        else:
            print('You beat the politician! You fixed the time loop.')
            exit()


instructions()  # prints instructions for player

if __name__ == '__main__':  # main function

    command = ''  # player input for iterations
    while location != 'den':  # gameplay loop definition

        show_status()  # main gameplay loop
        command = (input('What would you like to do? ')).lower().split(' ')
        if command[0] == 'go' or 'grab' or 'exit':  # player control loop
            if command[0] == 'exit':
                print('Thanks for playing!')
                exit()
            elif command[0] == 'go':  # player movement
                if command[1] not in location:
                    print('Invalid direction.\n')
                else:
                    location = rooms[location[command[1]]]
                    roomItem = location['item']
            elif command[0] == 'grab':  # player update inventory
                if command[1] == 'nothing':
                    print("You can't grab that.\n")
                else:
                    if command[1] not in roomItem:
                        print('Invalid command.\n')
                    else:  # dictionary update
                        playerInv.append(roomItem)
                        del location['item']
                        location.update({"item": 'nothing'})
                        roomItem = location['item']
            else:
                print('Item not in room.')  # invalid command for item print
        else:
            print("Invalid command. Please try again.")  # overall invalid command
