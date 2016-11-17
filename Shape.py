# from abc import ABCMeta, abstractmethod
import numpy as np


class Shape:

    def __init__(self, **kwargs):
        self.center = kwargs.get("center", np.zeros(3))
        self.scale = kwargs.get("scale", np.ones(3))
        self.rot = kwargs.get("rot", None)
        self.painter = kwargs.get("painter", None)

    def draw(self):
        self.painter.draw()




