from Item import Item
from Rooms import Rooms

options = [    'new room (1)',    'remove room (2)',    'update room name (3)',    'remove item from room (4)',    'remove item from property (5)',    'update item name (6)',    'update item id (7)',    'move item to room (8)']

if __name__ == "__main__":
    for option in options:
        print(option)

    option = input("Enter Command: ")
    if option.isnumeric():
        option = int(option)
    else:
        print("Invalid input")
        exit()

    if option == 1:
        newRoomName = input("Name of new room? ")
        Rooms.new(newRoomName)

    elif option == 2:
        removeRoomName = input("Name of room to remove? ")
        Rooms.remove(removeRoomName)

    elif option == 3:
        currentRoomName = input("What is the name of the room to rename? ")
        renamedRoomName = input("Name of renamed room? ")
        Rooms.update_name(currentRoomName,renamedRoomName)

    elif option == 4:
        roomOfItem = input("Room of item to remove? ")
        IdOfItemToRemove = input("ID of item to remove? ")
        Rooms.remove_item(roomOfItem, IdOfItemToRemove)

    elif option == 5:
        removeItem = input("Name of item to remove from property")
        Item.remove(removeItem)

    elif option == 6:
        itemNameToRename = input("Name of item to rename")
        newItemName = input("Name of item to update")
        Item.update_name(itemNameToRename, newItemName)

    elif option == 7:
        itemNameToUpdate = input("Name of item to update ID?")
        newItemId = input("New ID of item?")
        Item.update_id(itemNameToUpdate, newItemId)

    elif option == 8:
        itemId = input("ID of item to move?")
        room = input("Room to move item to?")
        Item.move_to_room(itemId, room)

    else:
        print("Invalid input")
