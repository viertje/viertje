from line_class import line

class rectangle(line):
    def __init__(self, xs, ys, xe, ye, xf, yf):
        super().__init__(xs, ys, xe, ye, xf, yf)


    def calc_a(self):
        return (self.p2.x - self.p1.x)

    def calc_b(self):
        return (self.p2.y - self.p1.y)

    def calc_area(self):
        return (self.calc_a() * self.calc_b())

    def calc_circumference(self):
        return (self.calc_a() + self.calc_b())*2
