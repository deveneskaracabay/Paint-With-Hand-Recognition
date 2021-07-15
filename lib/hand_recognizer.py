import math
import mediapipe as mp
from .sys_path_append import add_path
add_path('..')
from conf import *

class HandRecognizer:
    def __init__(self):
        # Hand recognizer class for detect hand on image
        self.mpHands = mp.solutions.hands
        self.hands = self.mpHands.Hands()
        # self.mpDraw = mp.solutions.drawing_utils
        self.hand = self.results_landmarks = None

    def detection(self, frame):
        # This method detects hand with RGB Images
        frame_rgb = cv.cvtColor(frame, cv.COLOR_BGR2RGB)
        results = self.hands.process(frame_rgb)
        self.results_landmarks = results.multi_hand_landmarks
        # If result is None return None
        if self.results_landmarks is None:
            return None
        return self.control()

    def control(self):
        # if one hand is detected
        if len(self.results_landmarks) == 1:
            hand = self.results_landmarks[0]
            # index finger points
            f1x, f1y = hand.landmark[12].x*HEIGHT, hand.landmark[12].y*WIDTH
            # middle finger points
            f2x, f2y = hand.landmark[8].x*HEIGHT, hand.landmark[8].y*WIDTH
            # if the distance between index finger and middle finger is so close, return Nothing
            diff = math.sqrt(math.pow(f1x - f2x, 2) + math.pow(f1y - f2y, 2))
            if diff < 100:
                return None

        return self.results_landmarks
