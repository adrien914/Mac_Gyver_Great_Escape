import random


class Labyrinth:
    """
    This class represents the labyrinth,
    create a labyrinth by calling Labyrinth(map_name)
    """
    layout = []
    player_position = []
    guardian_position = []
    picked_up_objects = 0
    window = None
    state = None

    def __init__(self, _map: str) -> None:
        with open("maps/" + _map) as map_file:
            # Get the labyrinth representation from the given file
            for i, line in enumerate(map_file):
                # if the height goes over 15 don't add the following lines
                if i < 15:
                    # Add a line without line breaks as a list to the layout
                    self.layout.append(list(line[:15].replace("\n", "")))
        # Search for the player's position so we can put it in the variable
        self.seek_item("P")
        self.seek_item("E")
        self.place_items()

    def seek_item(self, item: str) -> None:
        """
        This function tries to find a specific item in the actual labyrinth
        """
        for index_y, line in enumerate(self.layout):  # Iterate over the y axis
            for index_x, tile in enumerate(line):  # Iterate over the x axis
                if tile == item:  # If the tile contains a player
                    if item == "P":
                        # Set the player position to this tile
                        self.player_position = [index_y, index_x]
                    else:
                        # Set the guardian position to this tile
                        self.guardian_position = [index_y, index_x]
                    return  # stop the function
        if not self.player_position:
            print("couldn't find player")
            exit()

    def move(self, direction: str) -> None:
        switch = {
            "u": self.move_up,
            "up": self.move_up,
            "r": self.move_right,
            "right": self.move_right,
            "d": self.move_down,
            "down": self.move_down,
            "l": self.move_left,
            "left": self.move_left,
        }
        try:
            switch[direction.lower()]()
        except KeyError:
            print("wrong input")
            pass

    def move_up(self) -> None:
        y, x = self.player_position
        if self.check_collision(y - 1, x):
            self.move_player(y - 1, x)

    def move_down(self) -> None:
        y, x = self.player_position
        if self.check_collision(y + 1, x):
            self.move_player(y + 1, x)

    def move_left(self) -> None:
        y, x = self.player_position
        if self.check_collision(y, x - 1):
            self.move_player(y, x - 1)

    def move_right(self) -> None:
        y, x = self.player_position
        if self.check_collision(y, x + 1):
            self.move_player(y, x + 1)

    def move_player(self, new_y: int, new_x: int) -> None:
        y, x = self.player_position
        self.layout[y][x] = " "
        self.layout[new_y][new_x] = "P"
        self.player_position = [new_y, new_x]
        if self.picked_up_objects == 3:
            self.window.all_active_sprites.remove(self.window.aiguille)
            self.window.all_active_sprites.remove(self.window.ether)
            self.window.all_active_sprites.remove(self.window.tube_plastique)
            self.window.all_active_sprites.add(self.window.seringue)
            self.window.seringue.rect = (len(self.layout[0]) * 30 + 5, 20)
            # y, x = self.guardian_position
            # self.layout[y][x] = " "

    def check_collision(self, y: int, x: int) -> bool:
        """
        This function does all the calculations for what needs to happen
        if the player tries to go to a tile
        :param y: the new line
        :param x: the new column
        :return: a boolean representing if the player can or cannot go to the tile
        """
        try:
            tile = self.layout[y][x]
        # It will throw an IndexError if the
        # next position is out of range of the list
        except IndexError:
            return False
        # if the tile is a wall or the game has already ended return False
        if tile == "x" or self.state == "win" or self.state == "lose":
            return False
        elif tile == "E":  # if the tile is an enemy, exit the game
            if self.picked_up_objects == 3:
                self.window.all_active_sprites.remove(self.window.guardian)
                return True
            self.state = "lose"
        elif tile == "G":  # if the tile is the goal, exit the game
            self.state = "win"
        elif tile == '0' or tile == '1' or tile == '2':
            # Position the item on the right side of
            # the labyrinth in the order of their pick-up
            rect = (
                len(self.layout[0]) * 30 + 5,
                (self.picked_up_objects * 30) + 20
            )
            if tile == '0':
                self.window.aiguille.rect = rect
            elif tile == '1':
                self.window.tube_plastique.rect = rect
            elif tile == '2':
                self.window.ether.rect = rect
            # increment the number of picked up objects
            self.picked_up_objects += 1
        return True

    def get_free_tiles(self) -> list:
        free_tiles = []
        for index_y, line in enumerate(self.layout):  # Iterate over the y axis
            for index_x, tile in enumerate(line):  # Iterate over the x axis
                if tile == " ":  # If the tile is empty
                    free_tiles.append([index_y, index_x])
        return free_tiles

    def place_items(self) -> None:
        free_tiles = self.get_free_tiles()
        for i in range(0, 3):
            random_index = random.randint(0, len(free_tiles))
            x, y = free_tiles.pop(random_index)
            self.layout[x][y] = str(i)
