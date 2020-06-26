from utils.Labyrinth import Labyrinth
import pygame
from pygame.locals import KEYUP, KEYDOWN


class Main:

    def __init__(self):
        labyrinth = Labyrinth("sample_map.txt")
        while True:
            player_input = input("Direction ou aller: ")
            labyrinth.move(player_input)

if __name__ == "__main__":
    Main()
