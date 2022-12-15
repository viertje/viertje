from line_class import line
import math

class triangle(line):
    def __init__(self, xs, ys, xe, ye, xf, yf):
        super().__init__(xs, ys, xe, ye, xf, yf)

    def calc_area(self):
        return 0.25 * math.sqrt(\
            (self.line_lenght()+self.line_lenght_2()+self.line_lenght_3())*\
            (-self.line_lenght()+self.line_lenght_2()+self.line_lenght_3())*\
            (self.line_lenght()-self.line_lenght_2()+self.line_lenght_3())*\
            (self.line_lenght()+self.line_lenght_2()-self.line_lenght_3()))

    def calc_circumference(self):
        return self.line_lenght() + self.line_lenght_2() + self.line_lenght_3()