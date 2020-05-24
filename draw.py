# Modules
import pygame

# Game Files
import helper


def draw_text(display_surface, text_to_display, font, coords, text_color, bg_color=None, center=False):
    '''
    Displays text on the desired surface.

    Args:
        display_surface (pygame.Surface): The surface the text is to be displayed upon.

        text_to_display (str): The text to be written

        font (pygame.font.SysFont): Font object used to write the text

        coords ((int, int)): Where on the display_surface the object will be written,
            the text will be written from its upper-left corner.

        text_color ((int, int, int)): (R, G, B) color code for the desired color of text.

        bg_color ((int, int, int), optional): (R, G, B) color code for the background.
            If not included, the background is transparent.
    '''

    # Get both the surface and rectangle of the desired message
    text_surf, text_rect = helper.text_objects(
        text_to_display, font, text_color, bg_color)

    # Adjusts the location of the surface based on coordinates
    if not center:
        text_rect.topleft = coords
    else:
        text_rect.center = coords

    display_surface.blit(text_surf, text_rect)
