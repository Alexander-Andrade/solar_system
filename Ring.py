from Shape import Shape
from RingPainter import RingPainter
from Rotation import Rotation
import numpy as np


class Ring(Shape):

    def __init__(self, center, inner_radius, outer_radius, img_name, rot=None):
        Shape.__init__(self, center=center, rot=rot, painter=RingPainter(self, img_name))
        self.inner_radius = inner_radius
        self.outer_radius = outer_radius
