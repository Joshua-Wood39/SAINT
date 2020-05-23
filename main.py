# Modules
import pygame
import sys
import random

# Game Files
import constants


def menu_main():
    game_initialize()

    menu_running = True

    # TODO Need buttons referencing ui_Button component

    while menu_running:

        list_of_events = pygame.event.get()
        mouse_position = pygame.mouse.get_pos()

        game_input = (list_of_events, mouse_position)

        for event in list_of_events:
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        # TODO Button update if statements

        # TODO Draw the menu

        # Update the surface
        pygame.display.update()


def game_initialize():
    '''
    This will initialize the main window, pygame, and globals
    '''
    global SURFACE_MAIN
    global CLOCK, ASSETS, CAMERA, RANDOM_ENGINE
    global PREFERENCES

    # Initialize pygame
    pygame.init()

    # TODO Preference check and load

    # SURFACE_MAIN is the display surface, a special surface that serves
    # as the root console of the whole game. Anything that appears in the
    # game must be drawn to this console before it will appear.
    SURFACE_MAIN = pygame.display.set_mode(
        (constants.CAMERA_WIDTH, constants.CAMERA_HEIGHT))

    # TODO Assign camera object

    # TODO Assign assets object

    # The CLOCK tracks and limits cpu cycles
    CLOCK = pygame.time.Clock()

    # Random Number Engine
    RANDOM_ENGINE = random.SystemRandom()


if __name__ == '__main__':
    menu_main()
