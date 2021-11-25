class Function():
    def __init__(self, func):
        self.function = func
        self.color = (50, 50, 155)


class LinearFunction(Function):
    def __init__(self, k, m):  # y = kx + m
        self.color = (50, 50, 155)
        self.k = k
        self.m = m

    def function(self, x):
        return x * self.k + self.m


class PolynomialFuntion(Function):
    def __init__(self, max_degree):
        self.max_degree = max_degree
        self.coefficient = [0] * max_degree
        self.color = (50, 50, 155)

    def function(self, x):
        ans = self.coefficient[0]
        X = x
        for i in range(1, self.max_degree):
            ans += self.coefficient[i] * X
            X *= x
        return ans