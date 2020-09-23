from utils import sub, dot, length, sum, mul, norm
from intersect import *

'''
  Diana Ximena de León Figueroa
  Carne 18607
  RT2 - Phong model
  Graficas por Computadora
  10 de septiembre de 2020
'''


class Sphere(object):
  def __init__(self, center, radius, material):
    self.center = center
    self.radius = radius
    self.material = material

  def rayIntersect(self, origin, direction):
    L = sub(self.center, origin)
    tca = dot(L, direction)
    l = length(L)
    # distancia al cuadrado
    dc = l ** 2 - tca ** 2

    if dc > self.radius ** 2:
        return None

    thc = (self.radius ** 2 - dc) ** 0.5
    t0 = tca - thc
    t1 = tca + thc

    if t0 < 0:
        t0 = t1
    if t0 < 0:
        return None

    hit = sum(origin, mul(direction, t0))
    normal = norm(sub(hit, self.center))

    return Intersect(
        distance=t0,
        point=hit,
        normal=normal
    )
