from pygame_engine import *
from Point import Point

class Player():
    def __init__(self, max_functions, points):
        self.x = self.y = 0
        self.max_functions = max_functions
        self.functions = []
        self.points = [Point(0,0)] + points
        self.number_of_points = len(self.points)
        self.can_reach = [True] + [False]*(len(self.points)-1)

    def update_function_reach(self, function):
        passes_through = [False]*self.number_of_points

        for i in range(self.number_of_points):
            x, y = self.points[i].x, self.points[i].y
            if function.function(x) == y:
                passes_through[i] = True

        if any([self.can_reach[i] and passes_through[i] for i in range(self.number_of_points)]):
            for i in range(self.number_of_points):
                if passes_through[i]: self.can_reach[i] = True
        print(*self.can_reach)

    def add_function(self, function):
        self.update_function_reach(function)
        for f in self.functions:
            self.update_function_reach(f)

        self.functions.append(function)
