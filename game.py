from pygame_engine import *
from Grid import Grid
from Level import Level
from Function import Function
from Input import Input

class Game():
    def __init__(self):
        self.grid = Grid()
        self.level = Level(0)
        self.input = Input()

    def game_loop(self):
        wait_iteration = False
        global from_input
        EVENTS = pg.event.get()
        for event in EVENTS:
            if event.type == pg.QUIT:
                exit(0)

            if event.type == pg.KEYDOWN:
                if event.key == pg.K_SPACE:
                    self.grid.scale += 2

                if event.key == pg.K_ESCAPE:
                    exit(0)

                if event.key == pg.K_RIGHT:
                    self.level.players[0].add_function(
                        Function(lambda x : x)
                    )

                if event.key == pg.K_LEFT:
                    self.level.players[0].add_function(
                        Function(lambda x : 5)
                    )

                if event.key == pg.K_RETURN and from_input is not None:
                    from_input = None
                    wait_iteration = True

        if wait_iteration: return
        self.grid.draw()
        for player in self.level.players:
            for point in player.points:
                self.grid.draw_point(point, 8)
            for function in player.functions:
                self.grid.draw_function(function)
            self.grid.draw_player(player)

        if from_input == None:
            self.input.draw()
            self.input.take_input(EVENTS)
            from_input = self.input.function
            if from_input != None:
                player.add_function(self.input.function)
                self.input = Input()
                from_input = 0
                print("here")


from_input = None

game = Game()

while True:

    game.game_loop()

    pg.display.flip()
    clock.tick(60);
