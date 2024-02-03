import pygame

class Gameplay:
    def __init__(self, game):
        self.game = game

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.game.running = False

    def update_logic(self):
        # Lógica da jogabilidade
        pass

    def render(self):
        # Renderizar elementos da jogabilidade
        pass
