from Shape import Shape
from OrbitPainter import OrbitPainter
import numpy as np
import math


class Orbit(Shape):

    def __init__(self, master_shape, slave_shape, radius, orbit_time, init_angle=0.0):
        Shape.__init__(self, painter=OrbitPainter(self))
        self.radius = radius
        self.init_angle = init_angle
        # time it takes to complete 1 orbit
        self.orbit_time = orbit_time
        self.master_shape = master_shape
        self.slave_shape = slave_shape

    # Calculate its position in 3d spacein the orbit using the given time value
    def update_slave_position(self, time):
        angle = self.init_angle + time*math.pi/self.orbit_time
        slave_center = np.zeros(3)
        slave_center[0] = math.sin(angle)*self.radius
        slave_center[1] = math.cos(angle)*self.radius
        slave_center[2] = 0
        self.slave_shape.center = slave_center

    def master_center(self):
        return self.master_shape.center
