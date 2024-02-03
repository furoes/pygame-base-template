import pygame

from gamestate import GameState


class Menu:
    def __init__(self, game):
        self.game = game

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.game.running = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    self.game.change_state(GameState.PLAYING)

    def update_logic(self):
        # Lógica do menu
        pass

    def render(self):
        # Renderizar itens do menu
        pass
