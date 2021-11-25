from pygame_engine import *

class Player():
    def __init__(self, max_functions, points):
        self.x = self.y = 0
        self.max_functions = max_functions
        self.functions = []
        self.points = points
        self.number_of_points = len(self.points)
        self.can_reach = [False]*len(self.points)

    def update_function_reach(self, function):
        passes_through = [False]*self.number_of_points

        for i in range(self.number_of_points):
            x, y = self.points[i].x, self.points[i].y
            if function.function(x) == y:
                passes_through[i] = True

        if any([self.can_reach[i] and passes_through[i] for i in range(self.number_of_points)]):
            for i in range(self.number_of_points):
                if passes_through[i]: self.can_reach[i] = True

    def add_function(self, function):
        self.update_function_reach(function)
        for f in self.functions:
            self.update_function_reach(f)

        self.functions.append(function)
