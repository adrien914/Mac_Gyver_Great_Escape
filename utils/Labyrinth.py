class Labyrinth:
    layout = []
    player_position = []

    def __init__(self, map):
        with open("maps/" + map) as map_file:
            for i, line in enumerate(map_file):
                self.layout.append(list(line.replace("\n", "")))
        self.seek_player()
        print(self.player_position)

    def seek_player(self):
        pos_x = 0
        pos_y = 0
        for line in self.layout:
            for tile in line:
                if tile == "P":
                    self.player_position = [pos_x, pos_y]
                    return
                else:
                    pos_x += 1
            pos_x = 0
            pos_y += 1

    def move(self, direction):
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
        switch[direction.lower()]()
        for line in self.layout:
            print(line)

    def move_up(self):
        x, y = self.player_position
        if self.layout[x][y - 1] != "x":
            self.layout[x][y] = " "
            self.layout[x][y - 1] = "P"
            self.player_position = [x, y - 1]

    def move_right(self):
        x, y = self.player_position
        if self.layout[x + 1][y] != "x":
            self.layout[x][y] = " "
            self.layout[x + 1][y] = "P"
            self.player_position = [x + 1, y]

    def move_down(self):
        x, y = self.player_position
        if self.layout[x][y + 1] != "x":
            self.layout[x][y] = " "
            self.layout[x][y + 1] = "P"
            self.player_position = [x, y + 1]

    def move_left(self):
        x, y = self.player_position
        if self.layout[x - 1][y] != "x":
            self.layout[x][y] = " "
            self.layout[x - 1][y] = "P"
            self.player_position = [x - 1, y]