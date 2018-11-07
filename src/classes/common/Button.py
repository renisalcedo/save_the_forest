import pygame

class Button:
    def __init__(self, screen, left_top=(50,50), width_height=(20,20),
        color=[255,0,0]):
        # PROPERTY INITIALIZATION
        self.btn = pygame.Rect(left_top, width_height)
        self.color = color
        self.screen = screen

    def flip(self):
        # Display the button
        pygame.draw.rect(self.screen, self.color, self.btn)

    def on_click(self, event, fn):
        # Gets the mouse position
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = event.pos

            # Detect collision on the button
            if self.btn.collidepoint(mouse_pos):
                fn()