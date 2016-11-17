from Painter import *
import numpy as np
from enum import Enum, unique
import math
import random


class Rotation:
    @unique
    class Direction(Enum):
        Left = 1
        Right = 2

    def __init__(self, angle=0, axes=np.array([0., 0., 1.0]), time=0.0, direct=Direction.Right):
        self.time = time
        self.direct = direct
        # angle in degrees
        self.angle = angle
        self.axes = axes

    def rotate_matrix(self):
        glRotatef(self.angle, self.axes[0], self.axes[1], self.axes[2])

    @staticmethod
    def generate(min_time, max_time):
        return Rotation(angle=random.uniform(0, 2*math.pi), axes=np.random.randint(0, 2, 3), time=random.uniform(min_time, max_time))

    def update_angle(self, global_time):
        if not self.time == 0:
            if self.direct == Rotation.Direction.Left:
                self.angle = global_time * 360 / self.time
            else:
                self.angle = -global_time * 360 / self.time
