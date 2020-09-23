'''
    Diana Ximena de León Figueroa
    Carne 18607
    RT2 - Phong model
    Graficas por Computadora
    10 de septiembre de 2020
'''

from utils import V3

class Light(object):
    def __init__(self, position, intensity):
        self.position = position
        self.intensity = intensity
