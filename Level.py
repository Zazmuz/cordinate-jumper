from Point import Point
from Function import Function, LinearFunction
from Player import Player

class Level():
    def __init__(self, id):
        self.id = id
        self.functions = [Function(lambda x : 8 - (x - 5)**2/4),
                            Function(lambda x : (1/3) * (x-5)**3 + 0.2*x)]
        self.players = self.load_players()

    def load_points(self):
        p = [
            [Point(x, y) for x, y in [(5,5),(10,5)]]
        ]
        return p[self.id]

    def load_players(self):
        return [Player(5, self.load_points())]
