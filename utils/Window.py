import pygame
from utils.Player import Player
from utils.Spritesheet import Spritesheet
from utils.NonPlayerSprites import NonPlayerSprites


class Window:
    screen = None
    all_active_sprites = None

    def __init__(self, labyrinth):
        self.labyrinth = labyrinth
        pygame.init()
        size = 500, 500
        self.FPSCLOCK = pygame.time.Clock()
        self.screen = pygame.display.set_mode(size)
        self.all_active_sprites = pygame.sprite.Group()
        self.player = Player()
        self.guardian = NonPlayerSprites('Gardien.png', (0, 0))
        self.aiguille = NonPlayerSprites('aiguille.png', (0, 0))
        self.tube_plastique = NonPlayerSprites('tube_plastique.png', (0, 0))
        self.ether = NonPlayerSprites('ether.png', (0, 0))
        self.seringue = NonPlayerSprites('seringue.png', (0, 0))
        self.all_active_sprites.add(self.player,
                                    self.guardian,
                                    self.aiguille,
                                    self.tube_plastique,
                                    self.ether
                                    )
        # Load the terrain tiles
        self.tiles = Spritesheet('ressource/floor-tiles-20x20.png')
        self.floor = self.tiles.image_at((0, 0, 20, 20))
        self.lava = self.tiles.image_at((0, 20*12, 20, 20))
        self.wall = self.tiles.image_at((0, 20*12, 20, 20))

    def refresh(self):
        self.all_active_sprites.update()
        self.screen.fill((0, 0, 0))
        for index_y, line in enumerate(self.labyrinth.layout):
            for index_x, column in enumerate(line):
                if column.lower() == 'x':
                    self.screen.blit(self.lava, (index_x * 30, index_y * 30))
                elif column == ' ':
                    self.screen.blit(self.floor, (index_x * 30, index_y * 30))
                elif column.lower() == "p":
                    self.player.rect.left = index_x * 30
                    self.player.rect.top = index_y * 30
                elif column.lower() == "e":
                    self.guardian.rect.left = index_x * 30
                    self.guardian.rect.top = index_y * 30
                elif column.lower() == "0":
                    self.aiguille.rect.left = index_x * 30
                    self.aiguille.rect.top = index_y * 30
                elif column.lower() == "1":
                    self.tube_plastique.rect.left = index_x * 30
                    self.tube_plastique.rect.top = index_y * 30
                elif column.lower() == "2":
                    self.ether.rect.left = index_x * 30
                    self.ether.rect.top = index_y * 30
        self.all_active_sprites.draw(self.screen)
        pygame.display.update()
        self.FPSCLOCK.tick(30)
