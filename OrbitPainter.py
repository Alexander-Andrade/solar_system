from Painter import *
import math

class OrbitPainter(Painter):

    def __init__(self, orbit):
        self.orbit = orbit
        self.step = 0.05

    def calc_best_step(self):
        step = 0.1 / self.orbit.radius
        if step > 0.05:
            step = 0.05
        return step

    def draw(self):
        # glDisable(GL_LIGHTING)
        # glPushAttrib(GL_CURRENT_BIT)
        # glColor3f(1.0, 1.0, 1.0)
        # glBegin(GL_POINTS)
        # glColor3f(1.0, 1.0, 1.0)
        # # loop round from 0 to 2*PI and draw around the radius of the orbit using trigonometry
        # angle = 0.0
        # while angle < 6.283185307:
        #     glVertex3f(math.sin(angle)*self.orbit.radius, math.cos(angle)*self.orbit.radius, 0.0)
        #     angle += self.step
        # #glVertex3f(0.0, self.orbit.radius, 0.0)
        # glEnd()
        # glPopAttrib()
        # glEnable(GL_LIGHTING)
        pass
