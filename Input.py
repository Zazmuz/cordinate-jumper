from pygame_engine import *

def multiply(arr):
    res = 1
    for a in arr: res *= a
    return res

class Input():
    def __init__(self):
        self.width = 500
        self.height = 300

        self.input_string = "y = "
        self.function = None

    def draw(self):
        opacity_surface = pg.Surface((WIDTH, HEIGHT))
        opacity_surface.set_alpha(180)
        opacity_surface.fill((255,255,255))
        screen.blit(opacity_surface, (0,0))

        x = (WIDTH - self.width) // 2
        y = (HEIGHT - self.height) // 2

        pg.draw.rect(screen, (255,255,255), (x, HEIGHT - y - self.height, self.width, self.height))


        myfont = pg.font.SysFont('Comic Sans MS', 30)
        textsurface = myfont.render(self.input_string, False, (0, 0, 0))
        screen.blit(textsurface,(x + 50, HEIGHT // 2 - 15))

    def get_function(self, string):
        print(string)
        s = string.replace(" ", "")[2:]
        sep = s.split("+")

        lambdas = []
        for j in sep:
            to_multiply = j.split("*")
            funcs = [lambda x : x] + [None] * len(to_multiply)

            for M in range(len(to_multiply)):
                m = to_multiply[M]
                if m == "x":
                    funcs[M+1] = lambda x : x

                elif all([letter in "1234567890" for letter in m]):
                    funcs[M+1] = lambda x : int(m)

                else:
                    return False

            lambdas.append(lambda x : multiply([f(x) for f in funcs]))


        func = lambda x : sum([l(i) for l in lambdas])


        for i in range(10):
            print(i,func(i))


        print(s)

    def take_input(self, EVENTS):
        for event in EVENTS:
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_BACKSPACE:
                    if len(self.input_string) == 4:
                        continue
                    self.input_string = self.input_string[:-1]
                if event.key == pg.K_RETURN:
                    if self.get_function(self.input_string):
                        return self.function

                else:
                    l = event.unicode
                    if l in "1234567890x+* ":
                        self.input_string += l
