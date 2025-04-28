# graphics.py

class Canvas:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.objects = []

    def create_rectangle(self, x1, y1, x2, y2, fill):
        rect = {'x1': x1, 'y1': y1, 'x2': x2, 'y2': y2, 'fill': fill}
        self.objects.append(rect)
        return rect

    def find_overlapping(self, x1, y1, x2, y2):
        overlapping_objects = []
        for obj in self.objects:
            if obj['x1'] < x2 and obj['x2'] > x1 and obj['y1'] < y2 and obj['y2'] > y1:
                overlapping_objects.append(obj)
        return overlapping_objects

    def set_color(self, rect, color):
        rect['fill'] = color

    def get_mouse_x(self):
        return 100  # Simulated mouse position for testing; replace with actual event handling in GUI

    def get_mouse_y(self):
        return 100  # Simulated mouse position for testing; replace with actual event handling in GUI

    def moveto(self, obj, x, y):
        obj['x1'] = x
        obj['y1'] = y
        obj['x2'] = x + 20
        obj['y2'] = y + 20

    def wait_for_click(self):
        pass  # Optional: Implement if integrating with GUI for click event handling

    def get_last_click(self):
        return 100, 100  # Simulate a click at (100, 100); adjust if integrating with GUI
