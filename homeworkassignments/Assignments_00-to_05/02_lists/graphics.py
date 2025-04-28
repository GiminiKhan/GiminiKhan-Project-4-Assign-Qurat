# graphics.py

class Canvas:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.objects = []

    def create_rectangle(self, x1, y1, x2, y2, fill):
        # Simulate the creation of a rectangle on the canvas
        rect = {'x1': x1, 'y1': y1, 'x2': x2, 'y2': y2, 'fill': fill}
        self.objects.append(rect)
        return rect

    def find_overlapping(self, x1, y1, x2, y2):
        # Simulate finding rectangles that overlap with the given coordinates
        overlapping_objects = []
        for obj in self.objects:
            if obj['x1'] < x2 and obj['x2'] > x1 and obj['y1'] < y2 and obj['y2'] > y1:
                overlapping_objects.append(obj)
        return overlapping_objects

    def set_color(self, rect, color):
        # Simulate changing the color of
