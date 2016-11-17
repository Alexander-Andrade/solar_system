from Globe import Globe
from GlobePainters import StarPainter
import numpy as np


class Star(Globe):

    def __init__(self, center, radius, img_name, rot=None):
        Globe.__init__(self, center, radius, rot, StarPainter(self, img_name))
