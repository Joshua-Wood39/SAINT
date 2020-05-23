# Modules
import pygame

# Game Files
import constants


class ui_Button:
    def __init__(self, surface, size, center_coords,
                 button_text=None,
                 color_box_mouseover=None,
                 color_box_default=None,
                 color_text_mouseover=None,
                 color_text_default=None):

        self.surface = surface
        self.size = size
        self.center_coords = center_coords
        self.button_text = button_text

        self.c_box_mo = color_box_mouseover
        self.c_box_dflt = color_box_default
        self.c_text_mo = color_text_mouseover
        self.c_text_dflt = color_text_default
        # Placeholders for the default colors
        self.c_c_box = color_box_default
        self.c_c_text = color_text_default

        self.rect = pygame.Rect((0, 0), self.size)
        self.rect.center = center_coords

    def update(self, player_input):

        mouse_clicked = False

        local_events, local_mouse_pos = player_input
        mouse_x, mouse_y = local_mouse_pos

        mouse_over = (mouse_x >= self.rect.left
                      and mouse_x <= self.rect.right
                      and mouse_y >= self.rect.top
                      and mouse_y <= self.rect.bottom)

        for event in local_events:
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    mouse_clicked = True

        if mouse_over and mouse_clicked:
            return True

        if mouse_over:
            self.c_c_box = self.c_box_mo
            self.c_c_text = self.c_text_mo
        else:
            self.c_c_box = self.c_box_dflt
            self.c_c_text = self.c_text_dflt

    def draw(self):

        pygame.draw.rect(self.surface, self.c_c_box, self.rect)
        if button_text:
            draw_text(self.surface,
                      self.button_text,
                      constants.FONT_DEBUG_PLACEHOLDER,
                      self.center_coords,
                      self.c_c_text,
                      center=True)
