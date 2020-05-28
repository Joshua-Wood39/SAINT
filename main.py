# Modules
import pygame
import sys
import random
import ui_components
import gzip
import pickle

# Game Files
import constants
import draw
import camera
import assets
import preferences


########################################################################################
# MENU - MAIN
########################################################################################


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
            # TODO Stop menu music
            game_new()
            game_main_loop()

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


########################################################################################
# GAME
########################################################################################


def game_main_loop():
    '''
    Loop the Main Game
    '''

    game_quit = False

    while not game_quit:

        # TODO Handle player input

        # TODO Draw the game

        # TODO Update the display

        # Tick the Clock
        CLOCK.tick(constants.GAME_FPS)


def game_initialize():
    '''
    This will initialize the main window, pygame, and globals
    '''
    global SURFACE_MAIN, SURFACE_WORLD_MAP, PLAYER
    global CLOCK, ASSETS, CAMERA, RANDOM_ENGINE
    global PREFERENCES

    # Initialize pygame
    pygame.init()
    pygame.font.init()

    # Preference check and load
    try:
        preferences_load()
    except:
        PREFERENCES = preferences.struct_Preferences()

    # SURFACE_MAIN is the display surface, a special surface that serves
    # as the root console of the whole game. Anything that appears in the
    # game must be drawn to this console before it will appear.
    SURFACE_MAIN = pygame.display.set_mode(
        (constants.CAMERA_WIDTH, constants.CAMERA_HEIGHT))

    # TODO Load World Map

    # Assign camera object
    CAMERA = camera.obj_Camera()

    # Assign assets object
    ASSETS = assets.obj_Assets()

    # The CLOCK tracks and limits cpu cycles
    CLOCK = pygame.time.Clock()

    # Random Number Engine
    RANDOM_ENGINE = random.SystemRandom()


def game_new():

    global GAME


def preferences_save():
    with gzip.open('data/pref', 'wb') as file:
        pickle.dump(PREFERENCES, file)


def preferences_load():
    global PREFERENCES

    with gzip.open('data/pref', 'rb') as file:
        PREFERENCES = pickle.load(file)


if __name__ == '__main__':
    menu_main()
