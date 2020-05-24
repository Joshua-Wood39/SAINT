# Modules
import pygame
import sys
import random
import ui_components

# Game Files
import constants
import draw


def menu_main():
    game_initialize()

    menu_running = True

    # Title Address
    title_x = constants.CAMERA_WIDTH/2
    title_y = constants.CAMERA_HEIGHT/2
    title_text = "Working Title: SAINTS"

    # Button Addresses
    button_y_offset = 40
    new_game_button_y = title_y + button_y_offset
    load_game_button_y = new_game_button_y + button_y_offset
    options_button_y = load_game_button_y + button_y_offset
    quit_button_y = options_button_y + button_y_offset

    # Buttons referencing ui_Button component
    new_game_button = ui_components.Button(SURFACE_MAIN,
                                           (150, 30),
                                           (title_x, new_game_button_y),
                                           "New Game",
                                           constants.COLOR_D_GREY,
                                           constants.COLOR_GREY,
                                           constants.COLOR_BLUE,
                                           constants.COLOR_BLACK)

    load_game_button = ui_components.Button(SURFACE_MAIN,
                                            (150, 30),
                                            (title_x, load_game_button_y),
                                            "Load",
                                            constants.COLOR_D_GREY,
                                            constants.COLOR_GREY,
                                            constants.COLOR_BLUE,
                                            constants.COLOR_BLACK)

    options_button = ui_components.Button(SURFACE_MAIN,
                                          (150, 30),
                                          (title_x, options_button_y),
                                          "Options",
                                          constants.COLOR_D_GREY,
                                          constants.COLOR_GREY,
                                          constants.COLOR_BLUE,
                                          constants.COLOR_BLACK)

    quit_button = ui_components.Button(SURFACE_MAIN,
                                       (150, 30),
                                       (title_x, quit_button_y),
                                       "Quit",
                                       constants.COLOR_D_GREY,
                                       constants.COLOR_GREY,
                                       constants.COLOR_BLUE,
                                       constants.COLOR_BLACK)

    while menu_running:

        list_of_events = pygame.event.get()
        mouse_position = pygame.mouse.get_pos()

        game_input = (list_of_events, mouse_position)

        for event in list_of_events:
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        # Button update if statements
        if new_game_button.update(game_input):
            # Start a game_new() and game_main_loop()
            pass

        if load_game_button.update(game_input):
            # Load submenu of saved games, menu_game_load()
            pass

        if options_button.update(game_input):
            # Load submenu for game options and preferences, menu_options()
            pass

        if quit_button.update(game_input):
            # Quit the game
            pygame.quit()
            sys.exit()

        # TODO Update menu with actual background
        SURFACE_MAIN.fill(constants.COLOR_BLACK)

        # Draw title
        draw.draw_text(SURFACE_MAIN,
                       title_text,
                       constants.FONT_DEBUG_PLACEHOLDER,
                       (title_x, title_y),
                       constants.COLOR_BLUE,
                       bg_color=constants.COLOR_WHITE,
                       center=True)

        # Draw the buttons
        new_game_button.draw()
        load_game_button.draw()
        options_button.draw()
        quit_button.draw()

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
    pygame.font.init()

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
