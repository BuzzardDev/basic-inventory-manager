class Rooms:
    rooms = {
        1: [],
        2: [],
        3: []
    }

    @classmethod
    def new(cls, name):
        cls.rooms[name] = []
        print(f"Successfully created room {name}")

    @classmethod
    def remove(cls, name):
        confirm = input(f"Are you sure you would like to remove room {name},you will lose all items inside. (type y or n) ").lower()
        if confirm == 'y':
            removedRoom = cls.rooms.pop(name)
            print(f"Successfully removed room {removedRoom}")

    @classmethod
    def update_name(cls, name, new_name):
        if name in cls.rooms and new_name not in cls.rooms:
            cls.rooms[new_name] = cls.rooms.pop(name)
            print(f"Successfully renamed {name} to {new_name}")
        else: print("Error Changing Name, new name either already exists or name is not a room")

    @classmethod
    def remove_item(cls, room, item):
        if room in cls.rooms:
            room_items = cls.rooms[room]
            if item in room_items:
                item_index = room_items.index(item)
                removedItemFromRoom = room_items.pop(item_index)
                print(f"Successfully removed {removedItemFromRoom} from room {room}")
            else: print(f"Item {item} not found in room {room}")
        else: print(f"Room {room} not found")

