'''
    Diana Ximena de León Figueroa
    Carne 18607
    RT2 - Phong model
    Graficas por Computadora
    10 de septiembre de 2020
'''

class Color(object):
    def __init__(self, r,g,b):
        self.r = r
        self.g = g 
        self.b = b

    def __add__(self, otherColor):
        r = self.r + otherColor.r
        g = self.g + otherColor.g
        b = self.b + otherColor.b

        return Color(r, g, b)


    def __mul__(self, otherColor):
        r = self.r * otherColor
        g = self.g * otherColor
        b = self.b * otherColor

        return Color(r, g, b)

    def __repr__(self):
        return "color (%s, %s, %s)" % (self.r, self.g, self.b)

    def toBytes(self):
        self.r = int(max(min(self.r, 255), 0))
        self.g = int(max(min(self.g, 255), 0))
        self.b = int(max(min(self.b, 255), 0))
        return bytes([self.b, self.g, self.r])
    
    __rmul__ = __mul__