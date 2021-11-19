from pygame_engine import *
from Grid import Grid
from Level import Level

class Game():
    def __init__(self):
        self.grid = Grid()
        self.level = Level(0)

    def game_loop(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                exit(0)

            if event.type == pg.KEYDOWN:
                if event.key == pg.K_SPACE:
                    self.grid.scale += 2

                if event.key == pg.K_ESCAPE:
                    exit(0)

        self.grid.draw()
        for point in self.level.points:
            self.grid.draw_point(point, 8)
        for function in self.level.functions:
            self.grid.draw_function(function)

game = Game()

while True:

    game.game_loop()

    pg.display.flip()
    clock.tick(60);
