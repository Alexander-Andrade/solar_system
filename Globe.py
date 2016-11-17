from Shape import Shape
from Rotation import Rotation
import numpy as np


class Globe(Shape):

    def __init__(self, center, radius, rot=None, painter=None):
        Shape.__init__(self, center=center, rot=rot, painter=painter)
        self.radius = radius





