import pygame
class button:
    width = None
    y_axis = None
    def __init__(self, width, y_axis):
        self.width = width
        self.y_axis = y_axis

    def outer_push_box(self):
        return pygame.Rect(self.width - 63, 7 + (self.y_axis * 35), 56, 26)

    def inner_push_box(self):
        return pygame.Rect(self.width - 65, 5 + (self.y_axis * 35), 60, 30)


a = button(32, 423)
a.outer_push_box()
a.inner_push_box()