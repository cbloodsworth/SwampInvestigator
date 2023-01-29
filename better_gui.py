import pygame
from textwrap import wrap
FONT_SIZE = 20


class UI:
    def __init__(self):
        self.objects = {}
        self.buttons = {}

    def draw_all(self, screen):
        for key in self.objects:
            self.objects[key].draw(screen)
        for key in self.buttons:
            self.buttons[key].draw(screen)


class Object:
    def __init__(self):
        self.pos = [0, 0]
        self.color = pygame.Color(0, 255, 0, 255)


class Box(Object):
    def __init__(self):
        super().__init__()
        self.size = [200, 200]
        self.layer = pygame.Surface((200, 200))

    def get_bounds(self):
        center_x = self.pos[0] - self.size[0] // 2
        center_y = self.pos[1] - self.size[1] // 2
        bounds = pygame.Rect(center_x, center_y, self.size[0], self.size[1])
        return bounds

    def set_layer(self):
        self.layer = pygame.Surface((self.size[0], self.size[1]), pygame.SRCALPHA)
        self.layer.fill(self.color)

    def draw(self, screen):
        center_x = self.pos[0] - self.size[0] // 2
        center_y = self.pos[1] - self.size[1] // 2
        bounds = pygame.Rect(center_x, center_y, self.size[0], self.size[1])
        self.set_layer()
        pygame.draw.rect(self.layer, self.color, pygame.Rect(0, 0, self.size[0], self.size[1]), 0, 20)
        screen.blit(self.layer, (center_x, center_y))


class Textbox(Box):
    def __init__(self, font):
        super().__init__()
        self.text = ""
        self.font = font
        self.justify = "center"

    def draw(self, screen):
        text_width, text_height = self.font.size(self.text)
        center_x = self.pos[0] - self.size[0] // 2
        center_y = self.pos[1] - self.size[1] // 2
        bounds = pygame.Rect(center_x, center_y, self.size[0], self.size[1])
        self.set_layer()
        pygame.draw.rect(self.layer, self.color, bounds, 0, 20)
        screen.blit(self.layer, (center_x, center_y))
        if self.justify == "center":
            bounds_center = (bounds.center[0] - text_width / 2, bounds.center[1] - text_height / 2)
        else:
            bounds_center = (bounds.center[0] - self.size[0] // 2, bounds[1])
        if text_width > self.size[0]:
            chunks = wrap(self.text, 19)
        else:
            chunks = [self.text]
        count = 0
        for txt in chunks:
            label = self.font.render(txt, 1, (0, 0, 0))
            screen.blit(label, (bounds_center[0], bounds_center[1] + count))
            count += 16




class Imgbox(Box):
    def __init__(self):
        super().__init__()
