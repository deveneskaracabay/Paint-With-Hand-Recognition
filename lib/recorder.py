from .sys_path_append import add_path
from .recorder_name_creator import date_time
import os
add_path('..')
from conf import *


class Recorder:
    # Video Recording Class
    def __init__(self, fps=20.0):
        # Initilazing video saver class
        self.path = os.path.join(RECORD_DIR_PATH, date_time)
        fourcc = cv.VideoWriter_fourcc(*'XVID')
        self.file = cv.VideoWriter(self.path, fourcc, fps, (WIDTH*2, HEIGHT))

    def add_image(self, frame):
        # Adding image on the video
        self.file.write(frame)

    def exit(self):
        # Saving video
        self.file.release()
        print(f'video is recorded to {self.path}')
