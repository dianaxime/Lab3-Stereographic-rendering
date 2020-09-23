from color import *

'''
  Diana Ximena de León Figueroa
  Carne 18607
  RT2 - Phong model
  Graficas por Computadora
  10 de septiembre de 2020
'''


class Material(object):
  def __init__(self, diffuse, albedo, spec, refractionIndex = 0):
    self.diffuse = diffuse
    self.albedo = albedo
    self.spec = spec
    self.refractionIndex = refractionIndex


WHITE = Color(250, 245, 250)
GRAY = Color(200, 200, 190)
RED = Color(240, 50, 40)
BROWN = Color(220, 160, 125)
ORANGE = Color(230, 115, 50)
ORANGE2 = Color(175, 85, 45)
MAROON = Color(125, 20, 10)
GREEN = Color(180, 190, 65)
BLACK = Color(40, 40, 40)


eye = Material(diffuse = BLACK, albedo = (0.6, 0.3, 0.1, 0.1), spec = 5, refractionIndex = 0)
oso1 = Material(diffuse = WHITE, albedo = (0.8, 0.8, 0.1, 0.1), spec = 30, refractionIndex = 0)
adorno1 = Material(diffuse = GRAY, albedo = (1, 1, 0.1, 0.1), spec = 30, refractionIndex = 0)
mona1 = Material(diffuse = RED, albedo = (0.6, 0.3, 0.1, 0.1), spec = 15, refractionIndex = 0)
oso2 = Material(diffuse = BROWN, albedo = (0.9, 0.8, 0.1, 0.1), spec = 30, refractionIndex = 0)
tono2 = Material(diffuse = ORANGE, albedo = (0.6, 0.3, 0.1, 0.1), spec = 15, refractionIndex = 0)
tono3 = Material(diffuse = ORANGE2, albedo = (0.6, 0.3, 0.1, 0.1), spec = 15, refractionIndex = 0)
adorno2 = Material(diffuse = MAROON, albedo = (0.9, 0.9, 0.1, 0.1), spec = 30, refractionIndex = 0)
mona2 = Material(diffuse = GREEN, albedo = (0, 10, 0, 0.8), spec = 1425, refractionIndex = 1.5)
