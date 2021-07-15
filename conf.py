import cv2 as cv


SCREEN_RATIO = 1.
WIDTH = int(640 * SCREEN_RATIO)
HEIGHT = int(480 * SCREEN_RATIO)
RECORD = True
RECORD_DIR_PATH = './records'
COLOR_DICT = {
    'WHITE': (255, 255, 255),
    'BLACK': (0, 0, 0),
    'YELLOW': (0, 255, 255),
    'GREEN': (0, 255, 0),
    'RED': (0, 0, 255),
    'BLUE': (255, 0, 0),
    'PURPLE': (255, 0, 255),
    'TURQUOISE': (255, 255, 0)
}
COLOR_BOX_RATIO = .1
fontFace = cv.FONT_HERSHEY_PLAIN
fontScale = SCREEN_RATIO
