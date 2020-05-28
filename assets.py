# Modules
import pygame


class obj_Assets:
    def __init__(self):
        self.sound_list = []

        self.load_assets()

        self.volume_adjust()

    def load_assets(self):
        pass
        # TODO Add all art and sprites

        # TODO Add all audio

    def sound_add(self, file_address):
        new_sound = pygame.mixer.Sound(file_address)

        self.sound_list.append(new_sound)

        return new_sound

    def volume_adjust(self):
        # TODO loop through sounds and music to adjust volume
        pass
