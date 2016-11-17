from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *


class SequenceTimer:
    # [(callback, ms), (callback, ms)]
    def __init__(self, time_events, without_delay=True):
        self.time_events = time_events
        self.i = 0
        self.without_delay = without_delay

    def timer_func(self, _=None):
        self.cur_time_event()[0]()
        self.i += 1
        self.__call_timer()

    def cur_time_event(self):
        if self.i < len(self.time_events):
            return self.time_events[self.i]

    def __call_timer(self):
        if self.i < len(self.time_events):
            glutTimerFunc(self.cur_time_event()[1], self.timer_func, 0)

    def start(self):
        if self.without_delay:
            self.time_events[0][0]()
            self.i += 1
        self.__call_timer()

    def push_event(self, time_event):
        self.time_events.append(time_event)
        if self.i == len(self.time_events-1):
            self.__call_timer()


