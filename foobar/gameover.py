import pygame

from gamestate import GameState


class GameOver:
    def __init__(self, game):
        self.game = game

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.game.running = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    self.game.change_state(GameState.MENU)

    def update_logic(self):
        # Lógica de fim de jogo
        pass

    def render(self):
        # Renderizar tela de fim de jogo
        pass
