from .hand_recognizer import HandRecognizer
from .screen import Screen
from .capture import Capture
from .recorder import Recorder
from conf import *
from .sys_path_append import add_path
add_path('..')


class App:
    def __init__(self):
        # Initializing the App class
        # Creating video capture
        self.capture = Capture()
        # Creating hand recognizer
        self.hand_recognizer = HandRecognizer()
        # Create a screen
        self.screen = Screen()
        # if record mode on --> creat record object
        if RECORD:
            self.recorder = Recorder()

    def run(self):
        while True:
            # Reading frame
            frame = self.capture.read()
            # Frame resizing with the conf files values
            frame = cv.resize(frame, (WIDTH, HEIGHT))
            # Detecting hand
            results = self.hand_recognizer.detection(frame)

            # If hand recognizer detects a hand on the frame
            if results is not None:
                for hand in results:
                    # Calculating index finger points
                    index_finger = hand.landmark[8]
                    w, h = index_finger.x*WIDTH, index_finger.y*HEIGHT
                    center = int(w), int(h)

                    # Draw a circle on the image with fingers
                    frame = cv.circle(frame, center, 10, self.screen.color.value, thickness=-1)

                    # If finger on the color box points, Color box open
                    if h < self.screen.color_box_y:
                        frame = self.screen.creat_color_picker(frame, center=w)
                    # Else center appending the stack
                    else:
                        self.screen.add_stack(center)

            # If hand recognizer can't detect a hand in the frame, this scope is running
            else:
                frame = self.screen.creat_color_picker(frame)
            frame = self.screen.draw(frame)

            frame = self.screen.img_concatenate(frame)
            cv.imshow('image', frame)
            if RECORD:
                self.recorder.add_image(frame)
            if cv.waitKey(1) & 0xFF == 27:
                break

    def exit(self):
        # Closing capture and save record
        self.capture.exit()
        if RECORD:
            self.recorder.exit()
        cv.destroyAllWindows()
