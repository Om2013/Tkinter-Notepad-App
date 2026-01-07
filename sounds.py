sounds.py
import pygame

class Sounds_Class:
    def __init__(self):
        # Initialize the mixer
        pygame.mixer.init()

        # Load your sounds (make sure files exist)
        self.click = pygame.mixer.Sound("sounds/click.wav")
        self.new = pygame.mixer.Sound("sounds/new.wav")
        self.open = pygame.mixer.Sound("sounds/open.wav")
        self.save = pygame.mixer.Sound("sounds/save.wav")
        self.error = pygame.mixer.Sound("sounds/error.wav")

