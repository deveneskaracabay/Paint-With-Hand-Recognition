class Stack:
    # This class help us for storing finger points
    def __init__(self, color, point, back_item, control=True):

        # Stack object color value
        self.color = color
        # Fingers center point in the frame
        self.point = point
        # Back Stack object
        self.back_item = back_item
        # If back_item is None --> control equals to False
        self.control = control
