from Point import Point
from Function import Function, LinearFunction

class Level():
    def __init__(self, id):
        self.id = id
        self.points = self.load_points()
        self.functions = [Function(lambda x : 8 - (x - 5)**2/4)]

    def load_points(self):
        p = [
            [Point(x, y) for x, y in [(5,5),(10,5)]]
        ]
        return p[self.id]
