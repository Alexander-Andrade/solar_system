from Painter import *
from Texture import Texture2D
import math


class SystemPainter(Painter):

    def __init__(self, system):
        self.system = system

    def translate_to_sys_coords(self):
        glTranslatef(self.system.master.center[0], self.system.master.center[1], self.system.master.center[2])

    def draw(self):
        glPushMatrix()
        self.translate_to_sys_coords()
        for subsystem in self.system.subsystems:
            subsystem.draw()
        for orbit in self.system.orbits:
            orbit.draw()
        for satellite in self.system.satellites:
            satellite.draw()
        glPopMatrix()
        self.system.master.draw()
