import pygame

from menu import Menu
from gameplay import Gameplay
from gameover import GameOver
from gamestate import GameState


class Game:
    def __init__(self):
        # Inicialize o Pygame
        pygame.init()

        # Configurar a tela
        self.screen = pygame.display.set_mode((800, 600))
        pygame.display.set_caption("Foobar")

        # Configurar o relógio
        self.clock = pygame.time.Clock()

        # Inicializar o estado do jogo
        self.current_state = GameState.MENU

        # Criar instâncias das classes lógicas
        self.menu = Menu(self)
        self.gameplay = Gameplay(self)
        self.game_over = GameOver(self)

        # Mapear estados do jogo para classes lógicas
        self.state_logic = {
            GameState.MENU: self.menu,
            GameState.PLAYING: self.gameplay,
            GameState.GAME_OVER: self.game_over,
        }

        # Sinalizador de execução (variável de execução)
        self.running = True

    def change_state(self, new_state):
        self.current_state = new_state

    def run(self):
        # Loop do jogo
        while self.running:
            current_logic = self.state_logic.get(self.current_state)

            if current_logic:
                print(self.current_state)
                current_logic.handle_events()
                current_logic.update_logic()
                current_logic.render()

            # Atualizar a tela
            pygame.display.flip()

            # Limitar a taxa de quadros
            self.clock.tick(60)

        # Encerrar o Pygame
        pygame.quit()
