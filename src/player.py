# Write a class to hold player information, e.g. what room they are in
# currently.
class Player:
    def __init__(self, name, current_room):
        self.name = name
        self.current_room = current_room
        self.inventory = []
    
    def move_rooms(self, move_direction):
        def none_room():
            print("Can't go that way. Try again...")

        if move_direction == 'n':
            if self.current_room.n_to is not None:
                self.current_room = self.current_room.n_to
            else:
                none_room()
        elif move_direction == 's':
            if self.current_room.s_to is not None:
                self.current_room = self.current_room.s_to
            else:
                none_room()
        elif move_direction == 'e':
            if self.current_room.e_to is not None:
                self.current_room = self.current_room.e_to
            else:
                none_room()
        elif move_direction == 'w':
            if self.current_room.w_to is not None:
                self.current_room = self.current_room.w_to
            else:
                none_room()
        else:
            none_room() 