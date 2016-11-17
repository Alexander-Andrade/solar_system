from Shape import Shape
from Orbit import Orbit
from SystemPainter import SystemPainter


class System:

    def __init__(self, master=None):
        self.master = master
        self.orbits = []
        self.satellites = []
        self.subsystems = []
        self.painter = SystemPainter(self)

    def set_master(self, master):
        self.master = master

    def add_satellite(self, satellite, orbit_radius, orbit_time, init_orbit_angle=0.0):
        self.satellites.append(satellite)
        orbit = Orbit(self.master, satellite, orbit_radius, orbit_time, init_orbit_angle)
        self.orbits.append(orbit)

    def append_subsystem(self, subsystem, orbit_radius, orbit_time, init_orbit_angle=0.0):
        self.subsystems.append(subsystem)
        orbit = Orbit(self.master, subsystem.master, orbit_radius, orbit_time, init_orbit_angle)
        self.orbits.append(orbit)

    def update_state(self, time):
        if self.master.rot:
            self.master.rot.update_angle(time)
        for orbit in self.orbits:
            orbit.update_slave_position(time)
        for satellite in self.satellites:
            if satellite.rot:
                satellite.rot.update_angle(time)
        for subsystem in self.subsystems:
            subsystem.update_state(time)

    def draw(self):
        self.painter.draw()
