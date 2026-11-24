import pygame

from config import resource_path


pygame.mixer.init()

mythicsound = pygame.mixer.Sound(resource_path("sols-rng-epic-roll_CCLMQGC.mp3"))
legsound = pygame.mixer.Sound(resource_path("1m-server-message.mp3"))
ultrasound = pygame.mixer.Sound(resource_path("100m-server-message.mp3"))
brsound = pygame.mixer.Sound(resource_path("1b-server-message.mp3"))
clicksound = pygame.mixer.Sound(resource_path("click.wav"))
