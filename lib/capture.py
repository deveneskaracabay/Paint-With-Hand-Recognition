import cv2 as cv
import sys


class Capture:
    # Video Reader class
    def __init__(self, video_path=0):
        # Initializing video capture
        # If path equals to 0(Zero), opening the first camera on the computer
        # If you want to process on the saved video, you can give video path
        self.capture = cv.VideoCapture(video_path)

    def read(self, flip=True):
        # Reading Frame
        ret, frame = self.capture.read()
        if flip and ret:
            frame = cv.flip(frame, 1)
        if ret:
            return frame
        print("video can't playing.\n\tProgram is closing...")
        sys.exit()

    def exit(self):
        self.capture.release()
