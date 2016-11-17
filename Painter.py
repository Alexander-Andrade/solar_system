from OpenGL.GL import * 
from OpenGL.GLU import * 
from OpenGL.GLUT import *

from abc import ABCMeta, abstractmethod


class Painter(metaclass=ABCMeta):

    @abstractmethod
    def draw(self):
        pass


