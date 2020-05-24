# Modules
import pygame


def text_objects(incoming_text, incoming_font, incoming_color, incoming_bg):
    '''
    Generates the text objects used for drawing text.

    Arg:
        incoming_text (str)
        incoming_font (pygame.font.SysFont)
        incoming_color ((int, int, int))
        incoming_bg ((int, int, int), optional)

    Returns:
        Text_surface (pygame.Surface)
        Text_surface.get_rect() (pygame.Rect)
    '''

    # If there is a background color, render with that
    if incoming_bg:
        Text_surface = incoming_font.render(incoming_text,
                                            False,
                                            incoming_color,
                                            incoming_bg)
    else:
        Text_surface = incoming_font.render(incoming_text,
                                            False,
                                            incoming_color)

    return Text_surface, Text_surface.get_rect()
