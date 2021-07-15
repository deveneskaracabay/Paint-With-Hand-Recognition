import cv2

from .stack import Stack
from .color import Color
import math
import time
from .sys_path_append import add_path
import numpy as np
add_path('..')
from conf import *


class Screen:
    def __init__(self):
        # Initializing class
        self.height = HEIGHT
        self.width = WIDTH
        self.stack = Stack(None, None, None, False)
        self.color = Color('white')
        self.color_box_size = len(COLOR_DICT) + 1
        self.color_box_x = int(WIDTH // self.color_box_size)
        self.color_box_y = int(COLOR_BOX_RATIO * HEIGHT)
        self.color_names = COLOR_DICT.keys()
        self.color_values = COLOR_DICT.values()
        self.adding_time = self.pt1 = self.pt2 = 0
        self.blank_screen = np.zeros((self.height, self.width, 3), dtype=np.uint8)

    def add_stack(self, center):
        # Finger point append to the Stack object
        temp_stack = Stack(self.color, center, self.stack)
        self.stack = temp_stack
        self.adding_time = time.time()

    def line_control(self):
        # Control finger point for opening color menu
        x1, y1 = self.pt1
        x2, y2 = self.pt2
        limit = 80
        x = math.pow((x2 - x1), 2)
        y = math.pow((y2 - y1), 2)
        hip = math.sqrt(x + y)
        if hip < limit:
            return True
        return False

    def img_concatenate(self, frame):
        return cv2.hconcat([frame, self.blank_screen])

    def draw(self, frame, thickness=5):
        # Draw on the image with stack object values
        temp = self.stack
        if not temp.control:
            return frame
        while True:
            back_item = temp.back_item
            if back_item.back_item is not None:
                self.pt1 = temp.point
                self.pt2 = back_item.point
                if self.line_control():
                    cv.line(frame, self.pt1, self.pt2, temp.color.value, thickness=thickness)
                    cv.line(self.blank_screen, self.pt1, self.pt2, temp.color.value, thickness=thickness)

                else:
                    cv.circle(frame, temp.point, thickness, temp.color.value, thickness=-1)
                    cv.circle(self.blank_screen, temp.point, thickness, temp.color.value, thickness=-1)
                temp = temp.back_item

            else:
                return frame

    def creat_clear_box(self, frame, clear=False):
        # Deleting the Stack values and refreshing image
        if clear:
            self.stack = Stack(None, None, None, False)
            self.blank_screen = np.zeros((self.height, self.width, 3), dtype=np.uint8)
            rect_font_color = 'BLACK'
            rect_text = 'CLEARED'
            rect_thickness = -1
            text_start_point = 3
            y_point = self.color_box_y+30
        else:
            rect_font_color = 'WHITE'
            rect_text = 'CLEAR'
            rect_thickness = 0
            text_start_point = 10
            y_point = self.color_box_y//2
        cv.rectangle(frame, (0, 0), (self.color_box_x, self.color_box_y), COLOR_DICT['WHITE'], thickness=rect_thickness)
        cv.putText(frame, rect_text, (text_start_point, y_point), fontFace, fontScale,
                   COLOR_DICT[rect_font_color], thickness=2)
        return frame

    def creat_color_picker(self, frame, circle_radius=20, center=None):
        # Color picker creator method with the control method
        time_control = time.time() - self.adding_time
        if time_control < .5:
            return frame

        if center is not None:
            hover_index = (center//self.color_box_x) - 1
            if hover_index == -1:
                frame = self.creat_clear_box(frame, True)
            else:
                frame = self.creat_clear_box(frame, False)
        else:
            hover_index = None
            frame = self.creat_clear_box(frame, False)

        box_x = int(3*self.color_box_x/2)
        box_y = self.color_box_y//2
        for count, data in enumerate(zip(self.color_values, self.color_names)):
            value, name = data
            thickness = 5
            if count == hover_index:
                thickness = -1
                cv.putText(frame, name, (box_x - int(self.color_box_x // 3),
                                         self.color_box_y + 30), fontFace, fontScale, value, thickness=2)
                self.color = Color(name)
            cv.circle(frame, (box_x, box_y), circle_radius, value, thickness=thickness)

            box_x += self.color_box_x
        return frame
