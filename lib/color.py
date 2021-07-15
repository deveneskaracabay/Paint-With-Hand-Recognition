from .sys_path_append import add_path
add_path('..')
from conf import *


class Color:
    # Color class, which is the getting color names and values on the conf files.
    def __init__(self, name):
        self.name = name
        self.value = COLOR_DICT[name.upper()]
