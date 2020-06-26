class Labyrinth:
    layout = None

    def __init__(self, map):
        with open("maps/" + map) as map_file:
            self.layout = map_file.read()
        print(self.layout)