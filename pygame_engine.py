import pygame as pg
import os
import ctypes
from ctypes import windll


# os.environ['SDL_VIDEO_CENTERED'] = '1' # You have to call this before pygame.init()

pg.init()


# Found this approach on stackover
# Probably only windows compatible
ctypes.windll.user32.SetProcessDPIAware()
true_res = (windll.user32.GetSystemMetrics(0),windll.user32.GetSystemMetrics(1))
WIDTH, HEIGHT = true_res


# pygame.display.set_mode(true_res,pygame.Fullscreen)
#
# info = pg.display.Info() # You have to call this before pygame.display.set_mode()
#
# WIDTH, HEIGHT = info.current_w,info.current_h
# WIDTH, HEGIHT = 1200, 800
# print(WIDTH, HEIGHT)
#
# size = pg.display.list_modes()[0]
# WIDTH, HEIGHT = size

screen = pg.display.set_mode((WIDTH, HEIGHT), pg.FULLSCREEN)

clock = pg.time.Clock()
