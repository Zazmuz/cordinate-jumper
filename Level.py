from Point import Point

class Level():
    def __init__(self, id):
        self.id = id
        self.points = self.load_points()

    def load_points(self):
        p = [
            [Point(x, y) for x, y in [(1,2),(0,3)]]
        ]
        return p[self.id]
