from Rooms import Rooms
class Item:
    property = {}

    def __init__(self, name, id, room=None):
        self.name = name
        self.id = id
        self.room = room
        if self.name not in Item.property:
            Item.property[self.name] = self.id
    @classmethod
    def remove(cls, name):
        confirm = input(f"Are you sure you would like to remove item {name},you will lose it forever. (type y or n) ").lower()
        if confirm == 'y':
            if name in Item.property:
                removedItem = cls.property.pop(name)
                print(f"Successfully removed {removedItem}")
            else: print("Not found")

    @classmethod
    def update_name(cls, name, new_name):
        if name in cls.property and new_name not in cls.property:
            cls.property[new_name] = cls.property.pop(name)
            print(f"Successfully changed '{name}' to '{new_name}'")
        else: print("Error Changing Name, new name either already exists or name is not the current inventory")

    @classmethod
    def update_id(cls, name, new_id):
        if name in cls.property and new_id != cls.property[name]:
            oldId = cls.property[name]
            cls.property[name] = new_id
            print(f"Successfully changed '{oldId}' to '{new_id}'")
        else: print("Error changing id, either name not found or id already present")

    @classmethod
    def move_to_room(cls, id, room):
        global rooms
        for key, value in cls.property.items():
            if value == id:
                Rooms().rooms[room].append(id)
                print(f"Successfully moved {key}, id: {value} to room {room}")
                break
        else: print("ID or room not found")

