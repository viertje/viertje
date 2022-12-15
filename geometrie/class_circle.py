from line_class import line
import math

class circleclass(line):
    def __init__(self, xs, ys, xe, ye, xf, yf):
        super().__init__(xs, ys, xe, ye, xf, yf)

    def calc_area(self):
        return(self.line_lenght()** 2) * math.pi

    def calc_circumference(self):
        return(self.line_lenght()* 2) * math.pi