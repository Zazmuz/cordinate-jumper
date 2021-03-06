from pygame_engine import *
from random import randint


class Grid():
    def __init__(self):

        self.axis_thickness = 4
        self.gridline_thickness = 1

        self.x_offset = self.y_offset = 2 # Integer steps in positive direction offset
        self.scale = 100 # Number of pixels per integer step parallell to axis

    def draw(self):

        gridline_color = (0,0,0)

        screen.fill((255,255,255))
        x_axis_start = self.scale * self.x_offset
        pg.draw.rect(screen, gridline_color, (x_axis_start - self.axis_thickness // 2, 0, self.axis_thickness, HEIGHT))

        y_axis_start = self.scale * self.y_offset
        pg.draw.rect(screen, gridline_color, (0, HEIGHT - (y_axis_start + self.axis_thickness // 2), WIDTH, self.axis_thickness))

        for vertical_gridline_x in range(x_axis_start % self.scale, WIDTH, self.scale):
            pg.draw.rect(screen, gridline_color, (vertical_gridline_x, 0, self.gridline_thickness, HEIGHT))

        for horizontal_gridline_y in range(y_axis_start % self.scale, HEIGHT, self.scale):
            pg.draw.rect(screen, gridline_color, (0, HEIGHT - horizontal_gridline_y, WIDTH, self.gridline_thickness))

    def draw_point(self, point, radius, color):
        x, y = point.x, point.y
        x = self.scale * (self.x_offset + x)
        y = HEIGHT - self.scale * (self.y_offset + y)
        pg.draw.circle(screen, color, (x, y), radius)

    def draw_function(self, function):
        last_Y = None
        for pixel_x in range(WIDTH):
            actual_x = pixel_x / self.scale - self.x_offset
            actual_y = function.function(actual_x)
            pixel_y = (self.y_offset + actual_y) * self.scale

            X = int(pixel_x); Y = HEIGHT - int(pixel_y)
            screen.set_at((X, Y-1), function.color)
            screen.set_at((X, Y), function.color)
            screen.set_at((X, Y+1), function.color)

            if last_Y is not None:
                iterating_range = range(last_Y, Y + 1) if Y >= last_Y else range(Y, last_Y + 1)

                for yp in iterating_range:
                    screen.set_at((X, yp), function.color)
            else:
                screen.set_at((X, Y), function.color)
            last_Y = Y

    def draw_player(self, player):
        x = self.scale * (self.x_offset + player.x)
        y = self.scale * (self.y_offset + player.y)
        pg.draw.circle(screen, (100, 100, randint(155, 200)), (x, HEIGHT - y), 15)
