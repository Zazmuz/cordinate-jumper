class Function():
    def __init__(self, func):
        self.function = func
        self.color = (50, 50, 155)


class LinearFunction(Function):
    def __init__(self, k, m): # y = kx + m
        self.color = (50, 50, 155)
        self.k = k
        self.m = m

    def function(self, x):
        return x * self.k + self.m
