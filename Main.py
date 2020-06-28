from utils.Labyrinth import Labyrinth
from utils.Window import Window
import pygame
from pygame import QUIT
import sys

class Main:

    def __init__(self):
        labyrinth = Labyrinth("sample_map.txt")
        window = Window(labyrinth)
        labyrinth.window = window
        BLACK = (0, 0, 0)
        while True:  # main game loop
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_LEFT:
                        window.player.move_left()
                        labyrinth.move('l')
                    if event.key == pygame.K_RIGHT:
                        window.player.move_right()
                        labyrinth.move('r')
                    if event.key == pygame.K_DOWN:
                        window.player.move_down()
                        labyrinth.move('d')
                    if event.key == pygame.K_UP:
                        window.player.move_up()
                        labyrinth.move('u')
            window.refresh()

        #player_input = input("Direction ou aller: ")
        #labyrinth.move(player_input)

if __name__ == "__main__":
    Main()
