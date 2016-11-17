from Shape import Shape
import pyassimp as assimp
from OpenGL.GL import *
import numpy as np
import copy

def gl_face_mode(face):
    n_indices = len(face)
    if n_indices == 1:
        return GL_POINTS
    elif n_indices == 2:
        return GL_LINES
    elif n_indices == 3:
        return GL_TRIANGLES
    elif n_indices == 4:
        return GL_POLYGON

from ModelPainter import ModelPainter


class ModelPrototype(Shape):

    def __init__(self, model_name, center=np.zeros(3), scale=np.ones(3), rot=None):
        self.model_name = model_name
        self.scene = assimp.load(model_name)
        Shape.__init__(self, center=center, scale=scale, rot=rot)
        self.painter = ModelPainter(self)

    def clone(self, center, scale=None, rot=None):
        clone = copy.copy(self)
        clone.center = center
        clone.scale = scale
        clone.scene = None
        if rot:
            clone.rot = rot
        clone.painter = self.painter.clone(clone)
        return clone

    def __del__(self):
        if self.scene:
            assimp.release(self.scene)


