# Angela Karina Vegega Ortiz


# Define function to print a welcome message and instructions
def display_opening_message(text_divider):
    """This function sets a welcome message and instructions for the player and prints them with a text divider
    at the end
    """
    # Set messages
    welcome_message = 'A Visit from El Chupacabras!'
    game_info = ('El chupacabras has come to suck the blood of your livestock! Move throughout your house and collect'
                 ' 6 items before coming face to face with the beast!')
    moving_instructions = 'To move to a different room type go South, go North, go East, or go West'
    item_instructions = 'To add an item to your inventory, type get "item name"'
    # Print messages and divider on separate lines
    print(welcome_message, game_info, moving_instructions, item_instructions, text_divider, sep='\n')


# Define function to show player status
def show_player_status(present_room, player_inventory, rooms):
    """This function prints the player's status in the game, what room they are in, if there is an item in that room it
    displays what that item is and what they can use it for, or it displays that there are no items. It also shows the
    contents of the player's inventory."""
    # Set message for the current room
    current_room_status = 'You are in the {}.'.format(present_room)

    # Determine output based on the existence of an item in the current room
    if 'item' not in rooms[present_room]:
        current_room_item_status = 'There are no items to pick up here.'
        print(current_room_status, current_room_item_status)
    else:
        current_room_item = rooms[present_room]['item']
        item_use = rooms[present_room]['item use']
        current_room_item_status = 'You see a {}. You can use it to {}.'.format(current_room_item, item_use)
        print(current_room_status, current_room_item_status)
    # Print player inventory
    print('Inventory:', player_inventory)


# Define function to move player between rooms
def move_between_rooms(present_room, cardinal_direction, rooms):
    """This function takes the room the player is currently in and their input of a cardinal direction to move to next.
    It checks if there is a room in that direction. If there is one, it returns the room the player has moved into"""
    # If the direction is one of the keys in the value of the current room's dictionary within the dictionary called
    # room, update the present_room variable to the value associated with that cardinal key, moving to that room
    if cardinal_direction in rooms[present_room]:
        present_room = rooms[present_room][cardinal_direction]
    # Else if the direction entered does not match the directions in the room's keys, print a message, return the
    # unchanged room, main gameplay loop continues and restarts, player will be asked for input again
    else:
        print('There isn\'t a room in that direction.')
    # Return the present_room variable which will update the current_room variable in the gameplay loop
    return present_room


# Define function to get an item
def get_item(item_to_get, present_room, player_inventory, rooms):
    """This function checks if the room the player is in has an item. If it does, it checks if the item the player
    wants is in that room, adds it to the players inventory and deletes it from the dictionary. If it's not, it prints
    a message to the player. It also prints a message if the player tries to pick up an item in a room that has no
    items."""
    # Check if the room the player is in has an item
    if 'item' in rooms[present_room]:
        # If the item the player wants is in the room add it to the inventory list and delete it from the dictionary,
        # then print a message to the player
        if item_to_get == rooms[present_room]['item']:
            player_inventory.append(item_to_get)
            del rooms[present_room]['item']
            print('You picked up a {}.'.format(item_to_get))
        # Else the player has a typo or tried to pick up an item not in the room, print a message to let them know
        else:
            print('Can\'t get {}.'.format(item_to_get))
    # Else inform the player that there are no items
    else:
        print('There are no items to pick up in this room.')


