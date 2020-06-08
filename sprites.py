# Modules
import pygame

# Game Files
import constants


class obj_Spritesheet:
    '''
    Class used to grab images out of a sprite sheet. As a class, it
    allows you to access and subdivide portions of the spritesheet.

    Attributes:
        file_name (arg, str): String which contains the directory/filename of
            the image for use as a spritesheet.
        sprite_sheet (pygame.surface): The loaded spritesheet accessed through
            the file_name argument.
    '''

    def __init__(self, file_name):
        self.sprite_sheet = pygame.image.load(file_name).convert()

        self.tiledict = {'a': 0, 'b': 1, 'c': 2, 'd': 3, 'e': 4, 'f': 5, 'g': 6, 'h': 7, 'i': 8, 'j': 9, 'k': 10, 'l': 11, 'm': 12,
                         'n': 13, 'o': 14, 'p': 15, 'q': 16, 'r': 17, 's': 18, 't': 19, 'u': 20, 'v': 21, 'w': 22, 'x': 23, 'y': 24, 'z': 25}

    def get_image(self, column, row, width=constants.CELL_WIDTH, height=constants.CELL_HEIGHT, scale=None):
        '''
        This method returns a single sprite.

        Args:
            column (str): Letter which gets converted into an integer, column in the
                spritesheet loaded.
            row (int): row in the spritesheet to be loaded.
            width (int): individual sprite width in pixels.
            height (int): individual sprite height in pixels.
            scale ((width, height)) = If included, scales sprites to a new size.

        Returns:
            image_list (list): This method returns a single sprite contained within a 
                list loaded from the spritesheet property.
        '''

        image_list = []

        image = pygame.Surface([width, height]).convert()

        image.blit(self.sprite_sheet, (0, 0), (self.tiledict[column] * width,
                                               row * height,
                                               width, height))

        image.set_colorkey(constants.COLOR_BLACK)

        if scale:
            (new_w, new_h) = scale

            image = pygame.transform.scale(image, (new_w, new_h))

        image_list.append(image)

        return image_list

    def get_animation(self, column, row, width=constants.CELL_WIDTH, height=constants.CELL_HEIGHT, num_sprites=1, scale=None):
        '''
        This method returns a sequence of sprites.

        Args:
            column (str): Letter which gets converted to an integer, column in 
                the spritesheet to be loaded.
            row (int): row in the spritesheet to be loaded.
            width (int): individual sprite width in pixels.
            height (int): individual sprite height in pixels.
            num_sprites (int): number of sprites to be loaded in sequence.
            scale ((width, height)) = If included, scales the sprites to a new size.

        Returns:
            image_list (list): This method returns a sequence of sprites contained within
                a list loaded from the spritesheet property.
        '''

        image_list = []

        for i in range(num_sprites):
            # Create blank image
            image = pygame.Surface([width, height]).convert()

            # Copy image from sheet onto blank
            imgae.blit(self.sprite_sheet, (0, 0), (self.tiledict[column] * width + (width * i),
                                                   row * height,
                                                   width,
                                                   height))

            # Set transparency key to black
            image.set_colorkey(constants.COLOR_BLACK)

            if scale:
                (new_w, new_h) = scale

                image = pygame.transform.scale(image, (new_w, new_h))

            image_list.append(image)

        return image_list
