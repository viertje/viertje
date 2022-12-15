import math
from point import point
from abc import ABC, abstractmethod

class line(ABC):
    def __init__(self, xs, ys, xe, ye, xf, yf):
        self.p1 = point(xs, ys)
        self.p2 = point(xe, ye)
        self.p3 = point(xf, yf)
        
    def line_lenght(self):
        return math.sqrt((self.p2.y-self.p1.y)**2+(self.p2.x-self.p1.x)**2)

    def line_lenght_2(self):
        return math.sqrt((self.p3.y-self.p1.y)**2+(self.p3.x-self.p1.x)**2)

    def line_lenght_3(self):
        return math.sqrt((self.p3.y-self.p2.y)**2+(self.p3.x-self.p2.x)**2)

    @abstractmethod
    def calc_circumference():
        pass

    @abstractmethod
    def calc_area():
        pass