# Define main function
def main():
    # A dictionary for the A Visit From El Chupacabras text game
    # The dictionary links a room to other rooms and contains the item that is in each room and information about the
    # item.
    rooms = {
        'Bedroom': {'North': 'Living Room', 'East': 'Kids\' Room'},  # Starting room
        'Living Room': {'North': 'Storage Room', 'East': 'Kitchen', 'South': 'Bedroom', 'West': 'Bathroom',
                        'item': 'Pro Camera', 'item use': 'document clear proof of the existence of el Chupacabras'},
        'Kids\' Room': {'West': 'Bedroom', 'item': 'Goat Plushie', 'item use': 'distract el Chupacabras'},
        'Storage Room': {'East': 'Backyard', 'South': 'Living Room', 'item': 'Machete',
                         'item use': 'kill el Chupacabras if you have to'},
        'Kitchen': {'North': 'Garage', 'West': 'Living Room', 'item': 'Frying Pan',
                    'item use': 'knock out el Chupacabras'},
        'Bathroom': {'East': 'Living Room', 'item': 'Shampoo Bottle', 'item use': 'blind el Chupacabras'},
        'Garage': {'South': 'Kitchen', 'item': 'Rope', 'item use': 'tie up el Chupacabras'},
        'Backyard': {'West': 'Storage Room'}  # Villain room
    }

    # Start player in the Bedroom
    current_room = 'Bedroom'

    # Initialize empty list for player inventory
    player_inventory = []

    # Set text divider variable to be used anywhere text needs to be separated
    text_divider = '-' * 30

    # Set validation message for invalid inputs
    validation_message = 'Please enter a valid move.'

    # Set the exit message for the end of the game
    exit_message = 'Thanks for playing, hope you had fun!'

    # Call function to print welcome message and instructions
    display_opening_message(text_divider)

    # Enter while loop for main gameplay which will continue until the player enters the backyard
    while True:
        # Call the function to print the player's status
        show_player_status(current_room, player_inventory, rooms)

        # If the player has reached the backyard, and they have all 6 items in their inventory, print the winning
        # message and break the gameplay loop
        if current_room == 'Backyard' and len(player_inventory) == 6:
            winning_message = ('You see el Chupacabras!\nYou toss the goat plushie by its feet. While it\'s '
                               'investigating it, you squirt shampoo into its eyes, knock it out with your frying pan, '
                               'tie it up with your rope, \nand take pictures of it once it\'s subdued.\n'
                               'You call Animal Control and become famous for capturing the first live specimen of '
                               'el Chupacabras. Your goats and chicken are happy.\nCongratulations!')
            print(winning_message)
            break
        # Else if the player doesn't have all 6 items upon reaching the backyard, print the losing message and break the
        # gameplay loop
        elif current_room == 'Backyard' and len(player_inventory) < 6:
            losing_message = ('You see el Chupacabras!\nYou try to fight it, but don\'t have enough items to deal with '
                              'it. You manage to keep it away from your livestock, but it\'s not leaving hungry.\nYou '
                              'become the first human victim of el Chupacabras.\nGame over.')
            print(losing_message)
            break

        # Get player input for their next move, strip whitespace, and split by space
        player_move = input('Enter your move:\n').strip().split()
        # Get the first word of the player's input and make it lowercase
        player_move_first_word = player_move[0].lower()

        # If player input first word is 'go', player_move gets the second word which should be the
        # cardinal direction, to check next
        if player_move_first_word == 'go':
            player_move = player_move[1].capitalize()
            # Check if the player entered a valid cardinal direction, jump to the beginning of the loop if not
            if player_move != 'South' and player_move != 'North' and player_move != 'East' and player_move != 'West':
                print(validation_message, text_divider, sep='\n')
                continue
            # Call the move_between_rooms function that will move the player to a different room and returns the room
            # the player has moved into, use that to update the current room variable
            current_room = move_between_rooms(current_room, player_move, rooms)
        # ELse if the first word is 'get', call the get_item function
        elif player_move_first_word == 'get':
            player_move = ' '.join(player_move[1:]).title()
            # Print a message if the player made a mistake and typed 'get' instead of 'go' for moving rooms
            if player_move == 'South' or player_move == 'North' or player_move == 'East' or player_move == 'West':
                print(validation_message, text_divider, sep='\n')
                continue
            # Call the get_item function that will update the player's inventory
            get_item(player_move, current_room, player_inventory, rooms)
        # The first word is neither 'go' nor 'get', so print the validation message
        else:
            print(validation_message)

        # Print text divider for clarity before starting the loop again
        print(text_divider)

    # Print the exit message after exiting the while loop
    print(exit_message)


# Call the main function
if __name__ == '__main__':
    main()
